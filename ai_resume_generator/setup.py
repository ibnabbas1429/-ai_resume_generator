from setuptools import setup, find_packages
import os
from pathlib import Path
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """Reads requirements from a file and returns them as a list."""
    if not os.path.exists(file_path):
        return []
    
    with open(file_path, "r") as file_obj:
        requirements = [req.strip() for req in file_obj.readlines()]
    
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)

    return requirements

def create_project_structure():
    """Creates the necessary project directory structure if it doesn't exist."""
    project_structure = {
        "backend/app": ["__init__.py", "main.py", "models.py", "routes.py", "database.py", "utils.py"],
        "backend": ["requirements.txt", "Dockerfile"],
        "frontend/public": [],
        "frontend/src/components": ["Header.js", "Dashboard.js", "ResumeForm.js"],
        "frontend/src": ["App.js", "index.js", "styles.css"],
        "frontend": ["package.json", "Dockerfile"],
        "cloud/aws": ["cloudformation.yaml"],
        "cloud/gcp": ["app.yaml"],
    }

    for folder, files in project_structure.items():
        Path(folder).mkdir(parents=True, exist_ok=True)  # Create directories
        for file in files:
            file_path = os.path.join(folder, file)
            if not os.path.exists(file_path):  # Avoid overwriting existing files
                with open(file_path, "w") as f:
                    f.write("")  # Create an empty file

    # Create additional root-level files if not present
    for file in [".gitignore", "README.md"]:
        if not os.path.exists(file):
            with open(file, "w") as f:
                f.write("# Resume & Cover Letter Generator\n")

# Run the project structure creation before setup
create_project_structure()

setup(
    name="AIPoweredResumeGenerator",
    version="0.0.1",
    author="IbnAbbas",
    author_email="ismail4tech123@gmail.com",
    description="An AI-powered Resume & Cover Letter Generator",
    long_description=open("README.md", encoding="utf-8").read() if os.path.exists("README.md") else "",
    long_description_content_type="text/markdown",
    install_requires=get_requirements("requirements.txt"),
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
)
