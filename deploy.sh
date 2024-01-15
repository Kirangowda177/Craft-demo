#!/bin/bash

# Install required dependencies
pip install Flask

# Create local k8s cluster (assuming you have 'kind' installed)
kind create cluster --name local-cluster

# Build Docker image
docker build -t country-lookup-service .

# Load Docker image into the local cluster
kind load docker-image country-lookup-service --name local-cluster

# Apply Kubernetes deployment
kubectl apply -f k8s/deployment.yaml

# Wait for the service to be available
sleep 10

# Port forward to access the service
kubectl port-forward service/country-lookup-service 5000:5000