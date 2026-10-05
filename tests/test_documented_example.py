"""Run the Python code published in the exercise, without a duplicate implementation."""

from html.parser import HTMLParser
from pathlib import Path
import unittest

import markdown


class PythonBlocks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.blocks = []
        self.current = None

    def handle_starttag(self, tag, attrs):
        if tag == "code" and "language-python" in dict(attrs).get("class", "").split():
            self.current = []

    def handle_data(self, data):
        if self.current is not None:
            self.current.append(data)

    def handle_endtag(self, tag):
        if tag == "code" and self.current is not None:
            self.blocks.append("".join(self.current))
            self.current = None


class DocumentedExampleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        path = Path(__file__).resolve().parents[1] / "docs/examples/first-maximum.md"
        parser = PythonBlocks()
        parser.feed(markdown.markdown(path.read_text(encoding="utf-8"), extensions=["fenced_code"]))
        if len(parser.blocks) != 1:
            raise AssertionError("The exercise must contain exactly one executable Python solution")
        namespace = {}
        exec(compile(parser.blocks[0], str(path), "exec"), namespace)
        cls.find_maximum = staticmethod(namespace["first_max_index"])

    def assert_result(self, values, expected):
        original = values.copy()
        self.assertEqual(self.find_maximum(values), expected)
        self.assertEqual(values, original, "The example must not mutate its input")

    def test_empty_input(self):
        self.assert_result([], None)

    def test_single_item(self):
        self.assert_result([4], 0)

    def test_negative_values(self):
        self.assert_result([-5, -2, -9], 1)

    def test_first_of_repeated_maxima(self):
        self.assert_result([3, 7, 7, 2], 1)

    def test_equal_values(self):
        self.assert_result([6, 6, 6], 0)

    def test_maximum_at_start(self):
        self.assert_result([9, 2, 1], 0)

    def test_maximum_at_end(self):
        self.assert_result([1, 2, 9], 2)

    def test_documented_limits(self):
        self.assert_result([-1_000_000] * 9_999 + [1_000_000], 9_999)


if __name__ == "__main__":
    unittest.main()
