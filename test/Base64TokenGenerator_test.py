import pytest
import Base64TokenGenerator


def test_encoding_base_64():
    encode = Base64TokenGenerator.simple_encoding("test")
    assert encode == "dGVzdA=="  # add assertion here


def test_decoding_base_64():
    decode = Base64TokenGenerator.base64_decode("dGVzdA==")
    assert decode == "test"


def test_create_basic_auth():
    auth = Base64TokenGenerator.create_basic_auth("testUser@testmail.com", "testPassword")
    assert auth == "dGVzdFVzZXJAdGVzdG1haWwuY29tOnRlc3RQYXNzd29yZA=="

# def test_options_selection(self):
#    selection = Base64TokenGenerator()
#    option = selection.select_action()
