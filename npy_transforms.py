import os
import argparse
import torchio as tio
import numpy as np
import torch
import config as cfg

#%%
def transform_and_save_npy(nii_path, output_path, transforms):
    subject = tio.Subject(img=tio.ScalarImage(nii_path))
    subject = transforms(subject)
    data = subject.img.data.squeeze(0).numpy()  # Remove channel dimension
    np.save(output_path, data)

#%%
def process_nifti_files(root_dir, npy_folder, transforms):
    nii_files = [f for f in os.listdir(root_dir) if f.endswith('_deskulled.nii.gz')]
    for nii_file in nii_files:
        nii_path = os.path.join(root_dir, nii_file)
        npy_file = nii_file.replace('_deskulled.nii.gz', '') + '.npy'
        output_path = os.path.join(npy_folder, npy_file)

        if os.path.exists(output_path):
            print(f"Skipping {npy_file}, already exists.")
            continue

        transform_and_save_npy(nii_path, output_path, transforms)
        print(f"Saved: {output_path}")

#%%
if __name__ == "__main__":

    deskull_folder = cfg.deskull_folder
    npy_folder = cfg.npy_folder
    os.makedirs(npy_folder, exist_ok=True)

    # Full transform pipeline
    transforms = tio.Compose([
        tio.Resample((1, 1, 1)),  # Resample to 1mm isotropic
        tio.CropOrPad((cfg.crop_size, cfg.crop_size, cfg.crop_size)),  # Crop/Pad to 180³
        tio.Resize((cfg.img_size, cfg.img_size, cfg.img_size)),  # Downscale to 96³
        tio.ZNormalization()  # Normalize intensity
    ])

    # Process
    process_nifti_files(deskull_folder, npy_folder, transforms)

    # Report
    npy_count = len([f for f in os.listdir(npy_folder) if f.endswith('.npy')])
    print(f"Total .npy files in {npy_folder}: {npy_count}")
