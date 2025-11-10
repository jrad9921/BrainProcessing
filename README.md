# BrainProcessing
Preprocessing for Brain sMRI:
## Steps
### 1. Extracting dcms
- extract_zip.py creates a structured dcm_raw folder after extracting downloaded data contained in zips
### 2. Dcm to niftii conversion 
- dcm_processing.py converts structured dcms to niftiis  #if you already have a BIDS-structured dcm_raw folder 
### 3. Nifti preprocessing 
- nifti_processing.py
  - bias corrects registered images and saves into nifti_n4 folder  
  - registers raw niftiis and saves into nifti_reg folder 
  - skull-stripps registered niftiis and saves into nifti_deskull folder
### 4. Tensor transformations
- npy_transforms.py includes cropping, normalization and resizing and creation of npy tensors

## Data Layout  

All datasets reside under a top-level `images/` directory outside the preprocessing code in BrainProcessing directory which should preferably be parallel to image directory but not inside. 
Each cohort has its own subdirectory for images at different preprocessing steps.

Data Tree

```text
images/
├── {cohort1}/
│   ├── dcm_cmprs/
│   │   ├── batch1.zip
│   │   ├── batch2.zip
│   │   └── ...
│   ├── dcm_raw/
│   │   ├── {eid1}/
│   │   │   ├── xx1.dcm
│   │   │   ├── xx2.dcm
│   │   │   └── ...
│   │   └── {eid2}/
│   ├── nifti_raw/
│   │   ├── {eid1}.nii.gz
│   │   └── ...
│   ├── nifti_reg/
│   │   ├── {eid1}_registered.nii.gz
│   │   └── ...
│   ├── nifti_deskull/
│   │   ├── {eid1}_deskulled.nii.gz
│   │   └── ...
│   ├── npy_{cohort1}180/
│   │   ├── {eid1}.npy
│   │   └── ...
├── {cohort2}/
├── {cohort3}/...
```


