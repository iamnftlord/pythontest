import pytest
from kiosk_billing import calculate_subtotal, apply_discount

def test_calculate_subtotal_success():
    result = calculate_subtotal(4.5, 3)
    assert result == 13.5

def test_calculate_subtotal_negative__raise_error():
        with pytest.raises(ValueError):
            calculate_subtotal(-4.50, 3)

def test_apply_discount():
    result = apply_discount(10.00, 0.10)
    assert result == 9.00
    