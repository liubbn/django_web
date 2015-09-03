#coding=utf-8
"""
Django settings for myproject project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
DJ_PROJECT_DIR = os.path.dirname(__file__)
BASE_DIR = os.path.dirname(DJ_PROJECT_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!iudke*hi8vo#qyntq5yxm+p2itkuqg-m@bo8o%+cbnq(h%@@-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# GETTING-STARTED: change 'myproject' to your project name:
ROOT_URLCONF = 'myproject.urls'

WSGI_APPLICATION = 'myproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        # GETTING-STARTED: change 'db.sqlite3' to your sqlite3 database:
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


#####
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'blog.views.global_setting',
            ],
        },
    },
]




# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'zh_cn'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static')

###
MEDIA_URL = '/uploads/'
MEDIA_ROOT = os.path.join(BASE_DIR,'uploads')

### Log####
LOGGING = {
    'version': 1,#指明dictConnfig的版本，目前就只有一个版本，哈哈
    'disable_existing_loggers': True,#禁用所有的已经存在的日志配置
    'formatters': {#格式器
        'verbose': {#详细
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {#简单
            'format': '%(levelname)s %(message)s'
        },
    },
    #===========================================================================
    # 'filters': {#过滤器
    #     'special': {#使用project.logging.SpecialFilter，别名special，可以接受其他的参数
    #         '()': 'project.logging.SpecialFilter',
    #         'foo': 'bar',#参数，名为foo，值为bar
    #     }
    # },
    #===========================================================================
    'handlers': {#处理器，在这里定义了三个处理器
        'null': {#Null处理器，所有高于（包括）debug的消息会被传到/dev/null
            'level':'DEBUG',
            'class':'django.utils.log.NullHandler',
        },
        'console':{#流处理器，所有的高于（包括）debug的消息会被传到stderr，使用的是simple格式器
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {#AdminEmail处理器，所有高于（包括）而error的消息会被发送给站点管理员，使用的是special格式器
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
           # 'filters': ['special']
        },
         'file':{#流处理器，所有的高于（包括）debug的消息会被传到stderr，使用的是simple格式器
            'level':'INFO',
            'class':'logging.FileHandler',
            'formatter': 'simple',
            'filename' : os.path.join(BASE_DIR,'log/views.log') ,
        },
    },
    'loggers': {#定义了三个记录器
        'django': {#使用null处理器，所有高于（包括）info的消息会被发往null处理器，向父层次传递信息
            'handlers':['null'],
            'propagate': True,
            'level':'INFO',
        },
        'django.request': {#所有高于（包括）error的消息会被发往mail_admins处理器，消息不向父层次发送
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'blog.views': {#所有高于（包括）info的消息同时会被发往console和mail_admins处理器，使用special过滤器
            'handlers': ['console', 'file'],
            'level': 'INFO',
            #'filters': ['special'],
            'propagate': True,
        }
    }
}

##############################################
####网页相关内容#################

SITE_TITLE = 'Python blog'
SITE_NAME = 'LIUBO的博客'
SITE_CONTENT = 'Python,Django,web,Blog'
SITE_DES = 'Python Technology blog'
SITE_LOGO = 'PYBLOG'

##分页
PAGE_SIZE = 1
