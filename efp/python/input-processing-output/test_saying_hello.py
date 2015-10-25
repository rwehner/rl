'''
Test the saying-hello exercises
'''
import unittest

import saying_hello as sh


class TestSayingHello(unittest.TestCase):

    def setUp(self):
        self.default_greeting = "Hello, {name}, nice to meet you!"
        self.names = "Robert Ruben Andrea Kermit Ana Chaofeng".split()
        # { "name": "expectedgreeting" }
        self.custom_greetings = {
            "Ruben": "{name}! Hola amigo.",
            "Andrea": "Oh, {name}, I was meaning to pay you back...",
            "Kermit": "{name}, did you know you are called 'Gustavo' in Spain?"
            }

    def test_say_hello_primary(self):
        for name in self.names:
            self.assertEqual(sh.say_hello_primary(name_func=lambda: name),
                             self.default_greeting.format(name=name))

    def test_say_hello_no_variables(self):
        for name in self.names:
            self.assertEqual(sh.say_hello_no_variables(name_func=lambda: name),
                             self.default_greeting.format(name=name))

    def test_say_hello_custom_greetings(self):
        for name in self.names:
            greeting = self.custom_greetings.get(name, self.default_greeting)
            self.assertEqual(sh.say_hello_custom_greetings(
                custom_greetings=self.custom_greetings,
                name_func=lambda: name),
                greeting.format(name=name))

    def test_say_hello_custom_greetings_no_customization(self):
        for name in self.names:
            self.assertEqual(sh.say_hello_custom_greetings(
                name_func=lambda: name),
                self.default_greeting.format(name=name))


if __name__ == "__main__":
    unittest.main()
