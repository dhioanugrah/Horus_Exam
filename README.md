# Horus Entry Exam – Fullstack Programmer Internship (Dhio)

## Port yang Digunakan
- **Backend** → http://localhost:5000  
- **Frontend (Vite Dev Server)** → http://localhost:5173  

---

## Persiapan Awal
Sebelum menjalankan project pastikan sudah terpasang:
- **XAMPP** → aktifkan **MySQL**.
- **Python** versi 3.10 atau lebih baru.
- **Node.js** versi 18 atau lebih baru.

---

## Backend Setup
```bash
cd backend
python -m venv .venv
# aktifkan environment
. .venv/Scripts/Activate.ps1
pip install -r requirements.txt
```

### Generate Secret Key
Jalankan Python interaktif:
```bash
python
```
Masukkan:
```python
import secrets
print("SECRET_KEY=", secrets.token_urlsafe(64))
print("JWT_SECRET_KEY=", secrets.token_urlsafe(64))
```
Salin hasilnya ke file `.env`.

###  Setup Database
Gunakan **XAMPP** dan buat database baru di **phpMyAdmin** dengan nama `horus_dhio_db`.

### Jalankan Migration & Server
```bash
set FLASK_APP=run.py
flask db upgrade  
python run.py
```

---

## Endpoint API
| Method | Endpoint | Deskripsi |
|--------|-----------|------------|
| **POST** | `/users/register` | Mendaftarkan pengguna baru |
| **POST** | `/users/login` | Login dan mengembalikan JWT token |
| **GET** | `/users` | Menampilkan semua user (tanpa password) |
| **PUT** | `/users/{id}` | Memperbarui data user |
| **DELETE** | `/users/{id}` | Menghapus user |

> Gunakan header:  
> `Authorization: Bearer <token>`

Cek dahulu respon dari backend di postman untuk memastikan backend tidak ada trouble.

---

## Frontend (Vue 3 + Vite)
```bash
cd ../frontend
copy .env.example .env
# pastikan di .env tertulis:
# VITE_API_URL=http://localhost:5000
npm install
npm run dev
```
Buka di browser:  
http://localhost:5173  

---

## Alur Aplikasi
1. **Login** → masuk ke Dashboard.  
2. **Registrasi** → jika sukses diarahkan ke Login.  
3. **Dashboard** → daftar user, search nama/username, tombol Update & Hapus.  
4. **Update User** → ubah data lalu kembali ke Dashboard.  

---

##  Catatan Teknis
- Password disimpan dalam bentuk hash menggunakan **Werkzeug**.  
- CORS aktif untuk pengujian antar port.  
- Migration menggunakan **Flask-Migrate** & **Alembic** (`migrations/0001_init_users.py`).  
- Struktur tabel utama:
  ```
  users(
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE,
    password VARCHAR(255),
    email VARCHAR(100) UNIQUE,
    nama VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
  )
  ```

---


## Catatan Akhir
Proyek ini dibangun dengan pendekatan modular menggunakan **Flask (Python)** untuk backend dan **Vue 3 (Vite)** untuk frontend.  
Struktur kode disusun agar mudah dibaca dan dikembangkan lebih lanjut sesuai praktik terbaik fullstack development.
