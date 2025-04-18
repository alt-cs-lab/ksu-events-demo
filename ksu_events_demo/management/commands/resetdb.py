import os
import glob
import subprocess
from django.core.management.base import BaseCommand
from django.db import connection
from django.conf import settings
from importlib import import_module

class Command(BaseCommand):
    help = 'Resets the database, deletes migrations, and recreates migrations'

    def handle(self, *args, **options):
        self.stdout.write('Resetting database...')
        
        # Drop and recreate schema
        with connection.cursor() as cursor:
            cursor.execute('DROP SCHEMA public CASCADE;')
            cursor.execute('CREATE SCHEMA public;')
        
        self.stdout.write('Schema reset successfully!')
        
        # Find dependency migrations
        installed_apps = settings.INSTALLED_APPS
        migration_paths = []
        for app in installed_apps:
            try:
                app_module = import_module(app)
                app_path = os.path.dirname(app_module.__file__)
                migrations_path = os.path.join(app_path, 'migrations')
                
                if os.path.exists(migrations_path):
                    migration_paths.append(migrations_path)
            except (ImportError, AttributeError):
                # Skip apps that can't be imported or don't have a file path
                pass
        
        # Delete dependency migrations
        for migrations_path in migration_paths:
            migration_files = glob.glob(os.path.join(migrations_path, '*.py'))
            for file_path in migration_files:
                # Keep __init__.py but remove all other migration files
                if not os.path.basename(file_path) == '__init__.py':
                    try:
                        os.remove(file_path)
                        self.stdout.write(f'Deleted: {file_path}')
                    except Exception as e:
                        self.stdout.write(self.style.ERROR(f'Failed to delete {file_path}: {e}'))
        
        self.stdout.write('Migrations deleted successfully!')
        
        # Run makemigrations and migrate
        try:
            self.stdout.write('Running makemigrations...')
            subprocess.run(['poetry', 'run', 'python', 'manage.py', 'makemigrations'], check=True)
            
            self.stdout.write('Running migrate...')
            subprocess.run(['poetry', 'run', 'python', 'manage.py', 'migrate'], check=True)
            
            self.stdout.write(self.style.SUCCESS('Database reset and migrations recreated successfully!'))
        except subprocess.CalledProcessError as e:
            self.stdout.write(self.style.ERROR(f'Command failed: {e}'))