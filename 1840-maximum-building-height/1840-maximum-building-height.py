class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions = restrictions + [[1, 0], [n, n - 1]]
        restrictions.sort()
        
        # Forward pass: enforce constraint from left neighbor
        for i in range(1, len(restrictions)):
            id1, h1 = restrictions[i - 1]
            id2, h2 = restrictions[i]
            restrictions[i][1] = min(h2, h1 + (id2 - id1))
        
        # Backward pass: enforce constraint from right neighbor
        for i in range(len(restrictions) - 2, -1, -1):
            id1, h1 = restrictions[i]
            id2, h2 = restrictions[i + 1]
            restrictions[i][1] = min(h1, h2 + (id2 - id1))
        
        # Now find max height achievable between consecutive constrained buildings
        ans = 0
        for i in range(1, len(restrictions)):
            id1, h1 = restrictions[i - 1]
            id2, h2 = restrictions[i]
            dist = id2 - id1
            # Peak height between two constrained points
            peak = (h1 + h2 + dist) // 2
            ans = max(ans, h1, h2, peak)
        
        return ans