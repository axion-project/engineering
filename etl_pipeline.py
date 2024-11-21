import pandas as pd
from sqlalchemy import create_engine

# Database connection configuration
DB_CONFIG = {
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost',
    'port': 5432,
    'database': 'ecommerce'
}

def create_connection():
    """Create a connection to the PostgreSQL database."""
    connection_string = f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
    engine = create_engine(connection_string)
    return engine

def load_csv_to_df(file_path):
    """Load CSV data into a Pandas DataFrame."""
    return pd.read_csv(file_path)

def transform_data(df, table_name):
    """Perform any data transformations (if needed)."""
    print(f"Transforming data for table: {table_name}")
    return df  # No transformations for now

def load_data_to_postgres(df, table_name, engine):
    """Load DataFrame data into PostgreSQL."""
    try:
        df.to_sql(table_name, con=engine, if_exists='replace', index=False)
        print(f"Successfully loaded data into table: {table_name}")
    except Exception as e:
        print(f"Error loading data into table {table_name}: {e}")

def main():
    # File paths
    files = {
        'sales': '../data/sales.csv',
        'products': '../data/products.csv',
        'customers': '../data/customers.csv',
        'time': '../data/time.csv'
    }
    
    # Create database connection
    engine = create_connection()
    
    # ETL process
    for table_name, file_path in files.items():
        print(f"Processing {table_name} data...")
        df = load_csv_to_df(file_path)  # Extract
        transformed_df = transform_data(df, table_name)  # Transform
        load_data_to_postgres(transformed_df, table_name, engine)  # Load

if __name__ == "__main__":
    main()
