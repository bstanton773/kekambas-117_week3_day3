from unittest import TestCase, main
from whiteboard import solution


class WhiteboardTestCase(TestCase):
    
    def test_1(self):
        self.assertEqual(solution("Hey welcome to doing whiteboard problems get prepared to figure our a problem on the fly"), "Hey! Welcome to doinG Whiteboard problems. Get prepared to fiGure our a problem on the fly!")
    
    def test_2_test_caps(self):
        self.assertEqual(solution("wsWGYy"), "Ws.WGY!y!")

    def test_3_no_change(self):
        self.assertEqual(solution("abd WG"), "abd WG")

if __name__ == "__main__":
    main()
