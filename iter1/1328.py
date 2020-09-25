class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        # case 0: empty string
        if len(palindrome) <= 1: return ""

        # case 1: replace a character by 'a'
        # and we can't modify the value in the middle
        for i in range(len(palindrome)):
            if i*2 == len(palindrome)-1: continue
            if palindrome[i] != "a":
                return palindrome[:i] + "a" + palindrome[i+1:]

        # case 2: all chars are 'a', so we replace the last a by b
        return palindrome[:-1] + "b"


