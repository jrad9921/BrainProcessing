import config as cfg
from pathlib import Path
import subprocess 

def dcm_to_nifti(
    input_dir: str = cfg.dcm_folder,
    output_dir: str = cfg.input_folder
):
    """Simplified version assuming dcm2niix is in PATH"""
    
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    for subj_dir in Path(input_dir).iterdir():
        if not subj_dir.is_dir():
            continue
            
        subj_id = subj_dir.name
        
        if list(Path(output_dir).glob(f"{subj_id}_*.nii.gz")):
            print(f"Skipping {subj_id}: NIfTI already exists.")
            continue
        
        print(f"Converting {subj_id}...")
        
        subprocess.run([
            "dcm2niix",
            "-z", "y",
            "-f", f"{subj_id}_%s",
            "-o", output_dir,
            str(subj_dir)
        ], check=True)


# Or specify custom paths
dcm_to_nifti()