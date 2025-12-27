import pytest
from analyzer import Analyzer

def test_extract_words():
    analyzer = Analyzer()
    text = "Hello, world! Hello Python."
    words = analyzer.extract_words(text)

    assert words == ["hello", "world", "hello", "python"]

def test_common_words():
    analyzer = Analyzer()
    analyzer.words = ["hello", "world", "hello"]

    result = analyzer.common_words()

    assert result == {
        "hello": 2,
        "world": 1
    }

def test_average_word_length():
    analyzer = Analyzer()
    analyzer.words = ["hi", "hello"]

    assert analyzer.average_word_length() == 3.5

def test_average_word_length_empty():
    analyzer = Analyzer()
    analyzer.words = []

    assert analyzer.average_word_length() == 0
