import number_in_wordt
import pytest


def test_hundred():
    assert number_in_wordt.hundred(100) == "one Hundred  "
    assert number_in_wordt.hundred(253) == "two Hundred fifty three"


def test_thousand():
    assert number_in_wordt.thousand(1000) == "one Thousand"
    assert number_in_wordt.thousand(26000) == "twenty six Thousand"
    assert type(number_in_wordt.thousand(1000)) == str


def test_lakh():
    assert type(number_in_wordt.lakh(200000)) == str
    assert number_in_wordt.lakh(200000) == "two Lakh"
    assert number_in_wordt.lakh(3300000) == "thirty three Lakh"


def test_crore():
    assert number_in_wordt.crore(20000000) == "two Crore"
    assert number_in_wordt.crore(330000000) == "thirty three Crore"



