from pathlib import Path


# Абсолютный путь до корневой директории проекта.
# Используется для построения всех путей внутри настроек проекта.
BASE_DIR = Path(__file__).resolve().parent.parent

# Секретный ключ Django. Используется для криптографических операций.
# Никогда не публикуется. В продакшене должен храниться в переменных окружения.
SECRET_KEY = (
    "django-insecure-q5kg0)za(0605y3=lpdlv)ivr)96-uc^qzp4v=jcjh3ny(88ej"
)

# Включает режим отладки. Показывает подробную информацию об ошибках.
# В продакшене всегда должен быть установлен в False.
DEBUG = True

# Список разрешённых доменов, с которых может обслуживаться сайт.
# Работает только если DEBUG установлен в False.
ALLOWED_HOSTS = ["127.0.0.1"]

# Список подключенных приложений проекта. Включает как встроенные, так и кастомные приложения.
INSTALLED_APPS = [
    "django.contrib.admin",         # Встроенная административная панель управления моделями.
    "django.contrib.auth",          # Система аутентификации пользователей.
    "django.contrib.contenttypes",  # Поддержка универсальных связей между моделями.
    "django.contrib.sessions",      # Поддержка пользовательских сессий через cookie.
    "django.contrib.messages",      # Механизм хранения временных сообщений для пользователей.
    "django.contrib.staticfiles",   # Поддержка обработки статических файлов (CSS, JS, изображения).
    'blog.apps.BlogConfig',         # <-- Подключаем приложение blog
]

# Список промежуточных компонентов, которые обрабатывают HTTP-запросы и ответы.
# Каждый middleware вызывается последовательно при обработке запроса и ответа.
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",  # Включает защиту: HTTPS, HSTS и другие меры безопасности.
    "django.contrib.sessions.middleware.SessionMiddleware",  # Подключает работу с сессиями.
    "django.middleware.common.CommonMiddleware",  # Обрабатывает общие аспекты HTTP-запросов (например, редиректы со слешами).
    "django.middleware.csrf.CsrfViewMiddleware",  # Защита от CSRF-атак (межсайтовой подделки запроса).
    "django.contrib.auth.middleware.AuthenticationMiddleware",  # Подключает текущего пользователя через request.user.
    "django.contrib.messages.middleware.MessageMiddleware",  # Поддержка временных сообщений (например, уведомления).
    "django.middleware.clickjacking.XFrameOptionsMiddleware",  # Устанавливает заголовок X-Frame-Options для защиты от clickjacking-атак.
]

# Имя Python-модуля, содержащего корневые маршруты URL проекта.
ROOT_URLCONF = "mysite.urls"

# Настройки шаблонизатора. Django будет искать шаблоны в директориях приложений и в DIRS.
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],  # Здесь можно указать дополнительные директории с шаблонами.
        "APP_DIRS": True,  # Поиск шаблонов внутри каждого установленного приложения.
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",  # Передаёт флаг DEBUG в шаблоны.
                "django.template.context_processors.request",  # Доступ к объекту request в шаблонах.
                "django.contrib.auth.context_processors.auth",  # Передаёт request.user и другие переменные аутентификации.
                "django.contrib.messages.context_processors.messages",  # Передаёт сообщения во все шаблоны.
            ],
        },
    },
]

# WSGI-приложение. Используется при развёртывании проекта через Gunicorn или uWSGI.
WSGI_APPLICATION = "mysite.wsgi.application"

# Настройки базы данных.
# По умолчанию используется SQLite — встроенная лёгкая база, подходящая для разработки.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",  # Движок базы данных. Здесь используется SQLite.
        "NAME": BASE_DIR / "db.sqlite3",  # Путь до файла базы данных.
    }
}

# Валидаторы паролей. Применяются при регистрации и изменении пароля.
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # Защищает от паролей, похожих на личные данные.
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",  # Проверяет минимальную длину пароля.
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",  # Запрещает популярные пароли.
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",  # Запрещает полностью числовые пароли.
    },
]

# Настройки интернационализации (язык, локализация и время).
LANGUAGE_CODE = "ru"  # Язык по умолчанию — русский.

TIME_ZONE = "Europe/Moscow"  # Часовой пояс проекта — Москва.

USE_I18N = True  # Включает поддержку перевода интерфейса.

USE_L10N = True  # Локализует вывод чисел, дат и времени в шаблонах.

USE_TZ = True  # Использует timezone-aware объекты datetime. По умолчанию сохраняет время в UTC.

# Базовый URL для доступа к статическим файлам (при DEBUG=True обслуживаются Django автоматически).
STATIC_URL = "/static/"

# Формат поля первичного ключа по умолчанию. С 3.2 — это BigAutoField, генерирующий большие целые значения.
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
