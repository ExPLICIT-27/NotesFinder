# CSV Import for Subjects and Modules

This document explains how to use the custom Django management command to import subjects and modules from a CSV file.

## CSV Format

The CSV file should have the following format:

```
Subject,Code,Modules
Subject Name 1,CODE1,Module - 1 : Module Name
,,Module - 2 : Another Module Name
Subject Name 2,CODE2,Module - 1 : First Module
```

- The first row is a header row
- Each subject has its name and code in the first column and second column
- Modules for a subject are listed in rows below, with empty cells for Subject and Code
- Each module name is in the third column

## Preparing the CSV File

You can use the provided `save_csv.py` script to generate a sample CSV file:

```
python save_csv.py
```

This will create a file named `subjects_modules.csv` in your project directory.

## Running the Import Command

To import subjects and modules from the CSV file, use the following command:

```
python manage.py import_csv subjects_modules.csv
```

Replace `subjects_modules.csv` with the path to your CSV file if it's different.

## What the Command Does

The import command will:

1. Read the CSV file row by row
2. For each subject (rows with Subject and Code values):
   - Check if the subject already exists in the database (by code)
   - If not, create a new subject
3. For each module (rows with only Module value):
   - Add the module to the current subject if it doesn't already exist
   - Set the file_path to "To be filled later"

## Notes

- The command uses database transactions to ensure data integrity
- If a subject or module already exists, it won't be duplicated
- The command will output progress information as it runs 