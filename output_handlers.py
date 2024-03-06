class Txt:
    @staticmethod
    def output(text, filePath, fileName):
        with open(filePath + fileName, mode='a') as destination:
            destination.write(text + '\n')

class Csv:
    @staticmethod
    def output(text, filePath, fileName):
        with open(filePath + fileName, mode='a') as destination:
            destination.write(text + ',' + '\n')

class Console:
    @staticmethod
    def output(text):
        print(text)