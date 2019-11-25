def test_smoke(app):
    assert app.config["TESTING"]


def test_database(db_engine, db_session):
    with db_engine.begin() as conn:
        assert conn.execute("SELECT NOW()").fetchone()
    db_session.commit()
