import os


def byte_counter(file_name):

    file_path = os.getcwd() + '/' + file_name

    if not os.path.isfile(file_path):
        raise ValueError("Error: File does not exist.")
        sys.exit(1)

    return f"{os.path.getsize(file_path)} {file_name}"
