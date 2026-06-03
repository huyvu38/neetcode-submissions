class Solution(object):
    def mergeTriplets(self, triplets, target):
        """
        :type triplets: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        check = set()
        for t in triplets:
            #Skip if any x,y,z is greater than target
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            for i in range(0,3):
                if target[i] == t[i]:
                    check.add(i)
        return len(check) == 3