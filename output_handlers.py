import os
from abc import ABC, abstractmethod


class Writer(ABC):
    @abstractmethod
    def write(self, text: str):
        pass


class FileWriter:
    def __init__(self, path):
        self.path = path

    def write(self, text):
        self.file_path = os.path.dirname(self.path)

        if not os.path.exists(self.file_path) and self.file_path != '':
            os.makedirs(self.file_path)


class TxtWriter(FileWriter):
    def write(self, text):
        super().write(text)
        with open(self.path, mode='a') as destination:
            destination.write(text + '\n')


class CsvWriter(FileWriter):
    def write(self, text):
        super().write(text)
        with open(self.path, mode='a') as destination:
            destination.write(text + ',' + '\n')


class ConsoleWriter:
    def __init__(self, path):
        self.path = path

    def write(self, text):
        print(text)
