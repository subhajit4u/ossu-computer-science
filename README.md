Product Explorer & Error-Resilient Logger

This project demonstrates Python file handling, API integration, exception handling, and logging.

The program interacts with the public DummyJSON API and performs multiple operations including reading/writing files, handling errors, and logging system events.

Tasks Implemented

Task 1 – File Read & Write
The program creates a file called `python_notes.txt` containing Python learning notes.

Operations performed:
- Write 5 lines to the file
- Append 2 additional lines
- Read and display the file contents
- Display numbered lines
- Count the total number of lines
- Search for a keyword inside the file

Task 2 – API Integration
The program connects to the DummyJSON public API.

Operations performed:
- Fetch 20 products using a GET request
- Display product information in table format
- Filter products with rating ≥ 4.5
- Sort filtered products by price (descending)
- Retrieve products from the **laptops** category
- Send a simulated POST request to create a product

Task 3 – Exception Handling
The program demonstrates safe error handling using try-except blocks.

Examples included:
- `safe_divide()` handles ZeroDivisionError and TypeError
- `read_file_safe()` handles FileNotFoundError
- API requests handle ConnectionError and Timeout

Task 4 – Error Logging
Errors are logged to a file called `error_log.txt`.

Each log entry contains:
- Timestamp
- Function name
- Error message

Example log entry:

[2026-04-0 212:30:01] ERROR in fetch_products: ConnectionError

Files Generated

After running the program the following files will be created:

- `python_notes.txt` – contains Python learning notes
- `error_log.txt` – contains logged error messages

Requirements

Install the requests library before running the program:

pip install requests

How to Run

Run the script using Python:

python part3_api_files.py