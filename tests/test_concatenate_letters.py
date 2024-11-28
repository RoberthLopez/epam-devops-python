import pytest
from app.concatenate_letters import concatenate_letters

def test_valid_input():
    result = concatenate_letters(["yoda", "best", "has"])
    assert result == "yes"

def test_empty_input():
    result = concatenate_letters([])
    assert result == ""
