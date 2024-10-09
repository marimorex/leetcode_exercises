# LeetCode 75

- Resolution of the [LeetCode75](https://leetcode.com/studyplan/leetcode-75/) exercise list, incorporating unit tests and adhering to Python best practices.

# Instructions to Contribute

1. **Prerequisites:**
- python3, pip3 and venv. here after some commands to install the prerequisits:
    - `sudo apt update`
    - `sudo apt install python3`
    - `sudo apt install python3-pip`
    - `sudo apt install python3-venv`

2. **Clone the repository**:
   `git clone https://github.com/marimorex/leetcode_exercises.git`

3. **Navigate to the project folder**:
   `cd /path/to/project`

4. **Create a virtual environment**:
   `python3 -m venv name_of_your_venv`

5. **Activate the virtual environment**:
   - For Linux/macOS: `source name_of_your_venv/bin/activate`
        - To deactivate venv run: `deactivate`
            - to remove a venv run : `sudo rm -rf name_of_your_venv`
   - For Windows: `venv\Scripts\activate`

6. **Install the dependencies**:
   `pip install -r requirements.txt`

7. **Run tests**:
   `python3 -m unittest discover test`

8. **Run pre-commit hooks before making a commit**:
   Ensure that all files pass pre-commit checks with:
   `pre-commit run --all-files`

9. **Generate Documentation with Sphinx**
   - To generate documentation for a package from the Python docstring documentation:
      - In the root directory, run: `sphinx-apidoc -o docs nameOfThePackageToGenerateDocumentationFor`
         - Example: `sphinx-apidoc -o docs arrays`

   - To generate HTML documentation from the previous Sphinx package documentation:
      - In the docs directory, run: `make clean html`
