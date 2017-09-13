# Employee management system

To run the system locally:

1. Clone the repo
```git clone https://github.com/JoanNgatia/kazi.git```

2. Create a virtual environment

```mkvirtualenv <virtualenvname>```

3. Install dependencies within virtualenv 

```pip install -r requirements.txt```

4. Set up local settings by adding `local.py` file in the settings folder with your secret key value.

5. Spin up server
```cd kaziapp```

```python mana.py runserver --settings=kaziapp.settings.local```

To run the tests:

```python manage.py test```