from typing import List, Dict, Optional

from .maps import FROM_MORSE_MAPPER
from .settings import WORD_DELIMITER, MORSE_WORD_DELIMITER, CHAR_DELIMITER


class Decoder:
    def __init__(self, mapper: Optional[Dict[str, str]] = None, word_delimiter: Optional[str] = None, morse_word_delimiter: Optional[str] = None, char_delimiter: Optional[str] = None) -> None:
        """``Morse code`` Decoder, This class uses ``mrcp`` style for decoding the ``Morse code`` codes.

        Parameters
        ----------
        mapper : Dict[str: str], optional
            ``mapper`` is the main ``to_morse`` mapper, we use ``mrcp._translator.maps.FROM_MORSE_MAPPER`` if you set it to ``None``, by default ``None``
        word_delimiter : Optional[str], optional
            ``word_delimiter`` is the seperator for each word in our decoder, we use ``mrcp._translator.settings.WORD_DELIMITER`` if you set  it to ``None``, by default ``None``
        char_delimiter : Optional[str], optional
            ``char_delimiter`` is the seperator for each char in our decoder, we use ``mrcp._translator.settings.CHAR_DELIMITER`` if you set  it to ``None``, by default ``None``
        """
        self.mapper = mapper if mapper else FROM_MORSE_MAPPER
        self.word_delimiter = word_delimiter if word_delimiter else WORD_DELIMITER
        self.morse_word_delimiter = morse_word_delimiter if morse_word_delimiter else MORSE_WORD_DELIMITER
        self.char_delimiter = char_delimiter if char_delimiter else CHAR_DELIMITER

    def decode(self, code: str) -> str:
        """decode the ``Morse code`` with the given ``mapper``, by default it will use the ``mrcp._translator.maps.FROM_MORSE_MAPPER``.

        Parameters
        ----------
        code : str
            ``Morse code`` that you want to decode it

        Returns
        -------
        str
            decoded ``Morse code`` that you gave
        """
        decoded = []
        words = self._normalize_words(code)

        for word in words:
            word_decoded = []
            word_norm = self._normilize_chars(word)
            for char in word_norm:
                mapped = self.mapper.get(char, None)
                if mapped:
                    word_decoded.append(mapped)

            decoded.append("".join(word_decoded))

        return f"{self.word_delimiter}".join(decoded)

    def _normalize_words(self, code: str) -> List[str]:
        """normilize the words inside the ``Morse code`` with the given ``word_delimiper``, by default it will use the ``mrcp._translator.settings.WORD_DELIMITER``.

        Parameters
        ----------
        code : str
            ``Morse code`` that need to be normilize

        Returns
        -------
        List[str]
            seperated words inside a list of strings
        """
        return code.split(self.morse_word_delimiter)

    def _normilize_chars(self, word: str) -> List[str]:
        return word.split(self.char_delimiter)