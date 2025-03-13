import csv
import os
from django.core.management.base import BaseCommand
from books.models import Subject, Module
from django.db import transaction

class Command(BaseCommand):
    help = 'Import subjects and modules from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']
        
        if not os.path.exists(csv_file_path):
            self.stdout.write(self.style.ERROR(f'File not found: {csv_file_path}'))
            return
        
        self.stdout.write(self.style.SUCCESS(f'Starting import from {csv_file_path}'))
        
        # Keep track of the current subject being processed
        current_subject = None
        
        with open(csv_file_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip header row
            
            with transaction.atomic():  # Use transaction to ensure data integrity
                for row in csv_reader:
                    if len(row) < 3:
                        self.stdout.write(self.style.WARNING(f'Skipping invalid row: {row}'))
                        continue
                    
                    subject_name, subject_code, module_name = row
                    
                    # If subject name and code are provided, this is a new subject
                    if subject_name and subject_code:
                        # Check if subject already exists
                        subject, created = Subject.objects.get_or_create(
                            code=subject_code,
                            defaults={'name': subject_name}
                        )
                        
                        if created:
                            self.stdout.write(self.style.SUCCESS(f'Created new subject: {subject_name} ({subject_code})'))
                        else:
                            self.stdout.write(self.style.SUCCESS(f'Found existing subject: {subject_name} ({subject_code})'))
                        
                        current_subject = subject
                    
                    # If we have a module name and a current subject, add the module
                    if module_name and current_subject:
                        # Check if module already exists for this subject
                        module, created = Module.objects.get_or_create(
                            subject=current_subject,
                            name=module_name,
                            defaults={'file_path': 'To be filled later'}
                        )
                        
                        if created:
                            self.stdout.write(self.style.SUCCESS(f'Added module: {module_name} to {current_subject.name}'))
                        else:
                            self.stdout.write(self.style.SUCCESS(f'Module already exists: {module_name}'))
        
        self.stdout.write(self.style.SUCCESS('Import completed successfully')) 