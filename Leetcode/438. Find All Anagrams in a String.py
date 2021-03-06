"""
438. Find All Anagrams in a String
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:
Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""
# Time complexity: O(N)
# Space complexity: O(1), because there can only be 26 different characters
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        size = len(p)
        anagram = collections.Counter(p)
        count = collections.Counter()

        output = []
        for i, c in enumerate(s):

            count[c] += 1
            if i >= size:
                count[s[i-size]] -= 1
                if count[s[i-size]] == 0:
                    del count[s[i-size]]

            if count == anagram:
                output.append(i-size+1)
                
        return output
