import unittest
import Game
import Frame


class MyTestCase(unittest.TestCase):
    game = Game.Game

    def test_rollOne(self):
        self.game.addRole(1)
        self.assertEqual(1, self.game.getRole)

    def test_frame(self):
        frame = Frame.Frame()
        frame.addFirst(1)
        expected = ([1], 1)
        self.assertEqual(expected, frame.getValue)

    def test_frame_second(self):
        frame = Frame.Frame()
        frame.addFirst(1)
        frame.addSecond(1)
        expected = ([1,1], 2)
        self.assertEqual(expected, frame.getValue)

    def test_frame_Last(self):
        frame = Frame.Frame(isLast=1)
        frame.addFirst(1)
        frame.addSecond(9)
        frame.addthird(1)
        expected = ([1,9,1], 11)
        self.assertEqual(expected, frame.getValue)
    def test_CheckRoll(self):
        acutual = Game.CheckRoll(1)
        expected = True
        self.assertEqual(expected, acutual)
    def Test_Strike(self):
        acutual = Game.Strike()
        expected =
        self.assertEqual(expected, acutual)
if __name__ == '__main__':
    unittest.main()
