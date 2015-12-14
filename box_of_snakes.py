import sys
import os
import django
from django.core import management


def create_django_project():
  ''' create_django_project
  Don't call this unless you intend on making a new django
  project.
  This function will trigger the setup of a new django project.
  Modify the paths to suit your needs
  '''
  python_path = "c:\python34\scripts\\"
  python_cmd = "python "
  cmd = python_cmd + python_path + \
    "django-admin.py startproject tango_with_django_project"
  os.system(cmd)


if __name__ == '__main__':
  '''Guess this isn't needed for now...that the django generated
  some files...
  '''
