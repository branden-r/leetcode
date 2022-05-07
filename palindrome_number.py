class Solution:
    def isPalindrome(self, integer: int) -> bool:
        return str(integer) == str(integer)[::-1]  # lol
