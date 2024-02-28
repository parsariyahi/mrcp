from mrcp import Decoder


def test_decode_morse_code_to_string():
    morse_code = "0000.0.0100.0100.111/011.111.010.0100.100"
    morse_code_string = "hello world"
    decoder = Decoder()
    decoded = decoder.decode(morse_code)

    assert decoded == morse_code_string