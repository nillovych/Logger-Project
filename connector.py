from output_handlers import Console, Csv, Txt
import os


class Connector:
    def __init__(self, inputValue):

        self.inputValue = inputValue
        cfgSeparated = self.readFile()

        for i in range(len(cfgSeparated)):
            self.connect(cfgSeparated[i])

    def connect(self, method):
        if method == 'console':
            Console.output(self.inputValue)

        else:
            PreparePath(method[-3:], method, self.inputValue)

    def readFile(self):
        with open('cfg.txt') as cfg:
            return cfg.read().splitlines()

class PreparePath:
    def __init__(self, type, fullName, inputValue):

        self.inputValue = inputValue
        filePath, fileName = self.pathCorrection(fullName)
        checker = self.checkForDirectory(self.filePath)

        if checker:
            if type == 'txt':
                Txt.output(self.inputValue, filePath, fileName)
            elif type == 'csv':
                Csv.output(self.inputValue, filePath, fileName)

        else:
            print(f'Incorrect path "{self.filePath}", file <{self.fileName}> cannot be saved!')

    def pathCorrection(self, fullTitle):
        last_slash_pos = fullTitle.rfind('/')

        if last_slash_pos != -1:
            filePath = fullTitle[0:last_slash_pos + 1]
            fileName = fullTitle[last_slash_pos + 1:]
            return (filePath, fileName)

        else:
            return ('', fullTitle)

    def checkForDirectory(self, directoryPath):
        self.directoryPath = directoryPath

        try:
            if self.directoryPath == '':
                return True
            elif not os.path.exists(self.directoryPath):
                os.makedirs(self.directoryPath)
                return True
            else: return True

        except OSError:
            return False