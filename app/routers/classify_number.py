from fastapi import APIRouter, Response
from ..dependencies import validate_number_query, get_numbers_fact, is_perfect_number, is_prime_number, is_armstrong
from pydantic import BaseModel
import json


class CustomValidationError(BaseModel):
    number: str
    error: bool


class SuccessResponse(BaseModel):
    number: int
    is_prime: bool
    is_perfect: bool
    properties: list
    digit_sum: int
    fun_fact: str


router = APIRouter()

@router.get("/api/classify-number", tags=["classify-number"], response_model=SuccessResponse, responses={400:{"model": CustomValidationError, "description": "Bad Request"}} )
async def classify_number(number:str = None):

    #using str and not int due to hng requirement for custom validation 
    validated_result = validate_number_query(number)

    if isinstance(validated_result, Response):
        return validated_result

    validated_number = validated_result
    
    return {"validated": True, "number": validated_number"}

    is_armstrong_num = is_armstrong(validated_number)
    is_even_parity = validated_number % 2 == 0
    
    properties = []
    if is_armstrong_num:
        properties.insert(0, "armstrong")
    properties.append("even" if is_even_parity else "odd")
    
    digit_is_negative = number.startswith('-')
    digit_sum = sum(int(i) for i in number.lstrip('-'))  
    if digit_is_negative:  
        digit_sum = -digit_sum
        

    fun_fact = await get_numbers_fact(validated_number)
    is_perfect = is_perfect_number(validated_number)
    is_prime = is_prime_number(validated_number)

    return Response(
        content=json.dumps({
            "number": validated_number,
            "is_prime": is_prime,
            "is_perfect": is_perfect,
            "properties": properties,
            "digit_sum": digit_sum,
            "fun_fact": fun_fact
        }),
            status_code=200,
            media_type="application/json"
        )


