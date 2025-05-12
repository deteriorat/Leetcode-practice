def blank(n):
    return ' '*n

#折磨人的字符串题目

class Solution:

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        right, n = 0, len(words)
        while True:
            left = right
            sumLen = 0
            while right < n and sumLen + len(words[right]) + right - left <= maxWidth:
                sumLen += len(words[right])
                right += 1
            
            if right == n:
                s = " ".join(words[left:])
                ans.append(s + blank(maxWidth - len(s)))
                break

            numWords = right - left
            numSpaces = maxWidth - sumLen


            if numWords == 1:
                ans.append(words[left] + blank(numSpaces))
                continue

            avgSpaces = numSpaces // (numWords - 1)
            extraSpaces = numSpaces % (numWords - 1)
            s1 = blank(avgSpaces + 1).join(words[left:left + extraSpaces + 1])
            s2 = blank(avgSpaces).join(words[left + extraSpaces + 1: right])
            ans.append(s1 + blank(avgSpaces) + s2)

        return ans