import pytest
from src.calculate_price import get_total

@pytest.fixture
def costs():
    return {'socks': 5, 'shoes': 60, 'sweater': 30}

def test_get_total_valid(costs):
    result = get_total(costs, ['socks', 'shoes'], 0.09)
    assert result == 70.85

def test_invalid_item_list(costs):
    result = get_total(costs, "socks, shoes", 0.09)
    assert result == 'Second param should be a list'

def test_invalid_tax(costs):
    result = get_total(costs, ['socks', 'shoes'], "0.09")
    assert result == 'Third param should be a float'
