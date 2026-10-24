# Continuous Intelligence Project Report

Continuous Intelligence | Project 01 | Example Report

## Overview

This project establishes a professional Python environment
for developing and running continuous intelligence applications.

The objective is to demonstrate that a Python project can be
configured, executed, verified, and maintained using
a reproducible workflow.

## Tools and Methods

The project uses:

- Python for application logic.
- uv for Python and dependency management.
- Git and GitHub for version control.
- Logging for execution records.
- Ruff, ty, and pytest for code verification.
- Zensical and GitHub Pages for published documentation.

The example pipeline is organized as a Python module
with a `main()` function and structured logging.

## Verification

A successful execution displays:

    Pipeline executed successfully!

The pipeline records execution details in a project log.

These results demonstrate that the project environment
can execute the example application.

## Interpretation

A working development environment is a prerequisite
for building reliable analytical systems.

This project establishes the foundation for subsequent
work involving data ingestion, signal design,
anomaly detection, monitoring, and system assessment.

## Documentation Index

- **Home** - this landing page
- [**Project Instructions**](project-instructions.md)
- [**Glossary**](glossary.md)
- [**API**](api.md)

## Project Links

- [GitHub Repository](https://github.com/denisecase/cintel-01-getting-started)
- [Example Pipeline](https://github.com/denisecase/cintel-01-getting-started/blob/main/src/cintel/pipeline.py)

## Project Resources

- [Project Instructions](project-instructions.md)
- [Professional Python Guide](https://denisecase.github.io/pro-analytics-02/)
- [Professional Python Project Explainer](https://pup-pack.github.io/professional-python-project-explainer/).

## Custom Modifications

**What I changed:** I added a basic missing-value check to `src/cintel/pipeline.py` using a small list of sample data.

**Why I chose this change:** I wanted to explore how Python could help identify data quality issues because this connects to my interest in data governance.

**My prediction:** If I add a missing-value check using sample data with two blank entries, I expect Python to identify two missing values and display the count in the terminal because the `.count("")` method counts empty strings in a list.

## Data

I created a small fictional healthcare department dataset containing five records with three fields: RecordID, Department, and Status. The data is stored in `data/department_records.csv`.

The dataset was created specifically for this project and does not contain actual patient or organizational information. No external data source or license is required.

## Techniques Applied

I used Python's built-in `csv` library to read the dataset and check for missing values. I also used the project's existing logging functionality to display the results in the terminal.

## Methods and Settings

My goal was to identify missing values in the department records. I used `csv.DictReader()` to read the CSV file and counted fields containing empty strings using Python's `sum()` function.

I chose a CSV file instead of keeping the sample data directly in the Python code because I wanted to practice working with a separate dataset.

The pipeline identified three missing values: two missing department names and one missing status. This matched my expected results, and the pipeline completed successfully.
