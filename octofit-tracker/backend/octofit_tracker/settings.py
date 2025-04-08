# Add MongoDB database configuration
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'octofit_db',
        'HOST': 'localhost',
        'PORT': 27017,
    }
}

# Add installed apps
INSTALLED_APPS += [
    'rest_framework',
    'corsheaders',
    'tracker',
]

# Add middleware for CORS
MIDDLEWARE += [
    'corsheaders.middleware.CorsMiddleware',
]

# Allow all origins for CORS
CORS_ALLOW_ALL_ORIGINS = True

# Allow all hosts
ALLOWED_HOSTS = ['*']