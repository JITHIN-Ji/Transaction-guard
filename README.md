💳 Fraud Detection System using Django & ML
This project is a Django web application integrated with a machine learning model to detect fraudulent transactions. Users can register, log in, and submit transaction data to receive real-time fraud analysis.

🚀 Features
👥 User & Admin login system

📝 User registration form

📊 Fraud detection using pre-trained ML model

✅ Classifies transactions as Fraud or Genuine

📦 Uses pandas and sklearn under the hood

🖼️ Frontend built using Django templates

📁 Project Structure
bash
Copy
Edit
detection/
│
├── migrations/
├── templates/
│   ├── detection/index.html
│   ├── login.html
│   ├── register.html
│   ├── userhome.html
│   ├── adminhome.html
├── __init__.py
├── views.py
├── models.py
├── forms.py
├── urls.py
├── model/                 # Contains ML model and label encoder
│   ├── model.pkl
│   └── label_encoder.pkl
🛠 Tech Stack
Backend: Django (Python)

Frontend: HTML, CSS (Django Templates)

ML Framework: scikit-learn

Database: SQLite (default Django DB)

🧠 ML Prediction Logic
Input Features:

Amount

Transaction Date (converted to timestamp)

Transaction Type (encoded with label_encoder)

Output:

Model returns 1 for Fraud and 0 for Genuine

Uses a pre-trained ML model stored in model.pkl

🔐 Authentication
Admin and user login system

Users can register through a custom registration form

Session-based login with request.session


How to Run
1. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
2. Apply Migrations
bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
3. Create Superuser (Optional)
bash
Copy
Edit
python manage.py createsuperuser
4. Run Server
bash
Copy
Edit
python manage.py runserver
Visit: http://127.0.0.1:8000/

