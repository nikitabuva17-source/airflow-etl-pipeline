# Airflow ETL Pipeline (API → Data Lake → PostgreSQL)

## 📌 Project Overview

This project demonstrates an **end-to-end ETL pipeline using Apache Airflow, Docker, and PostgreSQL**.

The pipeline extracts user data from a public API, stores the raw data in a data lake (JSON), transforms the data using Python, and loads the processed data into a PostgreSQL database.

Apache Airflow orchestrates the workflow using DAGs, ensuring the pipeline runs in a structured and automated way.

---

## 🛠️ Technologies Used

* Apache Airflow
* Docker & Docker Compose
* Python
* PostgreSQL
* REST API
* Pandas

---

## 🏗️ Architecture

```
Random User API
        │
        ▼
Apache Airflow DAG
        │
        ▼
Data Extraction Script
(api_extract.py)
        │
        ▼
Data Lake (JSON File)
raw_user.json
        │
        ▼
Data Transformation Script
(spark_etl.py)
        │
        ▼
PostgreSQL Database
users_data Table
```

---

## 🔄 ETL Workflow

1️⃣ Extract
Fetch user data from the **Random User API**.

2️⃣ Store Raw Data
Save the raw JSON data into the **data_lake folder**.

3️⃣ Transform
Process the JSON data and extract relevant user fields.

4️⃣ Load
Insert the processed data into the **PostgreSQL database table**.

---

## 📊 Airflow DAG Tasks

### extract_api

Extracts data from the API and stores raw JSON data in the data lake.

### transform_data

Transforms the raw data and loads it into PostgreSQL.

---

## 📁 Project Structure

```
airflow-etl-pipeline
│
├── dags
│   └── etl_pipeline.py
│
├── scripts
│   ├── api_extract.py
│   └── spark_etl.py
│
├── data_lake
│   └── raw_user.json
│
├── docker-compose.yaml
├── README.md
└── .gitignore
```

---

## ▶️ How to Run the Project

Start Docker containers:

```
docker compose up -d
```

Open Airflow UI:

```
http://localhost:8080
```

Login credentials:

```
username: airflow
password: airflow
```

Trigger the DAG:

```
etl_pipeline
```

---

## 📈 Future Improvements

* Integrate AWS S3 as the data lake
* Use Apache Spark for large-scale transformations
* Store processed data in AWS RDS
* Add monitoring and alerting

---

## 👩‍💻 Author

**Nikita Buva**

Data Engineering Project using Apache Airflow
