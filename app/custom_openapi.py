from fastapi.openapi.utils import get_openapi

def custom_openapi(app):
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="Number Classification API",
        description="This is a FastAPI-based project that provides an API endpoint to classify numbers based on their mathematical properties. The API checks if a number is prime, perfect, even, odd, or an Armstrong number, and also provides additional information like the digit sum and a fun fact about the number",
        version="1.0.0",
        routes=app.routes
    )

    
    openapi_schema["components"]["schemas"]["SuccessResponse"] = {
        "title": "SuccessResponse",
        "type": "object",
        "properties": {
            "number": {"type": "integer"},
            "is_prime": {"type": "boolean"},
            "is_perfect": {"type": "boolean"},
            "properties": {
                "type": "array",
                "items": {"type": "string"}  # Assuming the list contains strings
            },
            "digit_sum": {"type": "integer"},
            "fun_fact": {"type": "string"}
        }
    }

    del openapi_schema["components"]["schemas"]["ValidationError"]
    del openapi_schema["components"]["schemas"]["HTTPValidationError"] 
    
    openapi_schema["paths"]["/classify-number/"]["get"]["responses"].pop("422", None)

    app.openapi_schema = openapi_schema
    return app.openapi_schema
