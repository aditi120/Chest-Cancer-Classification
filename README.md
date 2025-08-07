# 🧠 Chest Cancer Classifier using CNN & Transfer Learning

This project aims to detect chest cancer using deep learning techniques, specifically Convolutional Neural Networks (CNNs) with transfer learning (e.g., VGG16). The model classifies chest X-ray images into appropriate categories (e.g., cancerous vs. non-cancerous).

---

## 📌 Table of Contents

- [Overview](#overview)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Workflow](#workflow)
- [Model Architecture](#model-architecture)
- [License](#license)

---

## 🧐 Overview

This project is built for binary image classification on chest X-rays using TensorFlow and Keras. It follows a modular, component-driven ML pipeline that is easy to maintain and scale.

Key Features:
- Uses pretrained CNN backbone (like VGG16 with `weights='imagenet'`)
- Implements data augmentation
- Modular code design
- Version-controlled using **DVC**
- YAML-based configuration management

---

## ⚙️ Tech Stack

- Python
- TensorFlow / Keras
- OpenCV / PIL
- Pandas / NumPy
- Matplotlib / Seaborn
- PyYAML
- DVC (Data Version Control)
- Flask (optional for deployment)
- Docker (optional)

---

## 📁 Project Structure

```bash
├── .dvc/
├── config/
│   ├── config.yaml
│   └── params.yaml
├── artifacts/
├── src/
│   ├── config/
│   ├── components/
│   ├── pipeline/
│   └── utils/
├── notebooks/
├── app/ (Flask app)
├── dvc.yaml
├── main.py
├── requirements.txt
├── README.md



🔁 Workflow
This is the typical flow you should follow when updating or retraining the model:

✅ Update config.yaml

Set dataset path, model directory, etc.

✅ Update params.yaml

Tune image size, learning rate, epochs, etc.

✅ Update the entity class

Define schema for configuration entities (e.g., DataIngestionConfig, TrainingConfig)

✅ Update the configuration manager in src/config

Load and parse YAML files using Path and ConfigBox

✅ Update the components

Modify or add logic in modules like data_ingestion.py, prepare_base_model.py, training.py, etc.

✅ Update the pipeline

Create or update pipelines in src/pipeline folder (e.g., training_pipeline)

✅ Update main.py

Sequentially call the training/testing pipeline and add logging

✅ Update dvc.yaml

Define stages: data ingestion → model training → evaluation

✅ Track changes with DVC

🧠 Model Architecture
Pretrained Backbone: VGG16 with include_top=False

Custom Head: Flatten → Dense → Softmax

Optimizer: SGD

Loss: Categorical Crossentropy

Metrics: Accuracy

📜 License
This project is licensed under the MIT License. See LICENSE file for details.

🙋‍♂️ Contact
For queries or collaborations, reach out at:rawataditi120@gmail.com
