# settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Підключення MongoDB
MONGODB_DATABASES = {
    'default': {
        'name': 'quotes_db',
        'host': 'mongodb+srv://your_mongo_user:your_mongo_password@cluster.mongodb.net/quotes_db',
    }
}
