"""Application configuration."""


class Config:
    """Container for configuration values shared by the scanners."""

    def __init__(self) -> None:
        self.timeout = 10
        self.threads = 50
