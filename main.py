from output_handlers import CsvWriter, TxtWriter, ConsoleWriter

answer1 = int(input('Do you want to import destinations from cfg.txt(Enter 0) or write your own(Enter 1): '))

if answer1 == 0:
    with open('cfg.txt') as cfg:
        destinations = cfg.read().splitlines()
elif answer1 == 1:
    destinations = []
    answer2 = ''
    print("Enter 'end', if you want to stop")
    while answer2 != 'end':
        answer2 = str(input("Path to file: "))
        destinations.append(answer2)
else:
    print('Choices are 0 and 1')

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

