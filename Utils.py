class Utils:
    
    def Clamp(x, min, max):
        if (x > max):
            return max
        
        if (x < min):
            return min
        
        return x