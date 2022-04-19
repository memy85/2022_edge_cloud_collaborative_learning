
import pydicom as pdm
from PIL import Image
import numpy as np
from torchvision import transforms
from pathlib import Path

def preprocess_dicom(full_path:bool, file_path=None, file_name=None, resize_scale=None):
    if full_path : 
        img = pdm.dcmread(file_name).pixel_array
    else : 
        if '.dcm' not in file_name : 
            dicom_file_name = Path(file_path).joinpath(file_name + '.dcm')
            img = pdm.dcmread(dicom_file_name).pixel_array
        else : 
            dicom_file_name = Path(file_path).joinpath(file_name)
            img = pdm.dcmread(dicom_file_name).pixel_array
            
    img = Image.fromarray(img)
    # img = img.resize((resize_scale, resize_scale))
    
    preprocess = transforms.Compose([
        transforms.Resize(resize_scale),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean = [0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    
    img_tensor = preprocess(img)
    input_batch = img_tensor.unsqueeze(0)
    return input_batch
    
