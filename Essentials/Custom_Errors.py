# Used for custom error handling -- created to avoid circular imports

class CsvError(Exception):
    pass
class FileError(Exception):
    pass