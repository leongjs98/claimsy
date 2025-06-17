# Claimsy

!! **only group leader can push to main branch** !!

everyone needs to develop in your own branch and ask to merge to main

## Development
`cd` into the correct directory (folder)

### Backend

1. Make sure you are using Python 3.12.7

use `python --version` to check

2. Make sure you are in your virtual environment

- Create one if you don't have one `python -m venv myenv`

3. Install Python packages

   `pip install -r requirements.txt`

   If you are installing any other dependencies, make sure to include them into `requirements.txt`

   `pip freeze > requirements.txt`

4. Create your own `.env` (for database and Gemini API)

5. Create `claimsy` database if you haven't.

6. Create mock data (seeding)
```
python db/tables.py
python db/seeder_admin.py
python db/seeder_employee.py
python db/seeder_invoice.py
python db/seeder_claim.py
```

7. Delete mock data using `db/cleaner.py`
```
python db/cleaner.py --all
python db/cleaner.py --table claims
python db/cleaner.py --help
```

### Frontend
1. TailwindCSS

   `npm run tailwindcss`

2. Development Server

   `npm run dev`

## Setup

1. Install all node packages:

   `npm install`

2. Install [TailwindCSS Plugin](https://marketplace.visualstudio.com/items?itemName=bradlc.vscode-tailwindcss) for autocomplete

## Branch naming convention:

Create branches before each push. Following the naming convention below:

1. `FE_name_feature-name`
2. `BE_name_feature-name`
3. `AI_name_feature-name`

Examples:
`FE_aisya_add-mock-data`, `BE_mark_add-fastapi`, `AI_diana_remove-bug`
