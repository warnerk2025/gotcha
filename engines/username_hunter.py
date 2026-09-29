"""Username scanning engine."""


class UsernameHunter:
    """Perform username lookups.

    Platform integrations can be added without changing the command-line
    interface.  An unavailable integration is represented by an empty result.
    """

    async def hunt_general_sites(self, username, include_adult=False):
        return []

    async def hunt_developer_platforms(self, username):
        return []

    async def hunt_forums(self, username):
        return []

    async def hunt_gaming_platforms(self, username):
        return []

    async def hunt_adult_platforms(self, username):
        return []
