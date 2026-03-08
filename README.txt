# Math Series API

A FastAPI-based project to generate mathematical series (Fibonacci, arithmetic, and more), with CSV output.

## Features

- Generate Fibonacci series as CSV (using query parameters)
- Generate arithmetic series as CSV (using query parameters)
- Modular code structure for easy extension

## Installation

Clone the repository and set up your Python virtual environment:

```bash
git clone https://github.com/theyaguito/psyapi.git
cd psyapi
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

### 1. Run the API

```bash
uvicorn api:app --reload
```

### 2. Endpoints and Examples

#### Fibonacci Series

Get the first N Fibonacci numbers as CSV (**using query parameter**):

`http://127.0.0.1:8000/fibonacci_csv?n=10`

Example:

```bash
curl "http://127.0.0.1:8000/fibonacci_csv?n=10"
```

#### Arithmetic Series

Generate an arithmetic series as CSV (**using query parameters**):

`http://127.0.0.1:8000/arithmetic_csv?n=10&start=3&diff=5`

Example:

```bash
curl "http://127.0.0.1:8000/arithmetic_csv?n=10&start=3&diff=5"
```

## Extending

You can add new mathematical series by creating a subclass of `Series` in `series.py` and registering a new endpoint in 'api.py'.

## License

MIT License

## Author

Santiago Cano Acosta  
Universidad Nacional de Colombia, Medellín
