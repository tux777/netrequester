class request():
    def __init__(self, type: str, data = {None}) -> None:
        self.type = type.lower()
        self._data = data
    
    def checkData(self, data: dict):
        match self.type:
            case "get":
                print("Not finished")
            

    def addData(data: dict):
        print("Not finished")