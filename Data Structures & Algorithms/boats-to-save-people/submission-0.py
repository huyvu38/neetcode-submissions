class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        count = 0
        l = 0
        r = len(people) - 1
        while l <= r:
            if people[l] + people[r] <= limit:
                l = l+1
            r=r-1
            count = count + 1
        return count