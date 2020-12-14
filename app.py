"""Flask app for Cupcakes"""

from flask import Flask, render_template, redirect, flash, jsonify
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


@app.route("/api/cupcakes/", methods=["GET"])
def show_cupcake(cupcake_id):
    """ GET: Shows a list of cupcakes.
        POST: adds a cupcake. """

    cupcakes = Cupcake.query.all()
    serialized = [c.serialize() for c in cupcakes]
    return jsonify(cupcakes=serialized)

@app.route("/api/cupcakes/", methods=["POST"])
def show_cupcake(cupcake_id):
    """ GET: Shows a list of cupcakes.
        POST: adds a cupcake. """

    new_cupcake = Cupcake(flavor = request.json['flavor'],
                          size = request.json['size'],
                          rating = request.json['rating'],
                          image = request.json['image'])
    db.session.add(new_cupcake)
    db.session.commit()

    return (jsonify(cupcake=new_cupcake.serialize()), 201)


@app.route("/api/cupcakes/<int:cupcake-id>")
def show_cupcake(cupcake_id):
    """ Shows cupcake details. """

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake=cupcake.serialize())
