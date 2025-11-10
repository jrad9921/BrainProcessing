#%%
import nibabel as  nib
import matplotlib.pyplot as plt
import numpy as np
import os
from glob import glob
from nibabel.orientations import aff2axcodes
import config as cfg
#%%
# Set folder path
folder_path = cfg.deskull_folder

# Get list of .nii.gz files
nii_files = sorted(glob(os.path.join(folder_path, '*.nii.gz')))

# Limit to top 10 files
nii_files = nii_files[:20]
print(nii_files)
#%%
for i, file_path in enumerate(nii_files):
    img = nib.load(file_path)
    data = img.get_fdata()
    print(data.shape)
    # Define slice indices
    axial_idx = data.shape[2] // 2
    coronal_idx = data.shape[1] // 2
    sagittal_idx = data.shape[0] // 2

    # Plot all three views
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    # Axial
    axes[0].imshow(data[:, :, axial_idx].T, cmap='gray', origin='lower')
    axes[0].set_title('Axial View')
    axes[0].axis('off')

    # Coronal
    axes[1].imshow(data[:, coronal_idx, :].T, cmap='gray', origin='lower')
    axes[1].set_title('Coronal View')
    axes[1].axis('off')

    # Sagittal
    axes[2].imshow(data[sagittal_idx, :, :].T, cmap='gray', origin='lower')
    axes[2].set_title('Sagittal View')
    axes[2].axis('off')

    plt.tight_layout()
    plt.show()
    print(file_path)
    print("Orientation:", aff2axcodes(img.affine))
#%%
