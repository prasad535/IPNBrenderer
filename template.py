import os
from pathlib import Path
import logging

logging.basicConfig(
    level = logging.INFO,
    format = "[%(asctime)s:%(levelname)s]:%(message)s"
)
while True:
    project_name = input("Enter the project name :")
    if project_name != '':
        break

logging.info(f"creating project by name: {project_name}")

# list of files

list_of_files = [
    ".github/workflow/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"tests/__init__.py",
    f"tests/integration/__init__.py",
    f"tests/unit/__init__.py",
    "init_Setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "pyproject.toml",
    "setup.cfg",
    "tox.ini",

]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != '':
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating a directing at : {filedir} for file : {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"creating new filename : {filename} at path : {filedir}")
    else:
        logging.info(f"file is already present at : {filedir}")


