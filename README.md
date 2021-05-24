# Basic dependencies:
- python
- Django
- djangorestframework
- gunicorn
- whitenoise
- psycopg2-binary (for using postgres database)
- dynaconf (for managing settings)
- django-debug-toolbar (this should be in the list of dev packages, 
  but still figuring how to apply inheritance in settings.yaml, so temporarily put it here)

# Dev dependencies:
pytest
coverage
pytest-django 
Faker
flake8
pylint
black - code format
isort - for sorting imports
mypy - static type check
tox - a generic virtualenv management and test command line tool

# Basic usage:
### Settings (dynaconf):
- Copy .template.secrets.yaml to new file and rename the new file as .secrets.yaml
- Settings in this .secrets.yaml will override all settings from settings.yaml.
- Modify .secrets.yaml and settings yaml according to the need.

### With virtual env:
- Install tox globally.
- Run: tox -e dev 
  will create virtual env, install packages and start env.
- Inside virtual env using:
  tox -e codeFormat/lintAndTypeCheck/testsDebug/codeGuarantee according to the need.

### With docker:
- Use Dockerfile in production and Dockerfile.development in development
##### Commands:
- docker-compose build
- docker-compose up -d
- (docker-compose -f docker-compose.yml exec plan python manage.py makemigrations)
- (docker-compose -f docker-compose.yml exec plan python manage.py migrate --noinput)
- (docker-compose -f docker-compose.yml exec plan python manage.py collectstatic --no-input --clear)  
