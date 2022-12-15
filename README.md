Lipetsk Region

![flake8 test](https://github.com/dino-mayk/LipetskRegion/actions/workflows/python-package.yml/badge.svg)

# Оглавление

- [Установка](#установка)
- [Запуск](#запуск)
- [Разработка](#разработка)

# Установка

Клонируйте репозиторий:
```bash
git clone https://github.com/dino-mayk/LipetskRegion.git
```

Создайте виртуальное окружение:

Windows:
```bash
python -m venv venv
```
Mac, Linux:
```bash
python3 -m venv venv
```

Активируйте виртуальное окружение:

Windows:
```bash
cd venv/Scripts/
.\activate
```
Mac, Linux:
```bash
source venv/bin/activate
```

Скачайте зависимости:

Windows:
```bash
pip install -r requirements.txt
```
Mac, Linux:
```bash
pip3 install -r requirements.txt
```

# Запуск 

Windows:
```bash
python index.py runserver
```
Mac, Linux:
```bash
python3 index.py runserver
```

# Разработка

Создание администратора:

Windows:
```bash
python index.py createsuperuser
```

Mac, Linux:
```bash
python3 index.py createsuperuser
```

Смена пароля в аккаунте:

Windows:
```bash
python index.py changepassword <user_name>
```

Mac, Linux:
```bash
python3 index.py changepassword <user_name>
```
