# Rivals of Aether 2 VODs

This is a simple website for collecting and searching Rivals of Aether 2 VODs.

## Developer instructions

These are instructions for running the site locally.

### Set up your developer environment

These instructions support Windows (PowerShell) and Unix.

You only need to do this once.

1. [Install Python 3.10+](https://www.python.org/downloads/).
2. Clone the repository:

    ```sh
    git clone https://github.com/akbiggs/vods2
    ```

3. Enter the directory.

   ```sh
   cd vods2
   ```

4. Create a virtual environment in the project directory:

    ```sh
    python3 -m venv .venv
    ```

5. Activate your virtual environment. On Windows (PowerShell):

   ```sh
   .venv\Scripts\activate.ps1
   ```

   On Unix:

   ```sh
   .venv/bin/activate
   ```

6. Install dependencies.

   ```sh
   python3 -m pip install click==8.1.7 flask==3.1.0
   ```

7. Initialize the database. Type "confirm" when the script asks you to.

   ```sh
   python3 -m flask init-db
   ```

8. Import the VODs.

   ```sh
   python3 -m flask ingest-csv data/vods.csv
   ```

### Running the site locally

To see your changes locally:

1. Activate your virtual environment. On Windows (PowerShell):

   ```sh
   .venv\Scripts\activate.ps1
   ```

   On Unix:

   ```sh
   .venv/bin/activate
   ```

2. Run the site in dev mode. This allows you to refresh and see your changes.

   ```
   python3 -m flask run --dev
   ```

3. Go to http://localhost:5000 to see the site.

### Adding VODs

TODO