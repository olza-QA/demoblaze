# Demoblaze Automation Tests

This project implements automated tests for https://www.demoblaze.com. Project is available
on [GitHub](https://github.com/olza-QA/demoblaze).

Tech Stack **Python**, **Pytest**, **Allure** , **Playwright**. 

The project’s architecture was built using the Page Object Model and Page Factory patterns

## Project Overview

The goal of this project is to automate the testing of the Demoblaze. The automated tests verify various
functionalities of the online store web application
Both positive (valid input, expected messages) and negative (invalid input, modal pop-up) scenarios are covered for:

End-to-end (E2E) user scenario

Sign up

Log in

Purchase product

Navigation features


## Getting Started

### Clone the Repository

To get started, clone the project repository using Git:

```bash
git clone https://github.com/olza-QA/demoblaze.git
cd demoblaze
```

### Creation of virtual environment

Use a virtual environment to manage project dependencies.

#### Linux / MacOS

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Install Dependencies

Install the project dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Playwright Setup (if needed)

For the first time, you  need to install the required browsers:

```bash
playwright install
```

### Running the Tests with Allure Report

To run the tests and generate an Allure report, use the command:

```bash
pytest -m "regression" --alluredir=./allure-results
```

See results in the terminal.

### Viewing the Allure Report

Then you can generate and view the Allure report with:

```bash
allure serve allure-results
```

This command will open  report in your  browser.