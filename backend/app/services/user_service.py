from ..extensions import db
from ..models.user import User
from sqlalchemy import or_

def create_user(username, password, email, nama):
    u = User(username=username, password=password, email=email, nama=nama)
    db.session.add(u)
    db.session.commit()
    return u

def find_user_by_username_or_email(username=None, email=None, exclude_id=None):
    q = User.query
    conds = []
    if username:
        conds.append(User.username == username)
    if email:
        conds.append(User.email == email)
    if not conds:
        return None
    q = q.filter(or_(*conds))
    if exclude_id:
        q = q.filter(User.id != exclude_id)
    return q.first()

def list_users():
    return User.query.order_by(User.id.asc()).all()

def update_user_by_id(uid, **fields):
    u = User.query.get(uid)
    if not u:
        return False
    for k, v in fields.items():
        setattr(u, k, v)
    db.session.commit()
    return True

def delete_user_by_id(uid):
    u = User.query.get(uid)
    if not u:
        return False
    db.session.delete(u)
    db.session.commit()
    return True
