class Solution:
    def internalAngles(self, sides: list[int]) -> list[float]:
        a, b, c = sorted(sides)
        
        if a + b <= c:
            return []
            
        rad_A = math.acos((b * b + c * c - a * a) / (2.0 * b * c))
        rad_B = math.acos((a * a + c * c - b * b) / (2.0 * a * c))
        rad_C = math.acos((a * a + b * b - c * c) / (2.0 * a * b))
        
        angles = [math.degrees(rad_A), math.degrees(rad_B), math.degrees(rad_C)]
        angles.sort()
        
        return angles