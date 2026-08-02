class Solution:
    def romanToInt(self, s: str) -> int:
        dict_roman = {
            'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000
        }
        roman_num = 0
        for i in range(len(s)):
            if i < len(s)-1:
                current_value = dict_roman[s[i]]
                next_value = dict_roman[s[i+1]]
                if current_value < next_value:
                    roman_num -= current_value
                else :
                    roman_num += current_value
            else:
                roman_num += dict_roman[s[i]]
        return roman_num
        




