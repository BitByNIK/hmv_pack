import numpy as np
import pandas as pd

def delete_record(incsv_file, outcsv_file):
    
    dataset = pd.read_csv(incsv_file)
    
    dataset = dataset.apply(pd.to_numeric, errors='coerce')
    new_dataset = dataset.dropna()
    
    new_dataset.to_csv(outcsv_file, index=False)
    

def replace_record(incsv_file, outcsv_file):
    
    dataset = pd.read_csv(incsv_file)
    
    dataset = dataset.apply(pd.to_numeric, errors='coerce')
    new_dataset = dataset.fillna(dataset.mean())
    
    new_dataset.to_csv(outcsv_file, index=False)