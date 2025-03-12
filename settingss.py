DATABASES = {
    "default": {  # PostgreSQL для користувачів
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "your_db_name",
        "USER": "your_db_user",
        "PASSWORD": "your_db_password",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

# MongoDB для цитат і авторів
from mongoengine import connect

connect(
    db="quotes_db",
    username="your_mongo_user",
    password="your_mongo_password",
    host="mongodb+srv://your_mongo_host"
)
