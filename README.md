# E-Commerce Data Warehouse

## Project Overview
This project demonstrates the design and implementation of a **data warehouse** for a fictional e-commerce platform. The data warehouse is built using **PostgreSQL**, with an **ETL pipeline** implemented in Python to process raw data from CSV files into structured tables. The purpose of this project is to showcase data engineering skills, focusing on organizing and transforming data for business intelligence and analytics.

---

## Features
- **End-to-End ETL Pipeline**: Extracts, transforms, and loads raw data into a PostgreSQL database.
- **Star Schema Design**: Optimized for efficient querying and reporting.
- **Modular and Scalable Code**: Easy to extend with additional datasets or transformations.
- **Sample Data Included**: Preloaded with realistic datasets for testing and demonstration.

---

## Project Structure

```plaintext
ecommerce_data_warehouse/
├── data/                # Sample datasets in CSV format
│   ├── sales.csv
│   ├── products.csv
│   ├── customers.csv
│   └── time.csv
├── scripts/             # Python scripts for the ETL pipeline
│   ├── etl_pipeline.py
├── README.md            # Project documentation
└── requirements.txt     # List of Python dependencies
