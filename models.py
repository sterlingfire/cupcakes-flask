"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DEFUALT_IMAGE = "https://tinyurl.com/demo-cupcake"

def connect_db(app):
    """Connect this database to provided Flask app.

    Called by Flask app.
    """

    db.app = app
    db.init_app(app)

class Cupcake(db.Model):
    """ Cupcake object, extends Model.
    Used for database actions. """

    __tablename__ = "cupcakes"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    image = db.Column(db.Text, default=DEFUALT_IMAGE, nullable=False)

    def serialize(self):
        """ Serialize Object to dictionary. """

        return {
            "id":self.id,
            "flavor":self.flavor,
            "size":self.size,
            "rating":self.rating,
            "image":self.image
        }
