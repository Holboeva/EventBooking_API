# 🎫 Event Booking API

Event Booking API — bu RESTful API bo‘lib, foydalanuvchilar tadbir (event)lar tashkil qilishi va boshqa foydalanuvchilar ularni ko‘rib ro‘yxatdan o‘tishi mumkin. API JWT token orqali autentifikatsiyani qo‘llaydi.

---

## 🔧 Texnologiyalar

- **Python 3.12**
- **Django**
- **Django REST Framework**
- **Simple JWT** – Token asosida autentifikatsiya
- **SQLite (yoki PostgreSQL)** – Ma’lumotlar bazasi

---

## 🚀 Loyihani ishga tushirish

```bash
# 1. Repozitoriyani klonlang
git clone https://github.com/your-username/EventBooking_API.git
cd EventBooking_API

# 2. Virtual environment yaratish va aktivlashtirish
python3 -m venv .venv
source .venv/bin/activate

# 3. Kutubxonalarni o‘rnatish
pip install -r requirements.txt

# 4. Migratsiyalarni bajarish
python manage.py makemigrations
python manage.py migrate

# 5. Superuser yaratish
python manage.py createsuperuser

# 6. Serverni ishga tushirish
python manage.py runserver
