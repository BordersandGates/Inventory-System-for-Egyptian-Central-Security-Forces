#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os , sys , webbrowser , subprocess 

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Manzoma.settings')
    os.environ.setdefault('DJANGO_DEBUG', 'True')
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
    #subprocess.Popen(['python3','Manzoma\manage.py' ,'runserver'])
    #webbrowser.open('http://127.0.0.1:8000')

if __name__ == '__main__':
    main()


