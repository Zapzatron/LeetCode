class Solution:
    def romanToInt(self, s: str) -> int:
        output = False
        characters = set('IVXLCDM')
        symb_val = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        roman_num = s
        int_num = 0
        if 1 <= len(roman_num) <= 15:
            if not characters.isdisjoint(s):
                for i in range(len(roman_num)):
                    try:
                        a = roman_num[i]
                        if output:
                            print(f"Symbol: {roman_num[i]}")
                            print(f"Before: {int_num}")
                    except IndexError:
                        break
                    try:
                        if roman_num[i + 1]:
                            if roman_num[i] == "I":
                                if roman_num[i + 1] in "VX":
                                    int_num += (symb_val[roman_num[i + 1]] - symb_val[roman_num[i]])
                                    roman_num = roman_num.replace(roman_num[i + 1], '', 1)
                                else:
                                    int_num += symb_val[roman_num[i]]
                            elif roman_num[i] == "X":
                                if roman_num[i + 1] in "LC":
                                    int_num += (symb_val[roman_num[i + 1]] - symb_val[roman_num[i]])
                                    roman_num = roman_num.replace(roman_num[i + 1], '', 1)
                                else:
                                    int_num += symb_val[roman_num[i]]
                            elif roman_num[i] == "C":
                                if roman_num[i + 1] in "DM":
                                    int_num += (symb_val[roman_num[i + 1]] - symb_val[roman_num[i]])
                                    roman_num = roman_num.replace(roman_num[i + 1], '', 1)
                                else:
                                    int_num += symb_val[roman_num[i]]
                            else:
                                int_num += symb_val[roman_num[i]]
                    except IndexError:
                        int_num += symb_val[roman_num[i]]
                    if output:
                        print(f"After: {int_num}")

                print(f"Input: s = {roman_num}")
                print(f"Output: {int_num}")
                print(f"Explanation: {roman_num} = {int_num}.")
        return int_num
