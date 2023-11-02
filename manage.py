#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'unwasteBackend.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
    
    """Use the below as arguments when running the server
       Can't do other commands here if these are hardcoded
    developer_ip = "172.17.21.199"
    current_ip = "localhost"
    execute_from_command_line(["manage.py", "runserver", current_ip+":8080"])"""


if __name__ == '__main__':
    main()
