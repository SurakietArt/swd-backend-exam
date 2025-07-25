"""
เขียนโปรแกรมหาจำนวนเลข 0 ที่ออยู่ติดกันหลังสุดของค่า factorial โดยห้ามใช้ function from math

[Input]
number: as an integer

[Output]
count: count of tailing zero as an integer

[Example 1]
input = 7
output = 1

[Example 2]
input = -10
output = number can not be negative
"""


class Solution:

    def find_tailing_zeroes(self, number: int) -> int | str:
        if number < 0:
            return "number can not be negative"
        fac_result = 1
        for i in range(2, number + 1):
            fac_result *= i

        digits = [int(d) for d in str(fac_result)]
        zero_count = 0
        for i in range(1, len(digits) + 1):
            digit = digits[-i]
            if digit == 0:
                zero_count += 1
            else:
                break
        return zero_count
