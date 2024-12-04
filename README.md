# Resume Parser and Database Uploader

## Overview
This project automatically parses resumes and uploads the extracted data to a database. It utilizes a CI/CD pipeline to detect changes in resume files and process them automatically. I use this for uploading the parsed PDF to my DB to sync it with my personal website.

## Usage
1. Place your resume file in the `resume` directory as `resume.pdf`
2. Commit and push your changes
3. The CI pipeline will automatically:
   - Detect the change
   - Parse the resume
   - Upload data to the database
