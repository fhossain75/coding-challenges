import os


def byte_counter(file_name):

    file_path = os.getcwd() + '/' + file_name

    # todo: Add error handling: "file doesn't exist"
    if not os.path.isfile(file_path):
        pass

    return f"{os.path.getsize('d:/file.jpg')} {file_name}"
