import sys
import unittest
import io
from mini_grep import mini_grep


class TestSum(unittest.TestCase):

    def test_without_q(self):
        sys.argv = ['mini_grep.py', '-e', 'hi', '/secret/test_file1.txt']
        self.assertIs(mini_grep(), None, 'Should print 1 hi')

    def test_with_q(self):
        sys.argv = ['mini_grep.py', '-q', '-e', 'hi', '/secret/test_file1.txt']
        self.assertIs(mini_grep(), None, 'Should print hi')

    def test_without_path(self):
        sys.argv = ['mini_grep.py', '-q', '-e', 'hi']
        sys.stdin = io.StringIO('/secret/test_file1.txt\n')
        self.assertIs(mini_grep(), None, 'Should print hi')


if __name__ == '__main__':
    unittest.main()
