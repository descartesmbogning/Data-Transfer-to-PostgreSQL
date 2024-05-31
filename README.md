# Data Transfer to PostgreSQL

This project provides a script (`transfer_data.py`) to load multiple pickle files from a directory, concatenate their data, and save the combined data to a PostgreSQL database. The script also ensures the data is saved in a CSV file before uploading it to the database.

## Features
- Load data from multiple pickle files.
- Concatenate data into a single DataFrame.
- Save concatenated data to a CSV file.
- Create a PostgreSQL table dynamically based on DataFrame columns.
- Upload data to the PostgreSQL table.

## Prerequisites
- Python 3.x
- PostgreSQL
- Required Python packages (specified in `requirements.txt`)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up your `.env` file with PostgreSQL credentials:
    ```plaintext
    POSTGRES_USER=your_username
    POSTGRES_PASSWORD=your_password
    POSTGRES_HOST=localhost
    POSTGRES_PORT=5432
    POSTGRES_DB=africa_research
    ```

## Usage

1. Place your pickle files in the specified directory:
    ```plaintext
    D:\COGNOS X\RESEARH PROJECT\africa_research\data
    ```

2. Run the `transfer_data.py` script:
    ```sh
    python transfer_data.py
    ```

3. The script will:
    - Load and concatenate data from all pickle files.
    - Save the concatenated data to `all_data_concat.csv`.
    - Create a PostgreSQL table named `african_research` if it does not exist.
    - Upload the data to the `african_research` table in the `africa_research` database.

## License
This project is licensed under the MIT License.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any changes.

## Contact
For any questions or feedback, please reach out to [dmbogning15@gmail.com](mailto:dmbogning15@gmail.com).

