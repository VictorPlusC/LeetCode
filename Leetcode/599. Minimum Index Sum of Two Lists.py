"""
599. Minimum Index Sum of Two Lists
Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

Example 1:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".
Example 2:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
Note:
The length of both lists will be in the range of [1, 1000].
The length of strings in both lists will be in the range of [1, 30].
The index is starting from 0 to the list length minus 1.
No duplicates in both lists.
"""
# Time complexity: O(N+M)
# Space complexity: O(N*L), where N is list1, L is the average length of a word
class Solution:
    def findRestaurant(self, list1, list2):
        idxs_1 = {v:i for i, v in enumerate(list1)}
        min_sum = float('inf')
        interests = []
        for i, v in enumerate(list2):
            temp_sum = i + idxs_1.get(v, float('inf'))
            if temp_sum < min_sum:
                min_sum = temp_sum
                interests = [v]
            elif temp_sum == min_sum:
                interests.append(v)
        
        return interests
