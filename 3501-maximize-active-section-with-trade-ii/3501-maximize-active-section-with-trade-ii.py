

class Solution:
    def maxActiveSectionsAfterTrade(self,s: str,queries: List[List[int]]) -> List[int]:

        blkStart = []
        blkEnd = []
        blkSize = []

        curr = 0
        n = len(s)

        for i in range(n):
            if s[i] == '0':
                if (i > 0 and s[i - 1] == '1') or i == 0:
                    blkStart.append(i)

                curr += 1

            else:

                if curr > 0:
                    blkSize.append(curr)

                curr = 0

                if i > 0 and s[i-1] == '0':
                    blkEnd.append(i - 1)

        if s[-1] == '0':
            blkEnd.append(n - 1)
            blkSize.append(curr)

        onesCount = s.count('1')

        if len(blkStart) < 2:
            return [onesCount] * len(queries)

        
        pairSum = [blkSize[i] + blkSize[i + 1] for i in range(len(blkSize) - 1)]

        

        segTree = [0] * (4 * len(pairSum))

        def buildSegmentTree(idx, s, e):

            if s == e:
                segTree[idx] = pairSum[s]
                return

            mid = s + (e - s) // 2

            buildSegmentTree(2 * idx + 1,s,mid)

            buildSegmentTree(2 * idx + 2,mid + 1,e)

            segTree[idx] = max(segTree[2 * idx + 1],segTree[2 * idx + 2] )

        def rangeMax(idx, s, e, tarS, tarE):
            if s > tarE or e < tarS:
                return float('-inf')

            
            if s >= tarS and e <= tarE:
                return segTree[idx]

            
            mid = s + (e - s) // 2

            return max(
                rangeMax(2 * idx + 1, s,mid, tarS,tarE),
                rangeMax(2 * idx + 2, mid + 1,e,tarS, tarE)
            )


        buildSegmentTree(0,0,len(pairSum) - 1 )

        

        result = []

        for q in queries:

            l = q[0]
            r = q[1]

            
            low = bisect_left(blkEnd, l)
            high = bisect_right(blkStart, r) - 1

            maxPairSum = 0

            if low < high:
                firstLen = (blkEnd[low]- max(blkStart[low], l) + 1)
                lastLen = (min(blkEnd[high], r) - blkStart[high] + 1)


                if high - low == 1:
                    maxPairSum = firstLen + lastLen

                else:

                    
                    pair1 = firstLen + blkSize[low + 1]
                    pair2 = blkSize[high - 1] + lastLen

                    
                    RMQMaxPairSum = rangeMax(0,0,len(pairSum) - 1,low + 1,high - 2)

                    maxPairSum = max(pair1,pair2,RMQMaxPairSum)

            result.append(maxPairSum + onesCount)

        return result