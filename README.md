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

```python manage.py runserver --settings=kaziapp.settings.local```

To run the tests:

```python manage.py test```


Available endpoints

| URL Endpoint | What it does                                       |
|--------------|----------------------------------------------------|
| /employers   | Creates new employer info, Retrieves all employers |
| /employees   | Creates new employee info, Retrieves all employees |
| /employers/employer_id/ | Updates, Deletes single employer info              |
| /employees/employee_id/ | Updates, Deletes single employee info              |