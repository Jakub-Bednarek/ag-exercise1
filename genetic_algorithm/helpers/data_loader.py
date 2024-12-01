import os.path


class DataEntry:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    def __str__(self):
        return f"{self.value} {self.weight}"


class ProgramData:
    def __init__(self):
        self.entries_count: int = 0
        self.storage_size: int = 0
        self.backpack_entries: Array[DataEntry] = []

    def add_entry(self, value: int, weight: int):
        self.backpack_entries.append(DataEntry(value, weight))

    def append_entry(self, data_entry: DataEntry):
        self.backpack_entries.append(data_entry)


def load_data(file_path: str):
    file_path = os.path.abspath(file_path)

    file_content = []
    with open(file_path, "r") as file_stream:
        file_content = file_stream.readlines()

    if len(file_content) == 0:
        raise EmptyInputException()

    program_data = ProgramData()
    objects_count, storage_size = file_content[0].split()
    program_data.entries_count = int(objects_count)
    program_data.storage_size = int(storage_size)

    for data_entry in file_content[1:]:
        if not data_entry:
            continue

        item_value, item_weight = data_entry.split()
        program_data.add_entry(int(item_value), int(item_weight))

    return program_data
