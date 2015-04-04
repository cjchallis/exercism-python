"""Tests for the ocr-numbers exercise

Implementation note:
Both ocr.grid and ocr.number should validate their input
and raise ValueErrors with meaningful error messages
if necessary.
"""

import os
import unittest

from ocr import grid, number

ROW = 4
COL = 3

all = ['    _  _     _  _  _  _  _  _ ',
       '  | _| _||_||_ |_   ||_||_|| |',
       '  ||_  _|  | _||_|  ||_| _||_|', 
       '                              ']

ocr_list = [[all[i][COL*j:COL*(j+1)]
	     for i in range(ROW)]
	     for j in range(10)]

ocr_list = [ocr_list[-1]] + ocr_list[:9]

def join_ocr(digits):
	ocr = ['' for i in range(ROW)]
	for d in digits:
		for r in range(ROW):
			ocr[r] += ocr_list[int(d)][r]
	return ocr


ZERO = [
    " _ ",
    "| |",
    "|_|",
    "   "
]

ONE = [
    "   ",
    "  |",
    "  |",
    "   "
]

class OcrTest(unittest.TestCase):

    def test_0(self):
        self.assertEqual('0', number(ZERO))

    def test_1(self):
        self.assertEqual('1', number(ONE))

    def test_garbage(self):
        self.assertEqual('?', number([" _ ",
                                      " _|",
                                      "  |",
                                      "   "]))

    def test_last_line_nonblank(self):
        self.assertEqual('?', number(["   ",
                                      "  |",
                                      "  |",
                                      "| |"]))

    def test_unknown_char(self):
        self.assertEqual('?', number([" - ",
                                      " _|",
                                      " X|",
                                      "   "]))

    def test_too_short_row(self):
        self.assertRaises(ValueError, number, ["   ",
                                               " _|",
                                               " |",
                                               "   "])

    def test_insufficient_rows(self):
        self.assertRaises(ValueError, number, ["   ",
                                               " _|",
                                               " X|"])

    def test_grid0(self):
        self.assertEqual(ZERO, grid('0'))

    def test_grid1(self):
        self.assertEqual(ONE, grid('1'))

    def test_0010110(self):
        self.assertEqual('0010110', number(join_ocr('0010110')))
        
    def test_3186547290(self):
        self.assertEqual('3186547290', number(join_ocr('3186547290')))

    def test_Lost(self):
        digits = '4815162342'
        self.assertEqual(digits, number(join_ocr(digits)))
        
    def test_garble_middle(self):
        digits = '12345'
        ocr_digits = join_ocr(digits)
        ocr_digits[1] = ocr_digits[1].replace(' _||', '  ||')
        self.assertEqual('12?45', number(ocr_digits))

    def test_3186547290_grid(self):
        dig = '3186547290'
        self.assertEqual(join_ocr(dig), grid(dig))

    def test_invalid_grid(self):
       self.assertRaises(ValueError, grid, '123a')

if __name__ == '__main__':
    unittest.main()
