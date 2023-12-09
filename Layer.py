class Layer():
    Default = 0
    Ship = 1
    Alien = 2
    ShipProjectile = 3
    AlienProjectile = 4
    Block = 5
    #                             BPPASD
    _DefaultLayerMask       = 0b11111111
    _ShipLayerMask          = 0b11111101
    _AlienLayerMask         = 0b11111011
    _SProjectileLayerMask   = 0b11100101
    _AProjectileLayerMask   = 0b11100011
    _BlockLayerMask         = 0b11011111
    
    _masks = [
        _DefaultLayerMask,
        _ShipLayerMask,
        _AlienLayerMask,
        _SProjectileLayerMask,
        _AProjectileLayerMask,
        _BlockLayerMask]
    
    def DoInteract(layerA : int, layerB : int) -> bool :
        aMask = Layer._masks[layerA]
        bFlag = 1 << layerB
        return (aMask & bFlag) == bFlag
    
    