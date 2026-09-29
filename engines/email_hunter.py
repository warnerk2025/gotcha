"""Email scanning engine."""


class EmailHunter:
    """Perform email lookups while keeping network integrations optional."""

    async def hunt_social_accounts(self, email):
        return []

    async def hunt_professional_accounts(self, email):
        return []

    async def analyze_domain(self, email):
        return {"domain": email.rsplit("@", 1)[1]}

    async def close_session(self):
        return None
