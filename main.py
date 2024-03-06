from output_handlers import CsvWriter, TxtWriter, ConsoleWriter

with open('cfg.txt') as cfg:
    destinations = cfg.read().splitlines()

writers = []

for destination in destinations:
    if destination[-3:] == 'txt':
        writers.append(TxtWriter(destination))
    elif destination[-3:] == 'csv':
        writers.append(CsvWriter(destination))
    elif destination == 'console':
        writers.append(ConsoleWriter(destination))

while True:
    userInput = input('Enter data, you want to proceed: ')

    for writer in writers:
        writer.write(userInput)

