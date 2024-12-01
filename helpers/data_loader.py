import os.path


class InvalidInputFilePathException(Exception):
    pass


class ProgramData:
    class DataEntry:
        def __init__(self, value, weight):
            self.value = value
            self.weight = weight

        def __str__(self):
            return f"{self.value} {self.weight}"

    def __init__(self):
        self.objects_count: int = 0
        self.storage_size: int = 0
        self.data_set: Array[DataEntry] = []

    def add_entry(self, value: int, weight: int):
        self.data_set.append(self.DataEntry(value, weight))

    def append_entry(self, data_entry: DataEntry):
        self.data_set.append(data_entry)


def load_data(file_path: str):
    file_path = os.path.abspath(file_path)

    file_content = []
    with open(file_path, "r") as file_stream:
        file_content = file_stream.readlines()

    if len(file_content) == 0:
        raise EmptyInputException()

    program_data = ProgramData()
    objects_count, storage_size = file_content[0].split()
    program_data.objects_count = objects_count
    program_data.storage_size = storage_size

    for data_entry in file_content[1:]:
        if not data_entry:
            continue

        item_value, item_weight = data_entry.split()
        program_data.add_entry(item_value, item_weight)

    return program_data
