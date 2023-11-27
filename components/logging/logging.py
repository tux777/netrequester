import colorama

# Yes, you can use these functions without the need of creating
# a logger instance, but creating a logger instance provides additional functionality
# Some of these features include logs being stored, counting amount of logs, setting a default type, etc.

types = ["info", "warning", "error", "debug", None]

def log_info(text, counter=None):
    if counter == None:   
        print(f"{colorama.Fore.GREEN}Info:{colorama.Fore.RESET} {text}")
    elif counter != None:
        print(f"{colorama.Fore.GREEN}Info {counter}:{colorama.Fore.RESET} {text}")

def log_warn(text, counter=None):
    if counter == None:
        print(f"{colorama.Fore.YELLOW}Warning:{colorama.Fore.RESET} {text}")
    elif counter != None:
        print(f"{colorama.Fore.YELLOW}Warning {counter}:{colorama.Fore.RESET} {text}")

def log_error(text, counter=None):
    if counter == None:
        print(f"{colorama.Fore.RED}Error:{colorama.Fore.RESET} {text}")
    elif counter != None:
        print(f"{colorama.Fore.RED}Error {counter}:{colorama.Fore.RESET} {text}")

def log_debug(text):
    print(f"{colorama.Fore.BLUE}Debug:{colorama.Fore.RESET} {text}")

class logger:
    def __init__(self, type) -> None:
        self._type = None
        if type not in types:
            log_error(f"The type \"{type}\" isn't valid.")
        else:
            self._type = type
        self._counter = None
        self._logs = []
        
    def changeType(self, type: str):
        if type.lower() not in self.types:
            self._type = type.lower()

    def initalizeCount(self):
        if self._counter == None:
            self._counter = 0
        elif self._counter != None:
            log_warn("Counter has already been initalized.")

    def incrementCount(self):
        self._counter += 1

    @property
    def type(self):
        return self._type
    
    @property
    def logs(self):
        return self._logs
    
    @property
    def logCount(self):
        return self._counter

    
    def log(self, text, type='debug'):
        if self._type != None and type != self._type: # if default type is already set
            type = self._type
            
        match type:
            case 'info':
                self.incrementCount()
                log_info(f"{text}", self._counter) # Use f string because data of other types may not be able to print raw
            case 'warning':
                self.incrementCount()
                log_warn(f"{text}", self._counter)
            case 'error':
                self.incrementCount()
                log_error(f"{text}", self._counter)
            case 'debug':
                log_debug(f"{text}")