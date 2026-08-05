from dataclasses import dataclass
#dataclasses is a python tool for creating classes that mainly store data.


@dataclass(frozen=True)
class Settings:
    app_name: str = "Proposal AI Assistant"
    app_version: str = "0.1.0"
    environment : str = "local"


settings = Settings()

