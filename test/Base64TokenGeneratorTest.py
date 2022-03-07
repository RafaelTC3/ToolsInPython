import unittest

# import pytest
import Base64TokenGenerator


class Base64TokenGeneratorTest(unittest.TestCase):
    def test_encoding_base_64(self):
        encode = Base64TokenGenerator.simple_encoding("test")
        self.assertEqual(encode, "dGVzdA==")  # add assertion here

    def test_decoding_base_64(self):
        decode = Base64TokenGenerator.base64_decode("dGVzdA==")
        self.assertEqual(decode, "test")

    def test_create_basic_auth(self):
        auth = Base64TokenGenerator.create_basic_auth("testUser@testmail.com", "testPassword")
        self.assertEqual(auth, "dGVzdFVzZXJAdGVzdG1haWwuY29tOnRlc3RQYXNzd29yZA==")

    # def test_options_selection(self):
    #    selection = Base64TokenGenerator()
    #    option = selection.select_action()


if __name__ == '__main__':
    unittest.main()
