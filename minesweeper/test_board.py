import unittest

import board


class TestStringMethods(unittest.TestCase):
    def test_field_defaults(self) -> None:
        field = board.Field()
        self.assertTrue(field.hidden)
        self.assertFalse(field.mine)
        self.assertIsNone(field.clue)
        self.assertFalse(field.marked)

    def test_field(self) -> None:
        field = board.Field(hidden=False, mine=True, clue=2, marked=True)
        self.assertFalse(field.hidden)
        self.assertTrue(field.mine)
        self.assertEqual(field.clue, 2)
        self.assertTrue(field.marked)


if __name__ == "__main__":
    unittest.main()
