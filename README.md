# CloudWatch: Real-time Monitoring and Analysis

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Monitoring and Scaling](#monitoring-and-scaling)
- [Demo](#demo)

## Introduction

CloudResource Monitor & AutoScaler is an advanced cloud-native monitoring and auto-scaling application that offers real-time insights into CPU and memory utilization of cloud resources. This project utilizes Flask, Plotly, Docker, Kubernetes (Amazon EKS), and Amazon ECR to provide a comprehensive solution for visualizing and managing resource utilization in a cloud environment. The application allows users to monitor, analyze trends, and automate scaling based on defined thresholds.

## Features

- Real-time monitoring of CPU and memory utilization through interactive gauge meters.
- Dynamic alert system for displaying messages on high resource utilization.
- Trend analysis and visualization with interactive Plotly line charts.
- Automatic scaling of the application using Kubernetes Deployment and Service.
- Seamless integration with Amazon ECR for efficient container image storage and management.

## Technologies Used

- Python
- Flask
- Plotly
- Docker
- Kubernetes (Amazon EKS)
- Amazon ECR
- AWS SDK (boto3)

### Prerequisites

- Python 3.9 or higher
- Docker
- Kubernetes (kubectl) configured with Amazon EKS

### Usage
- Access the application by navigating to the URL provided by Amazon EKS.
- The application dashboard will display real-time CPU and memory utilization gauge meters.
- Monitor resource utilization trends through interactive Plotly line charts.
- Automatic scaling of resources will occur based on configured thresholds.

### Monitoring and Scaling

- The application provides detailed monitoring of CPU and memory utilization.
- Automatic scaling ensures optimal resource allocation based on predefined thresholds.
- High utilization triggers dynamic alerts for prompt attention and action.

### Demo

![image](https://github.com/rakshit-18/CloudWatch/assets/109340645/a4f8450d-4f38-4bf8-b370-9eeaafe782f3)

![image](https://github.com/rakshit-18/CloudWatch/assets/109340645/19eaae5e-a62d-43a5-b66a-78fd724f1f51)
![image](https://github.com/rakshit-18/CloudWatch/assets/109340645/ba8afa78-2342-4c9d-be60-4e2a1b35c1de)

![image](https://github.com/rakshit-18/CloudWatch/assets/109340645/bb3ae0c9-269e-4f35-bcd9-25c5cbfa5d7a)
![image](https://github.com/rakshit-18/CloudWatch/assets/109340645/eb28957d-acda-4261-9aca-4154cf1fb585)

