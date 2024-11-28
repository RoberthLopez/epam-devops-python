import pytest
from src.dictionary import Dictionary

@pytest.fixture
def dictionary():
    return Dictionary()

def test_newentry_valid(dictionary):
    dictionary.newentry("Apple", "A fruit that grows on trees")
    assert dictionary.look("Apple") == "A fruit that grows on trees"
    
def test_newentry_valid(dictionary):
    dictionary.newentry("apple", "A fruit that grows on trees")
    assert dictionary.look("apple") == "A fruit that grows on trees"

def test_newentry_invalid(dictionary):
    dictionary.newentry(1, "A number")
    assert dictionary.look(1) == "Can't find entry for 1"

def test_look_nonexistent(dictionary):
    assert dictionary.look("banana") == "Can't find entry for banana"
