import csv
import os
import django
import sys

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NotesFront.settings')
django.setup()

# Now we can import Django models
from books.models import Subject, Module
from django.db import transaction

def import_csv(csv_file_path):
    """Import subjects and modules from a CSV file."""
    if not os.path.exists(csv_file_path):
        print(f"Error: File not found: {csv_file_path}")
        return
    
    print(f"Starting import from {csv_file_path}")
    
    # Keep track of the current subject being processed
    current_subject = None
    
    with open(csv_file_path, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header row
        
        with transaction.atomic():  # Use transaction to ensure data integrity
            for row in csv_reader:
                if len(row) < 3:
                    print(f"Warning: Skipping invalid row: {row}")
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
                        print(f"Created new subject: {subject_name} ({subject_code})")
                    else:
                        print(f"Found existing subject: {subject_name} ({subject_code})")
                    
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
                        print(f"Added module: {module_name} to {current_subject.name}")
                    else:
                        print(f"Module already exists: {module_name}")
    
    print("Import completed successfully")

if __name__ == "__main__":
    # Get the CSV file path from command line arguments or use default
    csv_file_path = sys.argv[1] if len(sys.argv) > 1 else 'subjects_modules.csv'
    import_csv(csv_file_path) 