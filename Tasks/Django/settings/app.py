# BASE_DIR = Path(__file__).resolve().parent.parent--------------------------Projectimiz hansi DIR yerde oldugunu gosteir.

# SECRET_KEY = 'django-insecure-o3s3*)7gzcg+)1%is7ss4oe7f@idn_a3$1t7^8kt929$l$iq12'-------------------------- Sitenin tehlukesizlyi ucundur.

# DEBUG = True-----------------------Butun sehvleri gosterir.

# ALLOWED_HOSTS = [] ------------------Istenilen Host verilir.


# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'app',
# ]--------------------------------------------------------------------Butun appler burda yaradilir.Meslen, 'app'

# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]----------------------------------------------------------------------------Requestnen responsu tezimleyir.



# ROOT_URLCONF = 'Site.urls'-------------------------------Proyektin  urls.py gosderir


# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': ['templates'],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]---------------------------------------------DIRS htmlde templates hissesi olur.




# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }---------------------------------------------DATABASES uzerinde default olaraq gelen sqlite-dir.


# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]--------------------------------Code guvenli olur.



# STATIC_URL = '/static/'-------------------------------- Turaq ki bizim saytin sekilerin istifade edirler amma biz isteyin qarsini alir.