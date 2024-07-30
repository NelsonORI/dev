from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    quote = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), default='pending')
    details = db.Column(db.JSON, nullable=False)

class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    home_type = db.Column(db.String(50), nullable=False)
    item_name = db.Column(db.String(100), nullable=False)
