"""
Configuration file for neuroimaging preprocessing pipeline
"""

# === Cohort Settings ===
cohort = 'nako'
reg_type = 'Affine'
crop_size = 180 
img_size = 96  # Add your image size here

# === Paths ===
template_path = '../images/templates/mni_icbm152_nlin_asym_09c/mni_icbm152_t1_tal_nlin_asym_09c.nii'
dcm2nii_path = '../.venv/bin/dcm2niix/console/build/dcm2niix'

dcm_folder = f'../{cohort}/dcm_raw/'
input_folder = f'../{cohort}/nifti_raw/'
n4_folder = f'../{cohort}/nifti_n4/'
reg_folder = f'../{cohort}/nifti_reg_{reg_type}/'
deskull_folder = f'../{cohort}/nifti_deskull_{reg_type}/'
npy_folder = f'../{cohort}/npy{img_size}/'

# === Processing Parameters ===
N4_PROCESSES = 4
REG_PROCESSES = 4
GPU_ID = 0
