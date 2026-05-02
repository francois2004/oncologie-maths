"""module able to load data from a set of RMI's"""

import numpy as np 
import nibabel as nib

class Loader : 
    @staticmethod
    def load_patient(patient_path): 
        data = {
            "flair" : nib.load(f"{patient_path}_flair.nii.gz"),
            "t1" : nib.load(f"{patient_path}_t1.nii.gz"),
            "t1ce" : nib.load(f"{patient_path}_t1ce.nii.gz"),
            "t2" : nib.load(f"{patient_path}_t2.nii.gz"),
            "seg" : nib.load(f"{patient_path}_seg.nii.gz"),
        }
        return data
    
    @staticmethod
    def load_patient_data(patient_path): 
        data = {
            "flair" : nib.load(f"{patient_path}_flair.nii.gz").get_fdata(),
            "t1" : nib.load(f"{patient_path}_t1.nii.gz").get_fdata(),
            "t1ce" : nib.load(f"{patient_path}_t1ce.nii.gz").get_fdata(),
            "t2" : nib.load(f"{patient_path}_t2.nii.gz").get_fdata(),
            "seg" : nib.load(f"{patient_path}_seg.nii.gz").get_fdata(),
        }
        return data
    