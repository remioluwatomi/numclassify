from typing import Annotated

from fastapi import Header, status
from fastapi.responses import JSONResponse
import asyncio
import httpx
import math
import json

NUMBERS_API_URL="http://numbersapi.com"

async def get_numbers_fact(number:int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{NUMBERS_API_URL}/{number}/math")
        return response.text


def is_perfect_number(number: int) -> bool:
    if number <= 0:
        return False 

    divisors_sum = sum(i for i in range(1, number // 2 + 1) if number % i == 0)

    return divisors_sum == number


def is_prime_number(number: int) -> bool:
    if number <= 1:
        return False 
    if number == 2:
        return True 
    if number % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False 

    return True 


def is_armstrong(number: int) -> bool:
    num_str = str(number)
    power = len(num_str)
    
    digit_sum = sum(int(digit) ** power for digit in num_str)
    
    return digit_sum == number


def validate_number_query(number:str):
    if not number:
        return JSONResponse(
            content= {
                "number": "missing",
                "error": True
            },
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    if not number.lstrip("-").isdigit():
        return JSONResponse(
            content= {
                "number": "alphabet",
                "error": True
            },
            status_code=status.HTTP_400_BAD_REQUEST,
        )
    
    number = int(number)
    if number < 0:
        return JSONResponse(
            content= {
                "number": "negative",
                "error": True
            },
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    return number

