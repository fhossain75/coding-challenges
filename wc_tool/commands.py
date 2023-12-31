import os


# todo: add method header
def byte_counter(file_name):
    file_path = os.getcwd() + '/' + file_name

    if not os.path.isfile(file_path):
        raise ValueError("Error: File does not exist.")
        sys.exit(1)

    return f"{os.path.getsize(file_path)} {file_name}"


def line_counter(file_name):
    file_path = os.getcwd() + '/' + file_name

    with open(file_path, 'r') as f:
        return f"{len(f.readlines())} {file_name}"


def word_counter(file_name):
    file_path = os.getcwd() + '/' + file_name

    words = []
    with open(file_path, 'r') as f:
        for line in f:
            words += line.strip().split()

    return f"{len(words)} {file_name}"


def character_counter(file_name):
    file_path = os.getcwd() + '/' + file_name

    characters = []
    with open(file_path, 'r') as f:
        for line in f:
            for word in line.split():
                characters += list(word)

    return f"{len(characters)} {file_name}"
