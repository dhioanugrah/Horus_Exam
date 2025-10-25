from datetime import datetime
from ..extensions import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)  # hashed
    email = db.Column(db.String(100), unique=True, nullable=False)
    nama = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def to_dict_public(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "nama": self.nama,
            "created_at": self.created_at.isoformat()
        }
