"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def number_to_thai(self, number: int) -> str:
        if number < 0:
            return "number can not less than 0"
        if number == 0:
            return "ศูนย์"
        if number > 10_000_000:
            return "number must not more than 10,000,000"

        digit_text = ["", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า"]
        position_text = ["", "สิบ", "ร้อย", "พัน", "หมื่น", "แสน", "ล้าน"]

        def convert(num: int) -> str:
            result = ""
            digits = [int(d) for d in str(num)]
            length = len(digits)

            for i in range(length):
                d = digits[i]
                pos = length - i - 1

                if d == 0:
                    continue

                if pos == 0 and d == 1 and length > 1:
                    result += "เอ็ด"
                elif pos == 1 and d == 2:
                    result += "ยี่" + position_text[pos]
                elif pos == 1 and d == 1:
                    result += position_text[pos]
                else:
                    result += digit_text[d] + position_text[pos]
            return result

        million = 1000000
        if number < million:
            return convert(number)
        else:
            millions = number // million
            remainder = number % million
            text = convert(millions) + "ล้าน"
            if remainder > 0:
                text += convert(remainder)
            return text


x = Solution().number_to_thai(1003751)
print(x)
