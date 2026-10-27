# Patient Records Management System

A command-line Python project to manage patient medical records,
built as part of a learning path covering Python, OOP, Testing,
and Data Analysis with real-world (fake) medical data.

> ⚠️ **Disclaimer:** This project uses fully fake/dummy data only.
> No real patient data is used or stored at any stage.

## Project Status

Currently in **Stage 1 (CLI)** — see roadmap below.

## Overview

The project is being built in 3 stages, each one adding a new layer
on top of the previous without throwing away earlier work:

| Stage | Focus | Output |
|---|---|---|
| 1 — CLI | Functions, dictionaries, basic I/O | Terminal app: add / search / delete / list patients, saved to JSON |
| 2 — OOP + Testing | Classes, inheritance, pytest | Same project rewritten with `Patient`, `Doctor`, `PatientRegistry` classes, with a working test suite |
| 3 — Data Analysis | pandas, matplotlib | Analysis of 50 fake patients: filtering, grouping, missing data, charts |

## Current Features (Stage 1)

- Add a patient (name, age, diagnosis) with input validation
- Search for a patient by name
- Delete a patient by name
- List all patients
- Simple terminal menu (`while` loop)

## Planned Features

- Save / load patients to and from `patients.json` (Stage 1, in progress)
- `Patient` class with `__init__` and `__str__` (Stage 2)
- `PatientRegistry` class to manage all patients (Stage 2)
- `Person` → `Patient` / `Doctor` inheritance (Stage 2)
- Unit tests with `pytest` (Stage 2)
- Data analysis notebook/script on 50 fake patients with pandas (Stage 3)
- Charts with matplotlib (Stage 3)

## Project Structure

```
records-patient/
├── README.md
└── v1/
    ├── cli.py         # Menu, user input, validation
    └── patients.py    # Core logic: add, search, delete, list
```

> Structure will change in Stage 2 when the project moves to classes
> (a new `v2/` folder, or restructured as the project grows).

## How to Run

```bash
cd v1
python cli.py
```

## How to Run Tests

> Not available yet — tests are planned for Stage 2.
> This section will be updated once `pytest` is added.

## Tech Stack

| Tool | Purpose |
|---|---|
| Python 3 | Core language |
| JSON | Data persistence |
| pytest | Testing (Stage 2) |
| pandas | Data analysis (Stage 3) |
| matplotlib | Visualization (Stage 3) |

## Author

Mohamed — learning project, Month 1 of a self-paced path toward
Python, Math, Machine Learning and Deep Learning with a focus on
medical data.