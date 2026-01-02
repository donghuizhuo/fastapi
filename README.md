# fastapi

A simple FastAPI application with async endpoints.

## Setup

1. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Starting the Server

Run the development server with auto-reload:
```bash
python server.py
```

The server will start at `http://127.0.0.1:8000`

## Testing the Server

### Using curl

Test the root endpoint:
```bash
curl http://127.0.0.1:8000/
```

Expected response:
```json
{"Hello":"World"}
```

Test the slow data endpoint:
```bash
curl http://127.0.0.1:8000/slow-data
```

Expected response (after 2 second delay):
```json
{"message":"Slow data loaded"}
```

### Using httpx (Python)

```python
import httpx

# Test root endpoint
response = httpx.get("http://127.0.0.1:8000/")
print(response.json())

# Test slow-data endpoint
response = httpx.get("http://127.0.0.1:8000/slow-data")
print(response.json())
```

### Using Browser

Visit the auto-generated interactive API documentation:
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Available Endpoints

- `GET /` - Returns a simple hello world message
- `GET /slow-data` - Returns data after a 2-second simulated delay
