from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required
from werkzeug.security import generate_password_hash, check_password_hash
from ..extensions import db
from ..models.user import User
from ..services.user_service import (
    create_user, find_user_by_username_or_email,
    list_users, update_user_by_id, delete_user_by_id
)
from ..utils.validators import is_valid_email

bp = Blueprint("users", __name__)

@bp.post("/register")
def register():
    data = request.get_json() or {}
    required = ["username", "password", "email", "nama"]
    if not all(k in data and str(data[k]).strip() for k in required):
        return jsonify(message="Field wajib diisi"), 400

    if not is_valid_email(data["email"]):
        return jsonify(message="Format email tidak valid"), 400

    if find_user_by_username_or_email(data["username"], data["email"]):
        return jsonify(message="Username atau email sudah terpakai"), 409

    hashed = generate_password_hash(data["password"])
    create_user(username=data["username"], password=hashed,
                email=data["email"], nama=data["nama"])
    return jsonify(message="Registrasi berhasil"), 201


@bp.post("/login")
def login():
    data = request.get_json() or {}
    if not data.get("username") or not data.get("password"):
        return jsonify(message="Username dan password wajib"), 400

    user = User.query.filter_by(username=data["username"]).first()
    if not user or not check_password_hash(user.password, data["password"]):
        return jsonify(message="Username atau password salah"), 401

    token = create_access_token(identity=str(user.id))
    return jsonify(message="Login berhasil", token=token), 200


@bp.get("")
@jwt_required()
def get_users():
    users = list_users()
    return jsonify([u.to_dict_public() for u in users]), 200


@bp.put("/<int:user_id>")
@jwt_required()
def update_user(user_id):
    payload = request.get_json() or {}
    allowed = {"username", "email", "nama"}
    data = {k: v for k, v in payload.items() if k in allowed}

    if "email" in data and not is_valid_email(data["email"]):
        return jsonify(message="Format email tidak valid"), 400

    # cek unik
    if "username" in data or "email" in data:
        exists = find_user_by_username_or_email(
            data.get("username"), data.get("email"), exclude_id=user_id
        )
        if exists:
            return jsonify(message="Username atau email sudah terpakai"), 409

    ok = update_user_by_id(user_id, **data)
    if not ok:
        return jsonify(message="User tidak ditemukan"), 404
    return jsonify(message="Data user berhasil diperbarui"), 200


@bp.delete("/<int:user_id>")
@jwt_required()
def delete_user(user_id):
    ok = delete_user_by_id(user_id)
    if not ok:
        return jsonify(message="User tidak ditemukan"), 404
    return jsonify(message="User berhasil dihapus"), 200
