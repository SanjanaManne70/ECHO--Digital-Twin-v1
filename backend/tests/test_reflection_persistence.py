from app.agents.reflection_persistence import ReflectionPersistence


class FakeReflection:
    def __init__(self):
        self.content = "old reflection"
        self.needs_refresh = True


class FakeRepository:

    def __init__(self, reflection=None):
        self.reflection = reflection
        self.updated = None
        self.created = None

    def get_by_date(self, db, user_id, day):
        return self.reflection

    def update(self, db, reflection):
        self.updated = reflection
        return reflection

    def create(self, db, reflection):
        self.created = reflection
        return reflection


def test_updates_existing_reflection():

    reflection = FakeReflection()
    repo = FakeRepository(reflection=reflection)

    persistence = ReflectionPersistence(
        repository=repo
    )

    result = persistence.save(
        db="fake-db",
        user_id=1,
        content="new reflection",
    )

    assert result is reflection
    assert reflection.content == "new reflection"
    assert reflection.needs_refresh is False
    assert repo.updated is reflection


def test_creates_new_reflection():

    repo = FakeRepository()

    persistence = ReflectionPersistence(
        repository=repo
    )

    result = persistence.save(
        db="fake-db",
        user_id=1,
        content="first reflection",
    )

    assert result is repo.created
    assert result.user_id == 1
    assert result.content == "first reflection"
    assert result.needs_refresh is False