"""Input validation helpers."""

import re


class Validator:
    """Validate user-provided targets."""

    _EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

    @classmethod
    def is_valid_email(cls, email):
        return bool(cls._EMAIL_PATTERN.fullmatch(email))
