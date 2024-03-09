# Logger

Logger is a program designed to take user input from the console and log it to different destinations, specified in the configuration file "cfg.txt" or entered from console.

## Functionality

The program supports logging to different destinations based on the configuration specified in "cfg.txt". Supported destination types include:

- **.txt**: Append log as a new line in a text file.
- **.csv**: Append log using comma (,) as a separator in a CSV file.
- **console**: Log to the console.

## Configuration

The configuration file "cfg.txt" specifies the destination type where the logs will be recorded. Each line in the configuration file represents a separate destination type.

Example content of "cfg.txt":

