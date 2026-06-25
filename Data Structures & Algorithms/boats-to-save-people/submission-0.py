class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = 0
        i, j = 0, len(people) - 1
        if len(people) == 1 or len(people) == 2:
            return 1
        
        people.sort()
        # 1, 2, 2, 3, 3

        while i <= j:
            if people[i] + people[j] > limit:
                boats += 1
                j -= 1
            elif people[i] + people[j] <= limit:
                boats += 1
                i += 1
                j -= 1
            elif i == j:
                boats += 1
                break
            
        return boats
