"""Given a string, find the length of the longest substring without repeating characters."""


class Solution:

    """every iteration adds a character from string to dict with character as key and its index as
    value. if a repeating value is not found, the result is updated as the difference between p and the current index
    plus one. where p is the last starting point of a non repeating substring.
     when a repeating character is found and p is less than or equal to the index of the repeating
      character found. which means the index of the repeated character stored is in the middle of the
       none repeating substring. p is updated to the index of the repeating character's index stored in dict"""

    def length_of_longest_substring(self, s):
        buffer = dict()
        result = p = 0

        for x in range(len(s)):
            if s[x] in buffer and p <= buffer[s[x]]:
                p = buffer[s[x]] + 1
            else:
                result = max(result, x - p + 1)
            buffer[s[x]] = x

        return result
