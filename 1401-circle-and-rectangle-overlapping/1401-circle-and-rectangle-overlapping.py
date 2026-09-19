class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        
        nx1 = xCenter
        if x1 > xCenter:
            nx1 = x1
        elif x2 < xCenter:
            nx1 = x2
        ny1 = yCenter
        if y1 > yCenter:
            ny1 = y1
        elif y2 < yCenter:
            ny1 = y2
        
        return int(sqrt(((nx1-xCenter)**2) + ((ny1-yCenter)**2))) <= radius
        

        