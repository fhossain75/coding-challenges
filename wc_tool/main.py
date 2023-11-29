import sys  # todo: Use argparse
from commands import *

# Error handling: Incorrect input
if len(sys.argv) < 3:
    raise ValueError("File name not provided.")
    sys.exit(1)

command, file_name = sys.argv[1], sys.argv[2]

command_map = {
    '-c': lambda: byte_counter(file_name),
    '-l': lambda: line_counter(file_name),
    '-w': lambda: byte_counter(file_name),
    '-m': lambda: byte_counter(file_name)
}

# Call the appropriate function based on the command
if command in command_map:
    print(command_map[command]())
else:
    print("Invalid command. Please choose from -c, -l, -w, -m.")
