from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Airport(db.Model):

    __tablename__ = 'airports'

    unique_id = db.Column(db.Integer, primary_key=True)
    ident = db.Column("ident", db.String(5))
    type_class = db.Column("type", db.String(64))
    name = db.Column("name", db.String(200))
    coordinates = db.Column("coordinates", db.String(100))
    elevation_ft = db.Column("elevation", db.Integer)
    continent = db.Column("continent", db.String(2))
    iso_country = db.Column("iso_country", db.String(3))
    iso_region = db.Column("iso_region", db.String(100))
    municipality = db.Column("municipality", db.String(100))
    gps_code = db.Column("gps_code", db.String(100))
    iata_code = db.Column("iata_code", db.String(3), unique=True)
    local_cod = db.Column("local_cod", db.String(100))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
