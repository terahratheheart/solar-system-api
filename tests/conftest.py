import pytest
from app import create_app
from app import db
from app.models.planet import Planet

@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def two_saved_planets(app):
    #Arrange
    jupiter = Planet(name="Jupiter",
                    description="The largest planet.  A gas giant.",
                    pos_from_sun=5)
    mercury = Planet(name="Mercury",
                    description="The smallest planet.",
                    pos_from_sun=1)
    
    db.session.add_all([jupiter, mercury])
    db.session.commit()

@pytest.fixture
def planet_data(app):
    #Arrange
    return {
        "name": "Uranus",
        "description": "It is a blue planet.",
        "pos_from_sun": 7
    }