# Patient Records

A command-line patient records manager in Python, built in stages to practice
core programming skills on a realistic, medical-flavoured problem.

> **Data disclaimer:** every record in this project is fake. No real patient
> data is used, stored, or should ever be added.

## Status

| Stage | Focus | State |
|---|---|---|
| 1. CLI (`v1/`) | Functions, dicts, input validation, JSON persistence | Done |
| 2. OOP + tests (`v2/`) | `Patient` class, registry, inheritance, `pytest` | In progress |
| 3. Data analysis | `pandas` + `matplotlib` on 50 generated fake patients | Planned |

## What works today

**v1 (terminal app)**
- Add, search, delete and list patients through a menu loop
- Input validation: non-empty names, age must be an integer from 1 to 120
- Patients are saved to `patients.json` and reloaded on start
- A missing or empty data file is handled; a corrupted one exits with a clear message

**v2 (rewrite with classes, in progress)**
- `Patient` class with `__init__` and `__str__`
- `to_dict()` / `from_dict()` for converting between objects and JSON-ready dicts

## Run

Requires Python 3.10+ and no external packages.

```bash
git clone https://github.com/mohamed-haithem-eng/patient-records.git
cd patient-records/v1
python cli.py
```

`patients.json` is created in the directory you run the program from. It is
git-ignored on purpose, so local data never gets committed.

## Tests

Not added yet. `pytest` tests for `Patient` and the registry are planned for Stage 2;
this section will be updated with the exact command when they land.

## Project layout

```
patient-records/
├── v1/
│   ├── cli.py        # menu, user input, validation
│   └── patients.py   # add / search / delete / list, JSON save and load
├── v2/
│   └── patients.py   # Patient class (registry and tests coming)
└── README.md
```

`v1` is kept as-is so the progression from functions to classes stays visible
in the history.

## Roadmap

- [x] CLI with menu and validation
- [x] JSON persistence
- [x] `Patient` class with `to_dict` / `from_dict`
- [ ] `PatientRegistry` (add, find, remove, all) and a menu that uses it
- [ ] `Person` base class, `Patient` and `Doctor` subclasses
- [ ] `pytest` suite, including edge cases (empty list, duplicates, negative age)
- [ ] Generated `patients.csv` and a `pandas` analysis with charts

## About

A learning project by Mohamed, part of a self-paced path through Python, maths,
Machine Learning and Deep Learning, with a focus on medical data.
