class Node:
    def __init__(self,mxLen = 0,fc = "",lc = "",pre=0,suff=0):
        self.maxLen = mxLen
        self.firstChar = fc
        self.lastChar = lc
        self.prefix = pre
        self.suffix = suff

class Solution:
    def longestRepeating(self, start: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(start)
        segTree = [""] * (4*n)

        def merge(leftIdx,rightIdx,leftLen,rightLen):
            leftNode = segTree[leftIdx]
            rightNode = segTree[rightIdx]
            newNode = Node()
            newNode.maxLen = max(leftNode.maxLen,rightNode.maxLen)
            if leftNode.lastChar == rightNode.firstChar:
                newNode.maxLen = max(leftNode.suffix + rightNode.prefix,newNode.maxLen)
            
            newNode.prefix = leftNode.prefix
            if leftLen == leftNode.prefix and leftNode.lastChar == rightNode.firstChar:
                newNode.prefix = leftNode.prefix + rightNode.prefix
            
            newNode.suffix = rightNode.suffix
            if rightLen == rightNode.suffix and leftNode.lastChar == rightNode.firstChar:
                newNode.suffix = leftNode.suffix + rightNode.suffix
            newNode.firstChar = leftNode.firstChar
            newNode.lastChar = rightNode.lastChar

            return newNode
        
        def update(idx,start,end,pos,ch):
            if start==end:
                segTree[idx] = Node(1,ch,ch,1,1)
                return 

            mid = start + (end-start)//2
            if pos <= mid:
                update(2*idx+1,start,mid,pos,ch)
            else:
                update(2*idx+2,mid+1,end,pos,ch)
            segTree[idx] = merge(2*idx+1,2*idx+2,mid-start+1,end-(mid+1)+1)
        
            


        def buildTree(idx,rangeStart,rangeEnd):
            if (rangeStart == rangeEnd):
                segTree[idx] =  Node(1,start[rangeStart], start[rangeStart],1,1)
                return


            mid = rangeStart + (rangeEnd - rangeStart) // 2
            left = buildTree(2*idx+1,rangeStart,mid)
            right = buildTree(2*idx+2,mid+1,rangeEnd)
            leftLen = mid - rangeStart + 1
            rightLen = rangeEnd - (mid + 1) + 1
            segTree[idx] = merge(2*idx+1,2*idx+2,leftLen,rightLen)

        buildTree(0,0,n-1)

        res = [0] * len(queryIndices)
        for i in range(len(queryIndices)):
            update(0,0,n-1,queryIndices[i], queryCharacters[i])
            res[i] = segTree[0].maxLen
        return res

        