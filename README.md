# 🦷 Impacted Canine Detector (YOLOv12 + Streamlit)

This is a simple local Streamlit app that lets you upload an image and detect/classify impacted canine types using a trained YOLOv12 model.

## 🧱 Project Structure


## 🚀 How to Run

1. Make sure Python 3.8+ is installed.
2. Install requirements:

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py


## 🚀 Features
Upload any .jpg or .png image

Get bounding boxes + class labels for detected canine types

JSON-style table of predictions: class, confidence, center_x/y, width, height

___________________________________________________________________________________________________________________________________________________________

🧑‍💻 Instructions for the Dentist (README.md)

# 🦷 Impacted Canine Classifier

This app allows you to upload dental X-ray images and automatically classify them into one of six categories using AI.

---

## ✅ What You Need

1. A Windows PC
2. [Docker Desktop](https://www.docker.com/products/docker-desktop/)
3. This folder: `impacted_canine_app` with all files, including:
   - `models/best.pt`
   - `Dockerfile`
   - `streamlit_app.py`

---

## 🚀 How to Run

1. **Install Docker Desktop**  
   Download and install Docker from: https://www.docker.com/products/docker-desktop  
   Ensure Docker is running.

2. **Download the App Folder**  
   Place the `impacted_canine_app` folder somewhere on your PC (e.g., Desktop).

3. **Open PowerShell or Command Prompt**  
   Navigate to the app folder:
   ```bash
   cd path\to\impacted_canine_app

