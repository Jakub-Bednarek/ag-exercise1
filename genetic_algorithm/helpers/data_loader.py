import os.path


class EmptyInputException(Exception):
    pass


class DataEntry:
    def __init__(self, value: float, weight: float):
        self.value: float = value
        self.weight: float = weight

    def __str__(self) -> str:
        return f"{self.value} {self.weight}"

    def __repr__(self) -> str:
        return str(self)


class ProgramData:
    def __init__(self):
        self.backpack_entries_count: int = 0
        self.storage_size: float = 0.0
        self.backpack_entries: Array[DataEntry] = []

    def add_entry(self, value: float, weight: float):
        self.backpack_entries.append(DataEntry(value, weight))

    def append_entry(self, data_entry: DataEntry):
        self.backpack_entries.append(data_entry)


def load_data(file_path: str) -> ProgramData:
    file_path = os.path.abspath(file_path)

    file_content = []
    with open(file_path, "r") as file_stream:
        file_content = file_stream.readlines()

    if len(file_content) == 0:
        raise EmptyInputException()

    program_data = ProgramData()
    objects_count, storage_size = file_content[0].split()
    program_data.backpack_entries_count = int(objects_count)
    program_data.storage_size = float(storage_size)

    for data_entry in file_content[1:]:
        if not data_entry:
            continue

        item_value, item_weight = data_entry.split()
        program_data.add_entry(float(item_value), float(item_weight))

    return program_data
