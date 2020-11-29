from app import db
from datetime import datetime

class Data(db.Model):
    __tablename__ = "data"

    id = db.Column(db.Integer,primary_key=True)
    temperature = db.Column(db.Float)
    humidity = db.Column(db.Float)
    timestamp = db.Column(db.DateTime,default=datetime.now)

    def to_json(self):
        json_data = {
                'id': self.id,
                'temperature': self.temperature,
                'humidity': self.humidity,
                'timestamp': self.timestamp,
            }
        return json_data

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __str__(self):
        return self.to_json()
