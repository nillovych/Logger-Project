from output_handlers import CsvWriter, TxtWriter, ConsoleWriter
from setup_options import Option


class Logger:
    def __init__(self, option: Option):

        self.writers = self._getWriters(option)

    def log(self, user_input: str):

        for writer in self.writers:
            writer.write(user_input)

    def _getWriters(self, option: Option):

        writers = []

        destinations = option.getDestinations()

        for destination in destinations:
            if destination[-3:] == 'txt':
                writers.append(TxtWriter(destination))
            elif destination[-3:] == 'csv':
                writers.append(CsvWriter(destination))
            elif destination == 'console':
                writers.append(ConsoleWriter(destination))

        return writers
