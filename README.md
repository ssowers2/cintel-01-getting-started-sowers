
# cintel-01-getting-started

[![Python 3.14](https://img.shields.io/badge/python-3.14%2B-blue?logo=python)](pyproject.toml)

[![CI](https://github.com/ssowers2/cintel-01-getting-started-sowers/actions/workflows/ci-python-zensical.yml/badge.svg)](https://github.com/ssowers2/cintel-01-getting-started-sowers/actions/workflows/ci-python-zensical.yml)

[![uv managed](https://img.shields.io/badge/uv-managed-DE5FE9)](https://docs.astral.sh/uv/)

[![ty type checked](https://img.shields.io/badge/ty-type_checked-2F80ED)](https://docs.astral.sh/ty/)

[![Zensical docs](https://img.shields.io/badge/Zensical-docs-purple)](https://zensical.org/)

[![MIT](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)

[![Documentation](https://img.shields.io/badge/docs-site-blue?logo=github)](https://ssowers2.github.io/cintel-01-getting-started-sowers/)

> Establish and verify a professional Python project for continuous intelligence.

## Project Overview

**Author:** Sabriya Sowers

**Date:** October 2026

This is my first project in the Continuous Intelligence course. I expanded the original Python pipeline to explore how Python can support data quality monitoring.

Using a small fictional healthcare dataset, I added a check for missing values and created a bar chart to visualize the results. This experiment connects what I'm learning in Python to my interest in data governance.

**Status:** Implemented and verified.

The project is configured in [pyproject.toml](pyproject.toml).

## Data

This project uses a fictional dataset containing five healthcare department records with three fields:

- RecordID
- Department
- Status

The dataset is stored in `data/department_records.csv`.

No real patient or organizational data is included.

## Approach

The project uses a Python pipeline to verify that the environment and project structure work correctly.

I expanded the pipeline to read a CSV file, identify missing values, and log the results. I also created a separate Python script using Matplotlib to generate a bar chart.

Important project components include:

- [pyproject.toml](pyproject.toml) - Project identity, dependencies, and tool configuration.
- [src/cintel/pipeline.py](src/cintel/pipeline.py) - Executable Python pipeline and data quality logging.
- [src/cintel/data_quality_chart.py](src/cintel/data_quality_chart.py) - Python script for creating the bar chart.
- [data/department_records.csv](data/department_records.csv) - Fictional healthcare department dataset.
- [docs/images/missing_values_chart.png](docs/images/missing_values_chart.png) - Saved data quality visualization.
- [tests/](tests/) - Automated tests.
- [.github/workflows/](.github/workflows/) - Automated testing and documentation deployment.
- [docs/](docs/) - Project documentation.
- [zensical.toml](zensical.toml) - Project documentation configuration.

## Run the Project

Follow the [Professional Python Workflow Guide](https://denisecase.github.io/pro-analytics-02/) to set up your machine and project environment.

From a VS Code terminal in the project root, run:

```shell
uv run python -m cintel.pipeline
```

To generate the data quality bar chart, run:

```shell
uv run python -m cintel.data_quality_chart
```

The chart is saved to `docs/images/missing_values_chart.png`.

## Results

The Python pipeline executed successfully and identified **3 missing values** across 5 fictional healthcare records.

- RecordID: 0 missing values
- Department: 2 missing values
- Status: 1 missing value

The pipeline displays the results through logging, including:

```text
Missing values found: 3
Pipeline executed successfully!
```

A `project.log` file is also created in the project root.

### Data Quality Visualization

The following bar chart shows the number of missing values in each field.

![Missing Values by Field](docs/images/missing_values_chart.png)

## Verification

I ran the pipeline twice and received the same result of 3 missing values.

I also manually reviewed the CSV file and confirmed that two Department values and one Status value were missing. This matched the Python results.

To run the automated tests:

```shell
uv run pytest
```

## Data Quality Experiment

I expanded my Python project to explore how Python can help identify missing values in healthcare department records.

I created a fictional dataset containing five records with three fields: RecordID, Department, and Status.

Using Python's built-in CSV library, I updated the pipeline to read the file and count missing values. The pipeline successfully identified three missing values and displayed the results through logging.

I also used Matplotlib to create a bar chart showing the missing values by field.

**Data Source:** Fictional data created specifically for this project. No real patient or organizational information was used.

### Observations

Department had the most missing values, while RecordID had none.

This helped demonstrate how a simple Python script can identify potential data quality issues that may need further review.

### Limitations

This experiment uses a small fictional dataset and only checks for blank values.

Future improvements could include checking for duplicate records, invalid values, and inconsistencies.

This experiment connects to my interest in using Python for data quality monitoring and data governance.

## Project Documentation

The [hosted documentation site](https://ssowers2.github.io/cintel-01-getting-started-sowers/) is published using Zensical and GitHub Pages.

The documentation site presents the project report, including data, methods, results, visualizations, interpretation, and conclusions.

## CI/CD and GitHub Actions

This project includes continuous integration and continuous deployment (CI/CD) to check project files and publish the documentation.

GitHub Actions include:

- [CI: Python and Documentation Checks](https://github.com/ssowers2/cintel-01-getting-started-sowers/actions/workflows/ci-python-zensical.yml)
- [CD: Documentation Deployment](https://github.com/ssowers2/cintel-01-getting-started-sowers/actions/workflows/deploy-zensical.yml)

## Developer Reference

Follow the [Professional Python Workflow Guide](https://denisecase.github.io/pro-analytics-02/) for detailed instructions and troubleshooting.

### Initialize and Update the Python Environment

With the project open in VS Code, open a terminal.

Run each command as needed:

```shell
uvx pup-clean --delete
uv self update
uv python pin 3.14
uv python install
uv lock --upgrade
uv sync
uv audit
```

Some commands may require adjustments depending on the local environment.

### Set Up and Run Git Hooks

Set up and run Git hooks to perform basic checks automatically before pushing changes to GitHub.

In the VS Code terminal:

```shell
uvx prek install --force
uvx prek update --freeze --cooldown-days 7

git add -A
uvx prek run --all-files
```

If checks modify files, review the changes and run the checks again.

### Run Common Chores

Run linters, formatters, type checks, tests, and build the documentation.

```shell
uv run ruff check . --fix
uv run ruff format .

uv run ty check
uv run python -m pytest
uv run python -m zensical build
```

### Git Add, Commit, and Push to GitHub

After making useful changes, save your work to GitHub.

```shell
git add -A
git commit -m "describe your changes in quotes"
git push
```

## Developer Notes

- Use the **UP ARROW** and **DOWN ARROW** in the terminal to scroll through previous commands.
- Use **Ctrl + F** to find text within a file.
- Use **Ctrl + H** in VS Code to find and replace text.
- Save changes before running the pipeline or committing files.

## Developer Tools

This project uses professional Python tools to support development, testing, documentation, and code quality.

- [uv](https://docs.astral.sh/uv/) - Python environments and dependencies.
- [Ruff](https://docs.astral.sh/ruff/) - Python linting and formatting, configured in [.ruff.toml](.ruff.toml).
- [ty](https://docs.astral.sh/ty/) - Python type checking.
- [pytest](https://docs.pytest.org/) - Automated Python testing, configured in [.pytest.toml](.pytest.toml).
- [prek](https://prek.j178.dev/) - Git hooks and automated checks, configured in [prek.toml](prek.toml).
- [Zensical](https://zensical.org/) - Project documentation, configured in [zensical.toml](zensical.toml).
- [Matplotlib](https://matplotlib.org/) - Python library used to create the data quality bar chart.

## Links

- [GitHub Repository](https://github.com/ssowers2/cintel-01-getting-started-sowers)
- [Hosted Documentation](https://ssowers2.github.io/cintel-01-getting-started-sowers/)
- [Professional Python Workflow Guide](https://denisecase.github.io/pro-analytics-02/)
- [Citation](CITATION.cff)
- [License](LICENSE)
