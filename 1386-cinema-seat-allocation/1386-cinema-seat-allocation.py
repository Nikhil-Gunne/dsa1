class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rowsHavingReservation = defaultdict(set)
        
        for r,s in reservedSeats:
            rowsHavingReservation[r].add(s)

        def helper(occSeats,seats):
            for i in seats:
                if i in occSeats:
                    return 0
            return 1
        #for rows that dont have any reservations we can accomodate 2 families
        res =(n - len(rowsHavingReservation))*2
        #iterate over the each row having reservation and check occupancy of the seats 
        for r in rowsHavingReservation:
            left = helper(rowsHavingReservation[r],[2,3,4,5])
                
            middle = helper(rowsHavingReservation[r], [4,5,6,7])
            
            right = helper(rowsHavingReservation[r], [6,7,8,9])
           

            if left and right:
                res += 2
            elif middle or left or right:
                res+=1
            # elif left:
            #     res+=1
            # elif right:
            #     res+=1
        return res

        