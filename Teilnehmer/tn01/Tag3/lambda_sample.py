def read_from_file(file_name: str, filter: Callable=None):
    with open(file_name) as file_dispatcher:
        for line in file_dispatcher:
            if filter and filter(line):
                result = filter