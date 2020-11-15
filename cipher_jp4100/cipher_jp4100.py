def cipher(text, shift, encrypt=True):
    """
    This is a function to encipher or decipher code and is called caesar cipher.
    
    Input
    ---------
    text: str
           A string that you want to encrypt or decrypt. 
    shift: int
           An integer which infers positions you want to change the text from the original format. It can be both positive and negative. Positive shift means shift forward, while negative one means shift backward.
    encrypt: bool
           A boolean value which will encipher the text if it is True, otherwise, it will decipher the text. The default value is True.
    
    Output
    ---------
    str
           The new text after enciphering or deciphering.
    
    Examples:
    >>> from cipher_jp4100 import cipher_jp4100
    >>> cipher_jp4100.cipher(text='abc', shift=3, encrypt=True)
          'def'
    >>> cipher_jp4100.cipher(text='abc', shift=3, encrypt=False)
          'XYZ'
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text