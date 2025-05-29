# Used for custom error handling -- created to avoid circular imports


class CsvError(Exception):    # Raised in check_database_content.py when the csv database content is corrupted.
    pass

