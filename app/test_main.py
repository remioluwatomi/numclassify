from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_classify_number_with_valid_query():
    response = client.get("/classify-number?number=4")
    assert response.status_code == 200

    data = response.json()
    assert "number" in data
    assert "is_prime" in data
    assert "is_perfect" in data
    assert "properties" in data
    assert "digit_sum" in data
    assert "fun_fact" in data


def test_classify_number_with_no_query():
    response = client.get("/classify-number")

    assert response.status_code == 400
    data = response.json()

    assert data == {
                "number": "missing",
                "error": True
            }


def test_classify_number_with_invalid_query():
    response = client.get("/classify-number?number=abc")

    assert response.status_code == 400
    data = response.json()

    assert data == {
                "number": "alphabet",
                "error": True
            }


def test_classify_number_is_armstrong():
    response = client.get("classify-number?number=371")

    assert response.status_code == 200

    data = response.json()
    assert data["properties"][0] == "armstrong"


def test_classify_number_is_even():
    response = client.get("classify-number?number=10")
    
    assert response.status_code == 200

    data = response.json()
    assert data["properties"][0] == "even"


def test_classify_number_is_odd():
    response = client.get("classify-number?number=13")
    
    assert response.status_code == 200

    data = response.json()
    assert data["properties"][0] == "odd"


def test_classify_number_is_prime():
    response = client.get("classify-number?number=7")
    
    assert response.status_code == 200

    data = response.json()
    assert data["is_prime"]


def test_classify_number_is_perfect():
    response = client.get("classify-number?number=6")
    
    assert response.status_code == 200

    data = response.json()
    assert data["is_perfect"]


def test_classify_number_fun_fact():
    response = client.get("/classify-number?number=42")
    assert response.status_code == 200

    data = response.json()
    assert "fun_fact" in data
    assert isinstance(data["fun_fact"], str)
    assert len(data["fun_fact"]) > 0


def test_classify_number_digit_sum():
    response = client.get("/classify-number?number=123")
    assert response.status_code == 200

    data = response.json()
    assert "digit_sum" in data
    assert data["digit_sum"] == 6 