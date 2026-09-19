class Solution:
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        closest_x = max(x1, min(x_center, x2))
        closest_y = max(y1, min(y_center, y2))
        
        dx = x_center - closest_x
        dy = y_center - closest_y
        
        return (dx**2 + dy**2) <= (radius**2)