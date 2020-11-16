from cipher_jp4100 import __version__
from cipher_jp4100 import cipher_jp4100
import pytest

def test_version():
    assert __version__ == '0.1.0'
    
def test_cipher_1():
    text = 'test'
    shift = 3
    new_text = 'whvw'
    result = cipher(text, shift)
    assert result == new_text
