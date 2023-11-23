import requests

class Get:
    def __init__(self) -> None:
        self.bulkRequest = True
        

    @staticmethod
    def request(bulkRequest: bool):
        log_info(requests.get("https://google.com"))
        