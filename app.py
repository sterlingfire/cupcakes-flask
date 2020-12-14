"""Flask app for Cupcakes"""

from flask import Flask, render_template, redirect, flash, jsonify, request
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///cupcakes"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
toolbar = DebugToolbarExtension(app)


connect_db(app)
db.create_all()

@app.route("/")
def show_index_page():
    """ Shows index page. """
    return render_template("index.html")


@app.route("/api/cupcakes", methods=["GET"])
def show_all_cupcakes():
    """ GET: Shows a list of cupcakes.
        returns {cupcakes: [{id, flavor, size, rating, image}, ...]}"""

    cupcakes = Cupcake.query.all()
    serialized = [c.serialize() for c in cupcakes]
    return jsonify(cupcakes=serialized)

@app.route("/api/cupcakes", methods=["POST"])
def create_new_cupcake():
    """ POST: adds a cupcake.
    returns {cupcake: {id, flavor, size, rating, image}}"""

    new_cupcake = Cupcake(flavor = request.json['flavor'],
                          size = request.json['size'],
                          rating = request.json['rating'],
                          image = request.json['image'])
    db.session.add(new_cupcake)
    db.session.commit()

    return (jsonify(cupcake=new_cupcake.serialize()), 201)


@app.route("/api/cupcakes/<int:cupcake_id>")
def show_cupcake_details(cupcake_id):
    """ Shows cupcake details.
    returns {cupcake: {id, flavor, size, rating, image}} """

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake=cupcake.serialize())


@app.route("/api/cupcakes/<int:cupcake_id>", methods=["PATCH"])
def update_cupcake_details(cupcake_id):
    """ Updates cupcake details.
        Return {cupcake: {id, flavor, size, rating, image}}. """
    cupcake = Cupcake.query.get_or_404(cupcake_id)

    print('cupcake', cupcake)
    data = request.json

    print('data', data)


    cupcake.flavor = data["flavor"]
    cupcake.size = data["size"]
    cupcake.rating = data["rating"]
    cupcake.image = data["image"]
    db.session.commit()

    return jsonify(cupcake=cupcake.serialize())


@app.route("/api/cupcakes/<int:cupcake_id>", methods=["DELETE"])
def delete_cupcake(cupcake_id):
    """ DELETES cupcake.
        Return {message: 'Deleted'}. """
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    db.session.delete(cupcake)
    return jsonify(message="Deleted")
