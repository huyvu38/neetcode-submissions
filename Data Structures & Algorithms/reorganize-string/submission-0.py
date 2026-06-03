import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        # Count frequency manually
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        
        # Build max heap
        max_heap = []
        for char in freq:
            heapq.heappush(max_heap, (-freq[char], char))
        
        result = []
        
        # Process heap
        while len(max_heap) > 1:
            count1, char1 = heapq.heappop(max_heap)
            count2, char2 = heapq.heappop(max_heap)
            
            result.append(char1)
            result.append(char2)
            
            # decrease counts
            if count1 + 1 < 0:
                heapq.heappush(max_heap, (count1 + 1, char1))
            if count2 + 1 < 0:
                heapq.heappush(max_heap, (count2 + 1, char2))
        
        #If one character left
        if max_heap:
            count, char = heapq.heappop(max_heap)
            if count < -1:
                return ""  # impossible
            result.append(char)
        
        return "".join(result)