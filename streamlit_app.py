import streamlit as st
from ultralytics import YOLO
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt
import torch
import os

# Title
st.title("🦷 Impacted Canine Detector")
st.write("Upload a dental X-ray or image to detect impacted canines and classify their type.")

# Load YOLOv12 model from local models folder
MODEL_PATH = "./best.pt"
if not os.path.exists(MODEL_PATH):
    st.error(f"Model not found at: {MODEL_PATH}. Please add best.pt to /models.")
    st.stop()

@st.cache_resource
def load_model():
    return YOLO(MODEL_PATH)

model = load_model()

# Upload file
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Run detection
    with st.spinner("Detecting impacted canines..."):
        results = model.predict(image, save=False, conf=0.25)
        result = results[0]

    # Show annotated image
    st.image(result.plot(), caption="Detection Result", use_container_width=True)

    # Extract data
    pred_data = []
    for box in result.boxes:
        cls_id = int(box.cls[0])
        class_name = model.names[cls_id]
        confidence = float(box.conf[0])
        xywh = box.xywh[0].tolist()
        pred_data.append({
            "class": class_name,
            "confidence": round(confidence, 3),
            "center_x": round(xywh[0], 1),
            "center_y": round(xywh[1], 1),
            "width": round(xywh[2], 1),
            "height": round(xywh[3], 1)
        })

    # Show JSON-style output
    if pred_data:
        st.subheader("📋 Detection Summary")
        st.dataframe(pd.DataFrame(pred_data))
    else:
        st.warning("No impacted canines detected.")
