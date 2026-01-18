from app import db
from datetime import datetime

class Car(db.Model):
    __tablename__ = 'cars'
    
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    plate_number = db.Column(db.String(20), unique=True, nullable=False)
    status = db.Column(db.String(20), default='Pending') # Pending, In Progress, Ready
    owner_name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Car {self.plate_number}>'

