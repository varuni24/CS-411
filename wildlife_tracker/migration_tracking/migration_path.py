from typing import Optional


class MigrationPath:
    def __init__(self, path_id: int, species: str, start_location: str, destination: str, duration: Optional[int] = None):
        self.path_id = path_id
        self.species = species
        self.start_location = start_location
        self.destination = destination
        self.duration = duration

    def get_migration_path_details(self) -> dict:
        pass

    def update_migration_path_details(self, **kwargs) -> None:
        pass
