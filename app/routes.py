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

        return jsonify({
            "success": True,
            "message": f"Planet {new_planet.name} has been created."

        }), 201

@planets_bp.route("/<planet_id>", methods=["GET", "PUT", "DELETE"])
def handle_planet(planet_id):
    planet = Planet.query.get(planet_id)

    if planet == None:
        return jsonify({
        "message": "That's not a planet!",
        "success": False,
        }), 404

    elif request.method == "GET":
        return jsonify({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "pos_from_sun": planet.pos_from_sun
        }), 200

    elif request.method == "PUT":
        form_data = request.get_json()

        planet.name = form_data["name"]
        planet.description = form_data["description"]
        planet.pos_from_sun = form_data["pos_from_sun"]
        db.session.commit()

        return jsonify({"message": f"Planet with id {planet_id} has been updated",
        "success": True}), 200

    elif request.method == "DELETE":
        db.session.delete(planet)
        db.session.commit()
        return jsonify({"message": f"Planet with id {planet_id} has been deleted",
        "success": True}), 200
    

