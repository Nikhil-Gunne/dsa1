class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:

        def solve(idx):
            currSet = {""}      
            resultSet = set()   

            while idx < len(expression) and expression[idx] != '}':
                if expression[idx] == '{':
                    rec, next_idx = solve(idx + 1)
                    newSet = set()
                    for a in currSet:
                        for b in rec:
                            newSet.add(a + b)

                    currSet = newSet
                    idx = next_idx + 1   

                
                elif expression[idx] == ',':
                    resultSet.update(currSet)
                    currSet = {""}
                    idx += 1

                
                else:
                    start = idx

                    while (idx < len(expression)
                           and expression[idx] not in '{},'):
                        idx += 1

                    word = expression[start:idx]

                    newSet = set()
                    for s in currSet:
                        newSet.add(s + word)

                    currSet = newSet

            
            resultSet.update(currSet)

            return resultSet, idx

        return sorted(solve(0)[0])