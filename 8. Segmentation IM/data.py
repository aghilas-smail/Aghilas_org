import os
import numpy as np
import cv2
import pandas as pd
import sys
import PIL.Image as Image
import matplotlib.pyplot as plt
import matplotlib as mpl


image_path = ''
image_save_path = ''

image_ligne = 420
image_col = 580

# Crée une fonction de train pour la data.
def create_train_data():
    train_image_path = os.path.join(image_path,'train')
    images = os.listdir(train_image_path)
    total = len(images) / 2
    
