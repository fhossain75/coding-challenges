import argparse
from commands import byte_counter

parser = argparse.ArgumentParser()
parser.add_argument('command', type=str, help='')
parser.add_argument('filename', type=str, help='')
args = parser.parse_args()

print(args.command, args.filename)

command_map = {
    '-c': lambda: byte_counter(args.filename),
    '-l': lambda: byte_counter(args.filename),
    '-w': lambda: byte_counter(args.filename),
    '-m': lambda: byte_counter(args.filename)
}

# Call the appropriate function based on the command
if args.command in command_map:
    result = command_map[args.command]()
    print(result)
else:
    print("Invalid command. Please choose from -c, -l, -w, -m.")


