# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
# Return the length of the longest substring containing the same letter you can get after performing the above operations.

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.
 
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        string_length = len(s)
        length_of_max_substring = 0
        start = 0
        char_freq = {}
        most_freq_char = 0

        for end in range(string_length):
            # if the new character is not in the dictionary, add it, else increment its frequency
            char_freq[s[end]] = char_freq.get(s[end], 0) + 1

            # update the most frequent char
            most_freq_char = max(most_freq_char, char_freq[s[end]])

            # if the number of replacements in the current window have exceeded
            # the limit, slide the window
            if end - start + 1 - most_freq_char > k:
                char_freq[s[start]] -= 1
                start += 1

            # if this window is the longest so far, update the length of max
            # substring
            length_of_max_substring = max(end - start + 1, length_of_max_substring)

        # return the length of the max substring with same characters after
        # replacement(s)
        return length_of_max_substring
