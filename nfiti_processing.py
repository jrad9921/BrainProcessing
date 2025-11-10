import os
import subprocess
import ants
import config as cfg
import multiprocessing as mp


fixed = ants.image_read(cfg.template_path)

# Collect all input NIfTIs
files_raw = sorted([f for f in os.listdir(cfg.input_folder) if f.endswith('.nii.gz')])

def bias_correct(filename):
    try:
        in_path  = os.path.join(cfg.input_folder, filename)
        out_name = filename.replace('.nii.gz', '_n4.nii.gz')
        out_path = os.path.join(cfg.n4_folder, out_name)

        if os.path.exists(out_path):
            print(f"[SKIP] N4 exists: {out_name}")
            return out_name

        print(f"[INFO] N4: {filename} -> {out_name}")
        img = ants.image_read(in_path)
        corrected = ants.n4_bias_field_correction(img)
        ants.image_write(corrected, out_path)
        return out_name
    except Exception as e:
        print(f"[ERROR] N4 {filename}: {e}")

def register(n4_name):
    try:
        if not n4_name or not n4_name.endswith('_n4.nii.gz'):
            return
        in_path  = os.path.join(cfg.n4_folder, n4_name)
        out_name = n4_name.replace('_n4.nii.gz', f'_registered.nii.gz')
        out_path = os.path.join(cfg.reg_folder, out_name)

        if os.path.exists(out_path):
            print(f"[SKIP] Registered exists: {out_name}")
            return out_name

        print(f"[INFO] REG: {n4_name} -> {out_name}")
        moving = ants.image_read(in_path)
        reg = ants.registration(fixed=fixed, moving=moving, type_of_transform=cfg.reg_type)
        ants.image_write(reg['warpedmovout'], out_path)
        return out_name
    except Exception as e:
        print(f"[ERROR] REG {n4_name}: {e}")

def deskull(reg_name, gpu_id=0):
    try:
        if not reg_name or not reg_name.endswith('_registered.nii.gz'):
            return
        in_path  = os.path.join(cfg.reg_folder, reg_name)
        out_name = reg_name.replace('_registered.nii.gz', '_deskulled.nii.gz')
        out_path = os.path.join(cfg.deskull_folder, out_name)

        if os.path.exists(out_path):
            print(f"[SKIP] Deskulled exists: {out_name}")
            return out_name

        print(f"[INFO] BET: {reg_name} -> {out_name} (GPU {gpu_id})")
        cmd = f'hd-bet -i "{in_path}" -o "{out_path}" -device cuda:{gpu_id}'
        subprocess.run(cmd, shell=True, check=True)
        return out_name
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] BET {reg_name}: {e}")
    except Exception as e:
        print(f"[ERROR] BET {reg_name}: {e}")

if __name__ == "__main__":
    os.makedirs(cfg.n4_folder, exist_ok=True)
    os.makedirs(cfg.reg_folder, exist_ok=True)
    os.makedirs(cfg.deskull_folder, exist_ok=True)

    print("=== N4 bias correction ===")
    with mp.Pool(processes=4) as pool:
        n4_names = list(pool.map(bias_correct, files_raw))

    print("=== Registration ===")
    with mp.Pool(processes=4) as pool:
        reg_names = list(pool.map(register, n4_names))

    print("=== Deskulling (sequential on GPU 0) ===")
    for name in reg_names:
        deskull(name, gpu_id=0)

