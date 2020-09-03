class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0: return "Zero"
        dict = {
            1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
            6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten",
            11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen",
            15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen",
            19: "Nineteen", 20: "Twenty", 30: "Thirty", 40: "Forty",
            50: "Fifty", 60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety"
        }

        def from_three_digit(num_str):
            output = ""
            if int(num_str[0]):
                output += dict[int(num_str[0])] + " Hundred "
            if int(num_str[1]):
                if num_str[1] == "1":
                    output += dict[int(num_str[1:])]
                    return output
                else:
                    output += dict[int(num_str[1])*10] + " "
            if int(num_str[2]):
                output += dict[int(num_str[2])]
            return output.strip()

        ret = ""
        num_str = str(num)
        num_str = '0'*(10-len(num_str)) + num_str

        if int(num_str[0]):
            ret += dict[int(num_str[0])] + " Billion "
        if int(num_str[1:4]):
            ret += from_three_digit(num_str[1:4]) + " Million "
        if int(num_str[4:7]):
            ret += from_three_digit(num_str[4:7]) + " Thousand "
        ret += from_three_digit(num_str[7:10])
        return ret.strip()

