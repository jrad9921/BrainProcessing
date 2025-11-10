
# %%
import os
import numpy as np
import matplotlib.pyplot as plt
import random
import config as cfg


# Get list of .npy files and sort them
npy_files = sorted([f for f in os.listdir(cfg.npy_folder) if f.endswith('.npy')])

# Randomly select 20 files
random_files = random.sample(npy_files, 100)

# Set up 4x5 grid
fig, axes = plt.subplots(12, 10, figsize=(40, 48))

for i, fname in enumerate(random_files):
    img = np.load(os.path.join(cfg.npy_folder, fname))
    axial_slice = img[:, :, img.shape[2] // 2]  # Middle axial slice
    #axial_slice = img[:, img.shape[2] // 2, :]  # Middle axial slice
    #axial_slice = img[img.shape[2] // 2, :, :]  # Middle axial slice
    ax = axes[i // 10, i % 10]
    ax.imshow(axial_slice.T, cmap='gray', origin='lower')
    ax.set_title(fname, fontsize=20)
    ax.axis('off')

plt.tight_layout()
plt.show()

# %%
