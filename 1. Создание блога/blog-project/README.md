```bash
# Создай публичный репозиторий в своем аккаунте GitHub и клонируй его на компьютер:
git clone https://github.com/you-accaunt-name/you-git-repositoies-name
cd you-git-repositoies-name

# Создай и активируй виртуальное окружение:
python3.9 -m venv venv
source venv/bin/activate

# Установи зависимости проекта:
pip install --upgrade pip
pip install -r requirements.txt

# Создай и примени миграции
cd you-app-name/
python manage.py makemigrations
python manage.py migrate

# Создай суперпользователя для админки
python manage.py createsuperuser

# Запусти проект на локальном тестовом сервере
python manage.py runserver

```