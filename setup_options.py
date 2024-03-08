from abc import ABC, abstractmethod


class Option(ABC):
    @abstractmethod
    def getDestinations(self) -> list:
        pass


class CfgFileOption(Option):
    def __init__(self):
        pass

    def getDestinations(self):
        with open('cfg.txt') as cfg:
            self.destinations = cfg.read().splitlines()
        return self.destinations


class ConsoleInputOption(Option):
    def __init__(self):
        pass

    def getDestinations(self):
        self.destinations = []
        answer = ''
        print("Enter 'end', if you want to stop")
        while answer != 'end':
            answer = str(input("Path to file: "))
            self.destinations.append(answer)
        return self.destinations
