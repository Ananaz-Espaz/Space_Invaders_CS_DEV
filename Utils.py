from random import random

class Utils:
    
    def Clamp(x, min, max):
        if (x > max):
            return max
        
        if (x < min):
            return min
        
        return x

    def RandProb(prob):
        """
        Renvoie True selon une certaine probabilité "prob"

        Arguments:
        
            prob: float
                Probabilité de retourner True

        Return:
        
            tf: type = bool
                True ou False selon la probabilité "prob" et un tirage aléatoire
        """
        prob = Utils.Clamp(prob, 0, 1)
        return random()<=prob