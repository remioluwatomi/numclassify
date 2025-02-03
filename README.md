# Number Classification API

This is a FastAPI-based project that provides an API endpoint to classify numbers based on their mathematical properties. The API checks if a number is prime, perfect, even, odd, or an Armstrong number, and also provides additional information like the digit sum and a fun fact about the number.

## Features

- **Number Classification**: Determine if a number is prime, perfect, even, odd, or an Armstrong number.
- **Digit Sum**: Calculate the sum of the digits of the number.
- **Fun Fact**: Get a fun fact about the number.
- **Error Handling**: Handle invalid inputs such as missing queries, non-numeric values, and negative numbers.

---

## Technologies Used

- **Python** proramming language.
- **FastAPI** for building the API.
- **fastapi.middleware.cors** for handling CORS.
- **Swagger** for api documentation.
- **Pytest** for testing the api

---

## Screenshots

![Screenshot of the Swagger API docs]()

![Screenshot of the Swagger API docs]()

---

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/remioluwatomi/numclassify.git

   cd numclassify

   ```

2. Create and Activate a Virtual Environment

   ```bash
    python -m venv venv

    # Activate virtual environment

    # Windows
    . venv\Scripts\activate

    # macOS/Linux
    source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt

   ```

4. Start the development server::

   ```bash
   uvicorn app.main:app --reload
   ```

   The API will be available at:

   ```bash
   http://127.0.0.1:8000/number-classify
   ```

   ```bash
   #docs
   http://127.0.0.1:8000/docs
   ```

---

## Endpoints

### `GET /classify-number?number={int}`

Accepts GET request with a number query and returns JSON response.

### Response:

- Success:

status_code: 200, OK

```json
{
  "number": 371,
  "is_prime": false,
  "is_perfect": false,
  "properties": ["armstrong", "odd"],
  "digit_sum": 11,
  "fun_fact": "371 is a narcissistic number."
}
```

- Error:

status_code: 400, BadRequest

```json
{ "number": "alphabet", "error": true }
```

---

## Disclaimer:

This project is my submssion to HNG task-1.

## License

This project is licensed under the **MIT License**.
