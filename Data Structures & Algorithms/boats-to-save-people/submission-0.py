
#sort array and traverse with two pointers. When they are found set the value at the location to 0
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()
        size = len(people) -1
        l,r=0,size
        ret = 0
        
        
        while l <= r:
            weight = people[l] + people[r]
            while l < r and (people[r] == limit or weight > limit):
                r-=1
                ret+=1
                weight = people[l] + people[r]
            
            r-=1
            l+=1
            ret+=1
        return ret
