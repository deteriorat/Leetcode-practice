class Solution:
    def calculate(self, s: str) -> int:
        stack = [1]
        sign = 1
        n = len(s)
        ans = 0
        i = 0

        while i < n:
            if s[i] == '+':
                sign = stack[-1]
                i += 1
            elif s[i] == '-':
                sign = -stack[-1]
                i += 1
            elif s[i] == '(':
                stack.append(sign)
                i += 1
            elif s[i] == ')':
                stack.pop()
                i += 1
            elif s[i].isdigit():
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                ans += sign * num
            else:
                i += 1
        return ans
