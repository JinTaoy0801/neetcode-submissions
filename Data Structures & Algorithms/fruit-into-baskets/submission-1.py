class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        hm = {}
        first = 0
        second = 0
        result = 0
        for second in range(len(fruits)):
            if fruits[second] not in hm:
                hm[fruits[second]] = 0
            while len(hm) > 2:
                hm[fruits[first]]-=1
                if hm[fruits[first]] == 0:
                    del hm[fruits[first]]
                first+=1
            hm[fruits[second]] = hm[fruits[second]] + 1
            result = max(result, second - first + 1)
        
        return result
            

