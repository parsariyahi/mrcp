from mrcp import Encoder


def test_encode_string_to_morse_code():
    string = "hello world"
    string_morse_code = "0000.0.0100.0100.111/011.111.010.0100.100"
    encoder = Encoder()
    encoded = encoder.encode(string)

    assert encoded == string_morse_code