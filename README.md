\# Airflow ETL Pipeline Project



\## Project Overview

This project demonstrates a simple \*\*Data Engineering ETL pipeline\*\* using Apache Airflow, Docker, and PostgreSQL.



The pipeline extracts user data from a public API, transforms it, and loads it into a PostgreSQL database.



\---



\## Tech Stack



\- Apache Airflow

\- Docker \& Docker Compose

\- Python

\- PostgreSQL

\- REST API

\- Pandas



\---



\## Project Architecture



API → Airflow DAG → Data Lake → Transformation → PostgreSQL Database



\---



\## Workflow



1\. \*\*Extract\*\*

&#x20;  - Fetch user data from Random User API



2\. \*\*Store Raw Data\*\*

&#x20;  - Save raw JSON data into the data lake



3\. \*\*Transform\*\*

&#x20;  - Process JSON data and extract required fields



4\. \*\*Load\*\*

&#x20;  - Insert transformed data into PostgreSQL database



\---



\## Project Structure

airflow-etl-pipeline

│

├── dags

│ └── etl\_pipeline.py

│

├── scripts

│ ├── api\_extract.py

│ └── spark\_etl.py

│

├── data\_lake

│ └── raw\_user.json

│

├── docker-compose.yaml

├── README.md

└── .gitignore





\---



\## DAG Tasks



\### extract\_api

Extracts data from the API and stores it in the data lake.



\### transform\_data

Transforms the raw JSON data and loads it into PostgreSQL.



\---



\## How to Run



Start the containers:

docker compose up -d



Open Airflow UI:



http://localhost:8080



Login:

username: airflow

password: airflow





Trigger the DAG:



etl\_pipeline





\---



\## Future Improvements



\- Add AWS S3 as data lake

\- Use Spark for transformation

\- Store processed data in AWS RDS

\- Add monitoring and logging



\---



\## Author



Nikitabuva

