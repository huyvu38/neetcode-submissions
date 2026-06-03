class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        new_dict = dict()
        for num in hand:
            new_dict[num] = new_dict.get(num, 0) + 1
        hand.sort()
        for num in hand:
            if new_dict[num] > 0:
                for i in range(num, num + groupSize):
                    if new_dict.get(i, 0) == 0:
                        return False
                    new_dict[i] -= 1
        
        return True