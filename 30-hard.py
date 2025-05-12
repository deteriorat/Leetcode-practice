class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        m, n = len(words), len(words[0])
        res = []

        for j in range(n):
            news = s[j:]
            s_list = [news[i*n : (i+1)*n] for i in range(0, len(news)//n)]
            
            sum = 0
            hash_map = {}
            for word in words:
                if word not in hash_map:
                    hash_map[word] = 0
                hash_map[word] -= 1

            
            for i in range(len(s_list)):
                if i<m:
                    if s_list[i] in hash_map:
                        hash_map[s_list[i]] += 1
                else:
                    if s_list[i-m] in hash_map:
                        hash_map[s_list[i-m]] -= 1
                    if s_list[i] in hash_map:
                        hash_map[s_list[i]] += 1

                if all(x==0 for x in hash_map.values()):
                    res.append(j + (i+1-m)*n)

        return res