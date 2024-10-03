from typing import Any
from migration_path import MigrationPath


class Migration:
    def __init__(self, migration_id: int, migration_path: MigrationPath, current_location: str, current_date: str, start_date: str, status: str = "Scheduled"):
        self.migration_id = migration_id
        self.migration_path = migration_path
        self.status = status
        self.current_location = current_location
        self.start_date = start_date
        self.current_date = current_date
