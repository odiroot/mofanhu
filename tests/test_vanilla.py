from project.vanilla.models import Example


def test_create(db_session):
    instance = Example(name="foo")
    db_session.add(instance)
    db_session.commit()

    assert instance.id
    assert instance.good
