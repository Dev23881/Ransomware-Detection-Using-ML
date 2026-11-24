# Deep Learning-Based Ransomware Detection Using Behavioral Features

## Project Overview
This project develops a machine learning-based ransomware detection system using behavioral features from the CIC-MalMem-2022 dataset. It classifies system behavior into **Benign** and **Ransomware** categories.

## Objectives
- Detect ransomware using behavioral data.
- Compare Machine Learning and Deep Learning models.
- Evaluate model performance using classification metrics.
- Develop an interactive dashboard for CSV-based predictions.

## Dataset
- **Dataset:** CIC-MalMem-2022
- **Selected classes:** Benign and Ransomware
- **Total records:** 38,760
- **Features:** 55 behavioral features

## Models Implemented
- Logistic Regression
- Random Forest Classifier
- Decision Tree Classifier
- Artificial Neural Network (ANN)

## Technologies Used
Python, Pandas, NumPy, Scikit-learn, TensorFlow/Keras, Matplotlib, Gradio, Google Colab

## Model Results
All four models achieved 100% accuracy on the initial test split. An additional ransomware-family holdout experiment was also conducted to evaluate generalization.

## Interactive Dashboard
A Gradio dashboard allows users to upload a CSV containing the required behavioral features and obtain Benign/Ransomware predictions.

## Project Limitations
This is an academic prototype based on dataset-derived behavioral features. It is not a live antivirus or real-time executable scanner.

## Team Members
- Ritesh — 1/23/SET/BCS/466
- Mansi — 1/23/SET/BCS/469
- Dev Setia — 1/23/SET/BCS/483

## Institution
Manav Rachna International Institute of Research and Studies (MRIIRS), Faridabad

---
**Project Type:** Applied Machine Learning PBL
