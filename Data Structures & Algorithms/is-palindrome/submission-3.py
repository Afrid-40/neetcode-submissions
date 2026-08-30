class Solution:
    def isPalindrome(self, s: str) -> bool:
        new= ''
        for S in s:
            if S.isalnum():
                new += S.lower()
        return new == new[::-1]