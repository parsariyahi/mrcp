from morsep import Encoder
from morsep import Decoder


def test_translator_functionality():
    text = "hello world"
    encoder = Encoder()
    decoder = Decoder()
    encoded = encoder.encode(text)
    decoded = decoder.decode(encoded)

    assert decoded == text