import unittest
from 917-reverse_only_letters import Solution


class TestCircleArea(unittest.TestCase):
    def test_area(self):
        self.assertEqual(Solution().reverseOnlyLetters("ab-cd"), "dc-ba")
        self.assertEqual(Solution().reverseOnlyLetters("a-bC-dEf-ghIj"), "j-Ih-gfE-dCba")
        self.assertEqual(Solution().reverseOnlyLetters("Test1ng-Leet=code-Q!"), "Qedo1ct-eeLg=ntse-T!")
