class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hold = Counter(s1)
        length = len(s2)
        seen = defaultdict(int)
        beg = 0
        
        for end in range(length):
            if s2[end] not in hold:
                seen.clear()
                beg = end+1
            else: 
                seen[s2[end]] += 1
                while seen[s2[end]] > hold[s2[end]]:
                    seen[s2[beg]] -= 1
                    if seen[s2[beg]] == 0:
                        seen.pop(s2[beg])
                    beg += 1
                
            if hold == seen:
                return True
        return False