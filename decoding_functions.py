def decode_language(data, from_lang):
    from deep_translator import GoogleTranslator
    from deep_translator.exceptions import LanguageNotSupportedException, InvalidSourceOrTargetLanguage
    try:
        translation = GoogleTranslator(source=from_lang, target="en").translate(data)
        return translation
    except LanguageNotSupportedException:
        return f"The language chosen is not right"
    except InvalidSourceOrTargetLanguage:
        return f"Invalid source language"


def decode_binary(data, decoding_technique='utf-8'):
    encoded_data = data.split()
    for index, values in enumerate(encoded_data):
        int_val = int(values, 2)  # that 2 represents binary data type and converts them to decimal
        if len(values) > 8:
            # checking if greater than 8 bits
            int_val = int_val & 0xFF
        encoded_data[index] = int_val
        # encoded_data is now a list of integers to become bytes
    try:
        hex_data = bytes(encoded_data)
        decoded_data = hex_data.decode(decoding_technique)
        return decoded_data
    except UnicodeDecodeError:
        return "Please choose a valid decoding technique"
    except ValueError:
        return f"Invalid bits to decode"


def decode_morse_code(data):
    from morse3 import Morse
    encoded_data = Morse(data).morseToString()
    return encoded_data.strip().capitalize()



def decode_enc(data) -> str:
    import base64
    import binascii
    split_data = data.split()
    try:
        encoded_part = split_data[-1]
        encoded_value = base64.b64decode(encoded_part)
        decoded_value = encoded_value.decode()
        return decoded_value
    except binascii.Error:
        return "Please enter a **valid** base64 code"



def decode_hex(data, decoding_technique="utf-8"):
    try:
        bytes_data = bytes.fromhex(data.replace("0x", ""))
        value = bytes_data.decode(decoding_technique)
        return value
    except UnicodeDecodeError:
        return f"Please choose a valid decoding technique"

def print_image(path="Files/evidence/photo/photo.bmp"):
    import climage
    output = climage.convert(path, width=40)
    print(output)

if __name__ == "__main__":
    print_image()
