import pytest

def cipher(text, shift, encrypt=True):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            assert isinstance(shift, int), f"shift must be an integer"
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text


def test_cipher_1():
    text = 'test'
    shift = 3
    new_text = 'whvw'
    result = cipher(text, shift)
    assert result == new_text



def test_cipher_2():
    text = 'test'
    shift = -2
    new_text = 'rcqr'
    result = cipher(text, shift)
    assert result == new_text




def test_cipher_3():
    text = 'test8'
    shift = -2
    new_text = 'rcqr8'
    result = cipher(text, shift)
    assert result == new_text




def test_cipher_4():
    text = 'test'
    with pytest.raises(AssertionError):
        shift = 'two'
        new_text = 'vguv'    
        result = cipher(text, shift)
        assert result == new_text

test_cipher_4()