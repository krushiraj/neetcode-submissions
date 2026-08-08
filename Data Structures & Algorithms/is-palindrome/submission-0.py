class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isalphanum(c):
            if 'a' <= c <= 'z':
                return True
            if 'A' <= c <= 'Z':
                return True
            if '0' <= c <= '9':
                return True
            return False

        return "".join(filter(lambda x: isalphanum(x), s.lower())) == "".join(filter(lambda x: isalphanum(x), s[::-1].lower()))