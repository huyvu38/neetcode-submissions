class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        freq = defaultdict()
        for bill in bills:
            if bill == 5:
                freq["5"] = freq.get("5", 0) + 1
            if bill == 10:
                if freq.get("5", 0) == 0:
                    return False
                else:
                    freq["5"] = freq.get("5", 0) - 1
                    freq["10"] = freq.get("10", 0) + 1
            if bill == 20:
                if freq.get("5", 0) == 0:
                    return False
                else:
                    if freq.get("10", 0) > 0:
                        freq["5"] = freq.get("5", 0) - 1
                        freq["10"] = freq.get("10", 0) - 1
                        freq["20"] = freq.get("20", 0) + 1
                    else:
                        if freq.get("5", 0) < 3:
                            return False
                        else:
                            freq["5"] = freq.get("5", 0) - 3
                            freq["20"] = freq.get("20", 0) + 1
        return True
