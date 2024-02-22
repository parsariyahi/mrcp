from typing import List, Dict, Optional

from .maps import TO_MORSE_MAPPER
from .settings import WORD_DELIMITER, MORSE_WORD_DELIMITER, CHAR_DELIMITER


class Encoder:
    def __init__(self, mapper: Optional[Dict[str, str]] = None, word_delimiter: Optional[str] = None, morse_word_delimiter: Optional[str] = None, char_delimiter: Optional[str] = None) -> None:
        """``Morse code`` Encoder, This class uses ``Morsep`` style for decoding the ``Morse code`` codes.

        Parameters
        ----------
        mapper : Dict[str: str], optional
            ``mapper`` is the main ``to_morse`` mapper, we use ``morsep._translator.maps.TO_MORSE_MAPPER`` if you set it to ``None``, by default ``None``
        word_delimiter : Optional[str], optional
            ``word_delimiter`` is the seperator for each word in our decoder, we use ``morsep._translator.settings.WORD_DELIMITER`` if you set  it to ``None``, by default ``None``
        char_delimiter : Optional[str], optional
            ``char_delimiter`` is the seperator for each char in our decoder, we use ``morsep._translator.settings.CHAR_DELIMITER`` if you set  it to ``None``, by default ``None``
        """
        self.mapper = mapper if mapper else TO_MORSE_MAPPER
        self.word_delimiter = word_delimiter if word_delimiter else WORD_DELIMITER
        self.morse_word_delimiter = morse_word_delimiter if morse_word_delimiter else MORSE_WORD_DELIMITER
        self.char_delimiter = char_delimiter if char_delimiter else CHAR_DELIMITER

    def encode(self, text: str):
        encoded = []
        words = self._normilize_words(text)
        for word in words:
            word_encoded = []
            for char in word:
                mapped = self.mapper.get(char, None)
                if mapped:
                    word_encoded.append(mapped)
            word_encoded = f"{self.char_delimiter}".join(word_encoded)
            encoded.append(word_encoded)

        return f"{self.morse_word_delimiter}".join(encoded)

    def _normilize_words(self, text: str) -> List[str]:
        return text.split(self.word_delimiter)