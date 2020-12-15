class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        left = ""
        for i in range(len(num2)-1, -1, -1):
            right, flag = "", 0
            for q in range(len(num1)-1, -1, -1):
                out = (int(num2[i]) * int(num1[q])) + flag
                if right == "0" and out == 0: continue
                right += str(out % 10)
                flag = out // 10
            right = (str(flag) if flag != 0 else "") + right[::-1] + "0"*(len(num2)-i-1)

            x, out, flag = -1, "", 0
            for x in range(min(len(left), len(right))):
                res = int(left[len(left)-x-1]) + int(right[len(right)-x-1]) + flag
                flag = res // 10
                out += str(res % 10)
            high = (left[:len(left)-x-1]
                    if len(left) > len(right) else right[:len(right)-x-1])
            if flag:
                for x in range(len(high)-1, -1, -1):
                    if high[x] == "9": high = high[:x] + "0" + high[x+1:]
                    else:
                        high = high[:x] + str(int(high[x])+1) + high[x+1:]
                        break
                else:
                    high = "1"+high
            left = high + out[::-1]
        return left



