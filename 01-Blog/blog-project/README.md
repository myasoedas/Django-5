```bash
# Создай публичный репозиторий в своем аккаунте GitHub и клонируй его на компьютер:
git clone https://github.com/you-accaunt-name/you-git-repositoies-name
cd you-git-repositoies-name

# Создай и активируй виртуальное окружение:
python3.12 -m venv my_env
source my_env/bin/activate

# Установи зависимости проекта:
pip install --upgrade pip
pip install -r requirements.txt

# Установка атоформатеров кода Python
pip install isort black
# Создайте файл pyproject.toml и внесите в него настройки PEP8
# Когда настройки будут готовы выполняйте команды из корня проекта:
isort mysite/
black mysite/

# Создай и примени миграции
cd you-app-name/
python manage.py makemigrations
python manage.py migrate

# Создай суперпользователя для админки
python manage.py createsuperuser

# Запусти проект на локальном тестовом сервере
python manage.py runserver

```