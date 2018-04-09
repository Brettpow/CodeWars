from parameterized import parameterized

import code
import unittest 

class TestUniqueinorder(unittest.TestCase):
	@parameterized.expand([
		["test1", "AAAABBBCCDAABBB", ['A','B','C','D','A','B']],
		["test2", "AAXABBUCCDAABYB", ['A','X','A','B','U','C','D','A','B','Y','B']],
		["test3", "A", ['A']],
		["test4", "AA", ['A']]
	])

	def test_uniqueinorder(self, name, origin, expected):
		self.assertEqual(code.unique_in_order(origin), expected)
	#assert_equals(unique_in_order('AAAABBBCCDAABBB'), ['A','B','C','D','A','B'])
