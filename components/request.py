import requests

types = ["GET", "POST", "PATCH"]

class request():
    def __init__(self, type: str, data: dict) -> None:
        self._type = None
        if type.upper().strip() not in types:
            raise Exception(f"Will not initialize request type to \"{type}\" because it is not a valid request type.")
        else:
            self._type = type
          
          
        self._data = data

    def request(self, url: str):
        match self._type:
            case "GET":
              return requests.get(url, headers=self._data)
            case "POST":
              return requests.post(url, headers=self._data)
            case "PATCH":
              return requests.patch(url, headers=self._data)
      
  
    @property
    def data(self):
        return self._data

    def checkData(self, data: dict):
      match self.type:
          case "GET":
              required_headers = ["User-Agent", "Accept"]
              for _ in required_headers:
                  if data.get(_) == None:
                      raise Exception(f"Required header item {_} was not specified for the request.")
          case "POST":
            required_headers = ["User-Agent", "Content-Type"]
            for _ in required_headers:
                if data.get(_) == None:
                    raise Exception(f"Required header item {_} was not specified for the request.")
  
    def addData(self, newData: dict):
        for _ in newData:
            self._data.update({f"{_}": f"{newData.get(_)}"}) # Append key (_) and its new value (newData.get(_)) to request data
        self.checkData(self._data)
          
  
    def removeData(self, dataName: str):
        self._data.pop(dataName)
      
    @property
    def type(self):
        return self._type

    def changeType(self, newType):
        if newType.upper().strip() not in types:
            raise Exception(f"Will not change request type to \"{newType}\" because it is not a valid request type.")
        self._type = newType