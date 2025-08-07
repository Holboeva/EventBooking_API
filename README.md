🎟️ EventBooking API
EventBooking is a Django-based RESTful API that allows users to create, view, and register for events. Authenticated users can organize their own events and register for others'. The API is secured with JWT authentication and provides Swagger documentation for easy testing and integration.

🚀 Getting Started
Follow these steps to set up and run the project locally:

1. Clone the Repository
bash
git clone https://github.com/YOUR_USERNAME/EventBooking_API.git
cd EventBooking_API

2. Create and Activate a Virtual Environment
bash
python -m venv .venv
source .venv/bin/activate        # Linux/macOS
.venv\Scripts\activate           # Windows

3. Install Dependencies
bash
pip install -r requirements.txt

4. Create a .env File (Optional)
Create a .env file in the root directory and add your environment variables:

env
SECRET_KEY=your-django-secret-key
DEBUG=True

5. Apply Migrations
bash
python manage.py makemigrations
python manage.py migrate

6. Create Superuser (Optional – for Admin Panel)
bash
python manage.py createsuperuser

7. Run the Development Server
bash
python manage.py runserver
➡️ Open in browser: http://localhost:8000

⚙️ Tech Stack
Category	Technology
Language	Python 3.12
Framework	Django, Django REST Framework
Auth	JWT (SimpleJWT)
Docs	Swagger (drf-yasg)
Database	SQLite (default), PostgreSQL compatible

📚 API Documentation (Swagger)
Interactive documentation is available via Swagger UI:

🔗 http://localhost:8000/swagger/

🔀 Main API Endpoints
Method	Endpoint	Description	Auth Required
GET	/api/events/	List all events	❌ No
POST	/api/events/	Create a new event	✅ Yes
GET	/api/events/my_events/	View your created events	✅ Yes
POST	/api/registrations/	Register for an event	✅ Yes
GET	/api/registrations/my_registrations/	View your event registrations	✅ Yes
POST	/api/token/	Obtain access & refresh tokens (login)	❌ No

👤 User Roles
Admin / Organizer – Can create and manage events

Authenticated User – Can register for events

Anonymous Visitor – Can only view public events

📁 Project Structure (Example)
bash
EventBooking_API/
├── apps/               # Event model & endpoints
├── root/
├── manage.py
├── requirements.txt
└── README.md

🙋‍♀️ Author
Vazira Holboeva
🎓 Software Engineering Student
📍 Tashkent, Uzbekistan

📫 Email: asmoholboyeva@gmail.com
🔗 GitHub: https://github.com/Holboeva
🔗 LinkedIn: https://www.linkedin.com/in/vazira-holboeva/