"""
Configuration file for neuroimaging preprocessing pipeline
"""

# === Cohort Settings ===
cohort = 'you/cohort'
reg_type = 'Affine'
crop_size = 180 
img_size = 96  # Add your image size here

# === Paths ===
template_path = 'path/to/your/file'
dcm2nii_path = 'path/to/your/file'

dcm_folder = 'path/to/your/folder'
input_folder = 'path/to/your/folder'
n4_folder = 'path/to/your/folder'
reg_folder = 'path/to/your/folder'
deskull_folder = 'path/to/your/folder'
npy_folder = 'path/to/your/folder'

# === Processing Parameters ===
N4_PROCESSES = 4
REG_PROCESSES = 4
GPU_ID = 0
