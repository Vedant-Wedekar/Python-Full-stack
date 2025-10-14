🧩 Step 1: Install uv
pip install uv

🧩 Step 2: Add the folder to PATH
Press Windows + R, type:
sysdm.cpl

In the System Properties window, go to:
Advanced → Environment Variables

Under User variables for ASUS, find the variable named Path, then click Edit.

Click New, and paste this exact line:

C:\Users\ASUS\AppData\Roaming\Python\Python313\Scripts

Click OK → OK → OK to save


⚙️ Step 3: (If it still doesn’t show)
uv --version

⚙️ Step 4:
cd "C:\Users\ASUS\OneDrive\Desktop\MCA\Python-Full-stack\my_django_app"

# Create virtual environment
uv venv

# Activate it
.venv\Scripts\activate

# Install Django
uv pip install django

# Create your project
django-admin startproject core .

# Run server
uv run python manage.py runserver

