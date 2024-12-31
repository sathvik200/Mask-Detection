import numpy as np
import cv2
import pickle
import keras
import sklearn
import streamlit as st
from PIL import Image

model = pickle.load(open('model.pkl', 'rb'))

st.header("Mask Detection System")

def detect_face_mask(img):
    y_pred = model.predict(img.reshape(1,224,224,3))
    predicted_classes = (y_pred > 0.5).astype("int32")
    
    return predicted_classes[0][0]


photo = st.camera_input("Take a picture")

if photo:
    image = Image.open(photo)
    image_np = np.array(image)
    resized_image = cv2.resize(image_np, (224, 224))

    y_pred = detect_face_mask(resized_image)
    
    if y_pred==0:
        st.text("The person is wearing mask")
    else:
        st.text("The person is not wearing mask")
