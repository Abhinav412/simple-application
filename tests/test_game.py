import unittest

from game import STORY, get_next_node


class GameLogicTests(unittest.TestCase):
    def test_get_next_node_valid_choice(self):
        self.assertEqual(get_next_node(STORY, "start", 0), "forest")
        self.assertEqual(get_next_node(STORY, "start", 1), "mountain")

    def test_get_next_node_invalid_choice_raises(self):
        with self.assertRaises(ValueError):
            get_next_node(STORY, "start", 2)


if __name__ == "__main__":
    unittest.main()
