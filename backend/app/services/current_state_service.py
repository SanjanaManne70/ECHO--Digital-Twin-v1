from app.models.current_state import CurrentState


class CurrentStateService:

    DEFAULT_STATES = [
        ("Sleep", 50),
        ("Energy", 50),
        ("Mood", 50),
        ("Learning", 50),
    ]

    def initialize(
        self,
        db,
        user_id,
    ):

        for domain, value in self.DEFAULT_STATES:

            db.add(
                CurrentState(
                    user_id=user_id,
                    domain=domain,
                    value=value,
                )
            )

        db.commit()