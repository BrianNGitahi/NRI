
#%%
import numpy as np
import matplotlib.pyplot as plt
import torch
import seaborn 
import scipy as sp
import h5py


#%%
with h5py.File("/Users/briangitahi/Desktop/Summer '25/Saxena Lab/Data/20230804_121600_1.1_converted.analysis.h5", "r") as f:
    dset_names = list(f.keys())
    locations = f["tracks"][:].T
    node_names = [n.decode() for n in f["node_names"][:]]

print("===filename===")
print("/Users/briangitahi/Desktop/Summer '25/Saxena Lab/Data")
print()

print("===HDF5 datasets===")
print(dset_names)
print()

print("===locations data shape===")
print(locations.shape)
print()

print("===nodes===")
for i, name in enumerate(node_names):
    print(f"{i}: {name}")
print()


#%%
frame_count, node_count, _, instance_count = locations.shape

print("frame count:", frame_count)
print("node count:", node_count)
print("instance count:", instance_count)

#%%