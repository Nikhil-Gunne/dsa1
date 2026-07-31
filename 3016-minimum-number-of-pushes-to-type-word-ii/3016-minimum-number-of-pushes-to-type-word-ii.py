class Solution:
    def minimumPushes(self, word: str) -> int:

        freq = [0] *26
        for i in word:
            freq[ord(i)-97] +=1
        
        maxHeap = []
        for i in range(26):
            if freq[i]:
                heappush(maxHeap,-freq[i])
        places = 1
        cnt = 0
        presses = 0
        while maxHeap:
            curr = heappop(maxHeap)
            presses += (-curr*places)
            cnt+=1
            if cnt % 8 == 0:
                places += 1
        return presses


        