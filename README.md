<div align="center">

# 🏥 Patient Records

**A command-line patient records manager in Python, built stage by stage:
from plain functions, to classes and tests, to data analysis.**

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Stage](https://img.shields.io/badge/Stage%202-in%20progress-orange)
![Data](https://img.shields.io/badge/data-100%25%20fake-success)
![Dependencies](https://img.shields.io/badge/dependencies-none-lightgrey)
![Last commit](https://img.shields.io/github/last-commit/mohamed-haithem-eng/patient-records)

</div>

> ⚠️ **Data disclaimer:** every record in this project is fake. No real patient
> data is used, stored, or should ever be added.

## 📑 Table of contents

- [Why this project](#-why-this-project)
- [Status](#-status)
- [Features](#-features)
- [Quick start](#-quick-start)
- [Example session](#-example-session)
- [Project layout](#-project-layout)
- [Tests](#-tests)
- [Roadmap](#-roadmap)
- [About](#-about)

## 🎯 Why this project

I'm learning Python, maths, Machine Learning and Deep Learning with a focus on
medical data. Instead of isolated exercises, I'm growing **one project** through
three stages, so each new skill is applied to code I already understand.
Earlier versions are kept in the repo to keep the progress visible.

## 🚦 Status

| Stage | Focus | State |
|---|---|---|
| 1. CLI (`v1/`) | Functions, dicts, input validation, JSON persistence | ✅ Done |
| 2. OOP + tests (`v2/`) | `Patient` class, registry, inheritance, `pytest` | 🔨 In progress |
| 3. Data analysis | `pandas` + `matplotlib` on 50 generated fake patients | 📋 Planned |

## ✨ Features

**🖥️ v1: terminal app**
- ➕ Add, 🔍 search, 🗑️ delete and 📋 list patients from a menu loop
- 🛡️ Input validation: non-empty names, age must be an integer from 1 to 120
- 💾 Saved to `patients.json` and reloaded on start
- 🧯 Handles a missing or empty data file; a corrupted one exits with a clear message

**🧱 v2: rewrite with classes (in progress)**
- `Patient` class with `__init__` and `__str__`
- `to_dict()` / `from_dict()` to convert between objects and JSON-ready dicts

## 🚀 Quick start

Requires Python 3.10+ and no external packages.

```bash
git clone https://github.com/mohamed-haithem-eng/patient-records.git
cd patient-records/v1
python cli.py
```

> 💡 `patients.json` is created in the folder you run the program from. It is
> git-ignored on purpose, so local data never gets committed.

## 🧪 Example session

```text
====|Patient Menu|====
1 Add
2 Search
3 Delete
4 List
5 Exit
Enter Num: 4

 ====================  patients list: 2 ====================
1.  name: jon
    age: 33
    diagnosis: diabetes
============================================================
2.  name: sara
    age: 41
    diagnosis: asthma
============================================================
```

## 🗂️ Project layout

```text
patient-records/
├── v1/
│   ├── cli.py         # menu, user input, validation
│   └── patients.py    # add / search / delete / list, JSON save and load
├── v2/
│   └── patients.py    # Patient class (registry and tests coming)
├── .gitignore
└── README.md
```

## ✅ Tests

Not added yet. `pytest` tests for `Patient` and the registry are planned for
Stage 2; this section will get the exact command when they land.

## 🗺️ Roadmap

- [x] CLI with menu and validation
- [x] JSON persistence
- [x] `Patient` class with `to_dict` / `from_dict`
- [ ] `PatientRegistry` (add, find, remove, all) and a menu that uses it
- [ ] `Person` base class with `Patient` and `Doctor` subclasses
- [ ] `pytest` suite, including edge cases (empty list, duplicates, negative age)
- [ ] Generated `patients.csv` and a `pandas` analysis with charts

## 👤 About

A learning project by **Mohamed**, part of a self-paced path through Python,
maths, Machine Learning and Deep Learning, with a focus on medical data.
