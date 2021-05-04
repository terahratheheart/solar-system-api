def test_get_all_planets_with_no_records(client):
    #Act
    response = client.get("/planets")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet(client, two_saved_planets):
    #Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Jupiter",
        "description": "The largest planet.  A gas giant.",
        "pos_from_sun": 5
    }

def test_get_one_planet_with_no_records(client, two_saved_planets):
    #Act
    response = client.get("/planets/4")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 404

def test_get_all_planets(client, two_saved_planets):
    #Act
    response = client.get("/planets")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert response_body == [{
        "id": 1,
        "name": "Jupiter",
        "description": "The largest planet.  A gas giant.",
        "pos_from_sun": 5,
    }, {
        "id": 2,
        "name": "Mercury",
        "description": "The smallest planet.",
        "pos_from_sun": 1
    }]

def test_create_one_planet(client, planet_data):
    response = client.post("/planets", json=planet_data)
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == {
        "success": True,
        "message": "Planet Uranus has been created."
    }
