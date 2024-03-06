from output_handlers import CsvWriter, TxtWriter, ConsoleWriter
from setup_options import CfgFileOption, ConsoleInputOption

answer = int(input('Do you want to import destinations from cfg.txt(Enter 0) or write your own(Enter 1): '))

if answer == 0:
    choosen_option = CfgFileOption()
elif answer == 1:
    choosen_option = ConsoleInputOption()

destinations = choosen_option.getDestinations()

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
