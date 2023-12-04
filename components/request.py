class request():
    def __init__(self, type: str, data: dict) -> None:
        self._type = type.upper()
        self._data = data
    
    def checkData(self, data: dict):
        match self.type:
            case "GET":
                required_headers = ["User-Agent", "Accept"]
                for _ in required_headers:
                    if data.get(_) == None:
                        raise Exception(f"Required header item {_} was not specified for the request.")
                    
    def addData(self, newData: dict):
        for _ in newData:
            self._data.update({f"{_}": f"{newData.get(_)}"}) # Append key (_) and its new value (newData.get(_)) to request data
    
    def removeData(self, dataName: str):
        self._data.pop(dataName)
    
    @property
    def data(self):
        return self._data