# Airflow Lab 1 - K-Means Clustering DAG Pipeline

## Overview
This lab sets up an Apache Airflow DAG pipeline using Docker Compose to perform K-Means clustering on credit card customer data.

## Modifications from Original Lab
- Fixed PythonOperator import for Airflow 2.5.1 compatibility (from airflow.operators.python instead of airflow.providers.standard.operators.python)
- Updated docker-compose.yaml: disabled example DAGs, added pip packages (pandas, scikit-learn, kneed), mounted working_data volume, changed credentials to airflow2/airflow2
- Used base64-encoded XCom serialization for JSON-safe data passing between tasks

## DAG Pipeline Tasks
1. load_data_task - Loads credit card data from CSV, serializes to base64
2. data_preprocessing_task - Drops nulls, selects BALANCE/PURCHASES/CREDIT_LIMIT, applies MinMaxScaler
3. build_save_model_task - Fits KMeans for k=1-49, saves model, returns SSE values
4. load_model_task - Uses elbow method (KneeLocator) to find optimal k, predicts on test data

## Steps to Re-run

### Prerequisites
- Docker Desktop installed and running (at least 4GB memory)

### Setup and Run
mkdir -p ~/app && cd ~/app
curl -LfO https://airflow.apache.org/docs/apache-airflow/2.5.1/docker-compose.yaml
mkdir -p ./dags ./logs ./plugins ./working_data
echo -e "AIRFLOW_UID=$(id -u)" > .env
cp -r <path-to-this-folder>/dags/* ~/app/dags/
docker compose up airflow-init
docker compose up

### Access Airflow UI
- Go to http://localhost:8080
- Login: airflow2 / airflow2
- Unpause Airflow_Lab1 DAG and trigger it
- All 4 tasks should complete green

### Stop
docker compose down

## File Structure
Lab_1_modified/
  README.md
  docker-compose.yaml
  .env
  dags/
    airflow.py
    data/file.csv, test.csv
    src/__init__.py, lab.py
