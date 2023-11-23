import colorama

# Yes, you can use these functions without the need of creating
# a logger instance, but creating a logger instance provides additional functionality
# Some of these features include logs being stored, counting amount of logs, setting a default type, etc.

types = []

def log_info(text, counter):
    if counter == None:   
        print(f"{colorama.Fore.GREEN}Info:{colorama.Fore.RESET} {text}")
    elif counter != None:
        print(f"{colorama.Fore.GREEN}Info | {counter}:{colorama.Fore.RESET} {text}")

def log_warn(text, counter):
    if counter == None:
        print(f"{colorama.Fore.YELLOW}Warning:{colorama.Fore.RESET} {text}")
    elif counter != None:
        print(f"{colorama.Fore.GREEN}Warning | {counter}:{colorama.Fore.RESET} {text}")

def log_error(text, counter):
    if counter == None:
        print(f"{colorama.Fore.RED}Error:{colorama.Fore.RESET} {text}")
    elif counter != None:
        print(f"{colorama.Fore.GREEN}Error | {counter}:{colorama.Fore.RESET} {text}")

def log_debug(text):
    print(f"{colorama.Fore.BLUE}Debug:{colorama.Fore.RESET} {text}")

class logger:
    def __init__(self, type) -> None:
        self._type = type
        self._counter = None
        self._logs = []
        
    def attachCounter(self, counterVar: int):
        counter = self._counter
        if counter == None:
            counter = counterVar
        elif counter != None:
            log_warn("Data is already set in the counter variable")
    
    def changeType(self, type: str):
        if type.lower() == "info" or type.lower() == "warning" or type.lower() == "error" or type.lower() == "debug":
            self._type = type.lower()

    @property
    def type(self):
        return self._type
    
    @property
    def logs(self):
        return self._logs
    
    @property
    def counts(self):
        return self._counter

    
    def log(self, text, type='debug'):
        if self._type != None and type != self._type: # if default type is already set
            type = self._type
        match type:
            case 'info':
                log_info(f"{text}", self._counter) # Use f string because data of other types may not be able to print raw
            case 'warning':
                log_warn(f"{text}", self._counter)
            case 'error':
                log_error(f"{text}", self._counter)
            case 'debug':
                log_debug(f"{text}")