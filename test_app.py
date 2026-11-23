
from app import process_payment


def test_valid_payment():
    result = process_payment(100)
    assert result == "Payment successful: $200.00"


def test_zero_payment():
    result = process_payment(0)
    assert result == "Payment failed"


def test_negative_payment():
    result = process_payment(-50)
    assert result == "Payment failed"
