from abc import ABC, abstractmethod


class Option(ABC):
    @abstractmethod
    def getDestinations(self) -> list:
        pass


class CfgFileOption:
    def __init__(self):
        pass

    def getDestinations(self):
        with open('cfg.txt') as cfg:
            destinations = cfg.read().splitlines()
        return destinations


class ConsoleInputOption:
    def __init__(self):
        pass

    def getDestinations(self):
        destinations = []
        answer = ''
        print("Enter 'end', if you want to stop")
        while answer != 'end':
            answer = str(input("Path to file: "))
            destinations.append(answer)
        return destinations
