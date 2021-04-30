from flask import Blueprint, request, make_response
from flask import jsonify
from app import db
from app.models.planet import Planet

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET", "POST"])
def handle_planets():
    if request.method == "GET":
        planets = Planet.query.all()
        planets_response = []

        for planet in planets:
            planets_response.append({
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "pos_from_sun": planet.pos_from_sun
            })
        
        return jsonify(planets_response), 200
    elif request.method == "POST":
        request_body = request.get_json()
        new_planet = Planet(name=request_body["name"], description=request_body["description"], pos_from_sun=request_body["pos_from_sun"])

        db.session.add(new_planet)
        db.session.commit()

        return {
            "success": True,
            "message": f"Planet {new_planet.name} has been created."

        }, 201

@planets_bp.route("/<planet_id>", methods=["GET"])
def handle_planet(planet_id):
    planet = Planet.query.get(planet_id)

    if planet:
        return {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "pos_from_sun": planet.pos_from_sun
        }, 200
    
    return {
        "message": "That's not a planet!",
        "success": False,
    }, 404
