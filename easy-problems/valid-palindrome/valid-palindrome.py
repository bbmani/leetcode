from typing import final


def isPalindrome(s):
        """
        :type s: str
        :rtype: bool
        """
        alphabets_only = "".join(character.lower() for character in s if character.isalpha())
        alphabets_only_reverse = alphabets_only[::-1]
        return alphabets_only == alphabets_only_reverse
if __name__ == "__main__" :
    final_answer = isPalindrome("0P")
    print(final_answer)