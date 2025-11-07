# solar-challenge-week1

This repository contains the setup and initial structure for Task 1 of the 10 Academy solar challenge, focusing on Git and environment configuration.


## Environment Setup

To reproduce the development environment, you can use either `venv` (Python's built-in virtual environment module) or `conda` (a powerful package and environment manager).

### Using `venv` (Recommended for lightweight Python projects)

1.  **Create a virtual environment:**
    Open your terminal in the project root directory and run:
    ```powershell
    python -m venv .venv
    ```
    (Note: If `python` doesn't work, try `python3` or `py -3`)
2.  **Activate the virtual environment:**
    ```powershell
    .venv\Scripts\Activate.ps1
    ```
3.  **Install dependencies:**
    With the virtual environment activated, install the required packages:
    ```powershell
    pip install -r requirements.txt
    ```
4.  **Deactivate the virtual environment** when you're done working:
    ```powershell
    deactivate
    ```

### Using `conda` (Recommended for complex data science environments - if you have Anaconda/Miniconda)

1.  **Create a new conda environment:**
    ```powershell
    conda create -n solar-challenge-week1 python=3.9
    ```
2.  **Activate the conda environment:**
    ```powershell
    conda activate solar-challenge-week1
    ```
3.  **Install dependencies:**
    With the conda environment activated:
    ```powershell
    pip install -r requirements.txt
    ```
4.  **Deactivate the conda environment** when you're done:
    ```powershell
    conda deactivate
    ```

## Basic Usage

Once your environment is set up and dependencies are installed, you can execute Python scripts, run Jupyter notebooks, or develop your project components within the activated environment.

***File and Folder Structure of the project***
```
┣ 📂.github
┃ ┗ 📂workflows
┃   ┗ 📜unittests.yml
┣ 📂.vscode
┃ ┗ 📜settings.json
┣ 📂notebooks
┃ ┣ 📜__init__.py
┃ ┗ 📜README.md
┣ 📂scripts
┃ ┣ 📜__init__.py
┃ ┗ 📜README.md
┣ 📂src
┣ 📂tests
┃ ┗ 📜__init__.py
┣ 📜.gitignore
┣ 📜README.md
┗ 📜requirements.txt

```

Example:
```powershell
# 1. Activate your environment (either venv or conda)
#    (e.g., .venv\Scripts\Activate.ps1)

# 2. Run a script from the src directory
python src/main.py

# 3. Launch Jupyter Lab (if installed via requirements.txt)
jupyter lab


