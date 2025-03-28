import unittest

from num2label.num2label import (lowercase_letter, uppercase_letter,
                                 spreadsheet_column)


class TestNum2Label(unittest.TestCase):
    def test_uppercase_letter(self):
        self.assertIsInstance(uppercase_letter(8), str)
        self.assertEqual(uppercase_letter(1), "A")
        self.assertEqual(uppercase_letter(4), "D")
        self.assertEqual(uppercase_letter(26), "Z")
        self.assertEqual(uppercase_letter(35), "I")
        self.assertEqual(uppercase_letter(36, strict=False), "J")
        self.assertEqual(uppercase_letter(1, strict=True), "A")
        self.assertEqual(uppercase_letter(5, strict=True), "E")
        self.assertEqual(uppercase_letter(26, strict=True), "Z")
        self.assertRaises(ValueError, uppercase_letter, -1000)
        self.assertRaises(ValueError, uppercase_letter, 0)
        self.assertRaises(ValueError, uppercase_letter, 42, strict=True)
        self.assertRaises(TypeError, uppercase_letter, "14")
        self.assertRaises(TypeError, uppercase_letter, 65.2)

    def test_lowercase_letter(self):
        self.assertIsInstance(lowercase_letter(15), str)
        self.assertEqual(lowercase_letter(1), "a")
        self.assertEqual(lowercase_letter(4), "d")
        self.assertEqual(lowercase_letter(26), "z")
        self.assertEqual(lowercase_letter(35), "i")
        self.assertEqual(lowercase_letter(36, strict=False), "j")
        self.assertEqual(lowercase_letter(1, strict=True), "a")
        self.assertEqual(lowercase_letter(5, strict=True), "e")
        self.assertEqual(lowercase_letter(26, strict=True), "z")
        self.assertRaises(ValueError, lowercase_letter, -13)
        self.assertRaises(ValueError, lowercase_letter, 0)
        self.assertRaises(ValueError, lowercase_letter, 27, strict=True)
        self.assertRaises(TypeError, lowercase_letter, "1")
        self.assertRaises(TypeError, lowercase_letter, 9.5)

    def test_spreadsheet_column(self):
        self.assertIsInstance(spreadsheet_column(90), str)
        self.assertEqual(spreadsheet_column(1), "A")
        self.assertEqual(spreadsheet_column(4), "D")
        self.assertEqual(spreadsheet_column(26), "Z")
        self.assertEqual(spreadsheet_column(35), "AI")
        self.assertEqual(spreadsheet_column(27), "AA")
        self.assertEqual(spreadsheet_column(52), "AZ")
        self.assertEqual(spreadsheet_column(153), "EW")
        self.assertEqual(spreadsheet_column(705), "AAC")
        self.assertRaises(ValueError, spreadsheet_column, -2)
        self.assertRaises(ValueError, spreadsheet_column, 0)
        self.assertRaises(TypeError, spreadsheet_column, "8")
        self.assertRaises(TypeError, spreadsheet_column, 0.001)
