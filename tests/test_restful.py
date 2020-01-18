from flask.helpers import url_for

from project.vanilla.models import Example


def test_index(client):
    response = client.get(url_for("restful.index"))
    assert response.status_code == 200
    assert response.is_json
    assert response.json == {"message": "Hello world"}


def test_get_example_list(db_session, client):
    db_session.add_all(
        [Example(name="foo", good=True), Example(name="bar", good=False)]
    )

    response = client.get(url_for("restful.examplelist"))
    assert response.status_code == 200
    assert len(response.json) == 2

    assert response.json[0]["name"] == "foo"
    assert response.json[1]["name"] == "bar"


def test_create_example(db_session, client):
    response = client.post(
        url_for("restful.examplelist"), json={"name": "ham", "good": False}
    )
    assert response.status_code == 201

    result = Example.query.all()
    assert len(result) == 1
    assert result[0].name == "ham"
