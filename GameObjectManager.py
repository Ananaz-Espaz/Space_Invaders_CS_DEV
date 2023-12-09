class GameObjectManager:
    GameObjects = []
    
    def Register(gameObject):
        GameObjectManager.GameObjects.append(gameObject)
        
    def Unregister(gameObject):
        GameObjectManager.GameObjects.remove(gameObject)