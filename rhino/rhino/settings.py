"""
Django settings for rhino project.

Generated by 'django-admin startproject' using Django 1.11.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import configparser
import os
from datetime import timedelta

import configparser

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROD_CONFIG_FOLDER = '/etc/rhino/config'
CONFIG_FILE = 'rhino.ini'
DEFAULT_CONFIG_FOLDER = 'rhino/config'

default_config_full_path = os.path.join(BASE_DIR, DEFAULT_CONFIG_FOLDER, CONFIG_FILE)
prod_config_full_path = os.path.join(PROD_CONFIG_FOLDER, CONFIG_FILE)

config = configparser.ConfigParser()
config.read([default_config_full_path, prod_config_full_path], encoding="utf8")

# PySpider
PYSPIDER_SERVER = config.get('PySpider', 'server')
PYSPIDER_PORT = int(config.get('PySpider', 'port'))

# Rhino server
#RHINO_STREAMING_SERVER = config.get('RhinoStreaming', 'server')
#RHINO_STREAMING_PORT = config.get('RhinoStreaming', 'port')

# Elastic Search Config
ELASTIC_SEARCH_SERVER = config.get('ElasticSearch', 'server')
ELASTIC_SEARCH_PORT = config.get('ElasticSearch', 'port')
ELASTIC_SEARCH_FAIL_INDEX = config.get('ElasticSearch', 'fail.record.index.name')
ELASTIC_SEARCH_FAIL_TYPE = config.get('ElasticSearch', 'fail.record.type.name')
ELASTIC_SEARCH_INSERT_BATCH_SIZE = config.get('ElasticSearch', 'batch.size')
ELASTIC_SEARCH_INSERT_TRY = config.get('ElasticSearch', 'max.retries')

# KAFKA
KAFKA_INSTALL_PATH = config.get('Kafka', 'kafka.install.path')
KAFKA_SERVERS = config.get('Kafka', 'kafka.servers')
KAFKA_SCHEMA_REGISTER_SERVER = config.get('Kafka', 'schema.register.server')
# RHINO Streaming Server
RHINO_SERVER = config.get('RhinoStreaming', 'rhinostreaming.server')

# Backup Server
BACKUP_SERVER_SSH_HOST = config.get('BackupServer', 'backup.server.ssh.host')
BACKUP_SERVER_SSH_PORT = config.get('BackupServer', 'backup.server.ssh.port')
BACKUP_SERVER_SSH_USERNAME = config.get('BackupServer', 'backup.server.ssh.username')
BACKUP_SERVER_SSH_PASSWORD = config.get('BackupServer', 'backup.server.ssh.password')

# RHINO SERVER
RHINO_DATABASE_NAME = config.get('Rhino', 'database.name')
RHINO_DATABASE_USERNAME = config.get('Rhino', 'database.username')
RHINO_DATABASE_PASSWORD = config.get('Rhino', 'database.password')
RHINO_DATABASE_PORT = config.get('Rhino', 'database.port')
RHINO_DATABASE_HOST = config.get('Rhino', 'database.host')

# PYSPIDER SERVER
PYSPIDER_DATABASE_NAME = config.get('Pyspider', 'database.name')
PYSPIDER_DATABASE_USERNAME = config.get('Pyspider', 'database.username')
PYSPIDER_DATABASE_PASSWORD = config.get('Pyspider', 'database.password')
PYSPIDER_DATABASE_PORT = config.get('Pyspider', 'database.port')
PYSPIDER_DATABASE_HOST = config.get('Pyspider', 'database.host')


# Environment
JAVA_HOME = config.get('Env', 'java.home')

# Mysql
MYSQL_HOST = config.get('Mysql', 'host')
MYSQL_DB = config.get('Mysql', 'db')
MYSQL_USER = config.get('Mysql', 'user')
MYSQL_PASSWORD = config.get('Mysql', 'password')

# Manual_Crawler
MANUAL_CRAWLER_URL = config.get('CrawlerInterface','url')
MANUAL_CRAWLER_USERNAME = config.get('CrawlerInterface','username')
MANUAL_CRAWLER_PASSWORD = config.get('CrawlerInterface','password')

# Export
EXPORT_PATH = config.get('Export','export_path')
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0n56d86$ucf)q)e539msklt#p2(mr-kw+ky6#q@ebgzrdak+5#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'web_monitor.apps.WebMonitorConfig',
    'common_utils.apps.CommonUtilsConfig',
    'manual_crawler.apps.ManualCrawlerConfig',
    'django_crontab',
    'monitor.apps.MonitorConfig',
    'crawler_manage.apps.CrawlerManageConfig',
    'rest_framework',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_celery_results'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True
CSRF_COOKIE_SECURE = False
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
#SESSION_COOKIE_SECURE = True
ROOT_URLCONF = 'rhino.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'rhino/templates'), 'VUErhino/dist'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "web_monitor/static"),
    os.path.join(BASE_DIR, "manual_crawler/static"),
    os.path.join(BASE_DIR, "monitor/static"),
    os.path.join(BASE_DIR, "rhino/static"),
    os.path.join(BASE_DIR, "VUErhino/dist/static"),
]

WSGI_APPLICATION = 'rhino.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': RHINO_DATABASE_NAME,
        'USER': RHINO_DATABASE_USERNAME,
        'PASSWORD': RHINO_DATABASE_PASSWORD,
        'HOST': RHINO_DATABASE_HOST,
        'PORT': RHINO_DATABASE_PORT
    },
    'pyspider': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': RHINO_DATABASE_NAME,
        'USER': RHINO_DATABASE_USERNAME,
        'PASSWORD': RHINO_DATABASE_PASSWORD,
        'HOST': RHINO_DATABASE_HOST,
        'PORT': RHINO_DATABASE_PORT
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/etc/rhino/static'

CRONJOBS = [
    ('0 0 * * *', 'monitor.views.cron'),
]

# EMAIL
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_USE_TLS = False
EMAIL_HOST = 'smtp.yscredit.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'automail@yscredit.com'
EMAIL_HOST_PASSWORD = 'y8svUoBf'
DEFAULT_FROM_EMAIL = 'automail@yscredit.com'



# Celery 设置
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'django-db'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Shanghai'

#logging日志配置
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {#日志格式
       'standard': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'}
    },
    'filters': {#过滤器
        'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse',
            }
    },
    'handlers': {#处理器
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console':{#输出到控制台
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
    },
    'loggers': {#logging管理器
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False
        }
    }
}
