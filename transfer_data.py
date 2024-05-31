import os
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# PostgreSQL database credentials
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
POSTGRES_DB = os.getenv('POSTGRES_DB')

# Check if environment variables are loaded
if not all([POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST, POSTGRES_PORT, POSTGRES_DB]):
    raise EnvironmentError("Some PostgreSQL environment variables are missing. Check your .env file.")

# PostgreSQL database URL
db_url = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'

# Create an engine
engine = create_engine(db_url)

# Path to your pickle files directory
pickle_directory = 'D:\\COGNOS X\\RESEARH PROJECT\\africa_research\\data'  # Change this to your actual directory path

# List all pickle files in the directory
pickle_files = [os.path.join(pickle_directory, file) for file in os.listdir(pickle_directory) if file.endswith('.pkl')]

# Load each pickle file and append it to a list
dataframes = []
for file in pickle_files:
    try:
        df = pd.read_pickle(file)
        dataframes.append(df)
    except Exception as e:
        print(f"Error loading {file}: {e}")

# Concatenate all dataframes into one, handling different columns
if dataframes:
    all_data = pd.concat(dataframes, ignore_index=True, sort=False).fillna('')
else:
    raise ValueError("No dataframes loaded. Please check your pickle files.")

# Save the concatenated data to a CSV file
csv_file_path = 'D:\\COGNOS X\\RESEARH PROJECT\\africa_research\\all_data_concat.csv'
all_data.to_csv(csv_file_path, index=False)
print(f"All data concatenated and saved to {csv_file_path}")

# Extract columns for table creation
columns = all_data.columns

# SQL to create table with dynamic columns
create_table_sql = f"""
CREATE TABLE IF NOT EXISTS african_research (
    {', '.join([f'"{col}" TEXT' for col in columns])}
);
"""

# Execute table creation
try:
    with engine.connect() as conn:
        conn.execute(text(create_table_sql))
    print("Table 'african_research' created successfully.")
except Exception as e:
    print(f"Error creating table: {e}")

# Save the concatenated data to PostgreSQL
try:
    all_data.to_sql('african_research', engine, if_exists='replace', index=False)
    print("All data processed and saved successfully to the PostgreSQL database.")
except Exception as e:
    print(f"Error saving data to PostgreSQL: {e}")
