"""
เขียบนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน list

[Input]
numbers: list of numbers

[Output]
index: index of maximum number in list

[Example 1]
input = [1,2,1,3,5,6,4]
output = 5

[Example 2]
input = []
output = list can not blank
"""


class Solution:

    def find_max_index(self, numbers: list[int]) -> int | str:
        if len(numbers) == 0:
            return "list can not blank"

        maxPos = 0
        maxNum = numbers[0]
        for idx, n in enumerate(numbers):
            if n > maxNum:
                maxNum = n
                maxPos = idx
        return maxPos
