"""Logging setup."""

import logging


def setup_logger() -> logging.Logger:
    """Return the application logger with a useful default configuration."""
    logger = logging.getLogger("gotcha")
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
        logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger
