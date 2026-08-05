import logging

#Record events that happen while the application runs

def configure_logging() -> None:
    logging.basicConfig(
        level = logging.INFO,
        format = "%(asctime)s %(levelname)s %(name)s %(message)s"
    )