# spotless-squad

Spotless Squad is a platform which facilitates communication between customers and clean services. (also this application is part of MOPs subject)

# General notes

This project uses Python 3.11.x but keep compatibility with Python 3.9.x.
You need to set up `pre-commit` to commit your changes (see section below).
Some tools that we're using:

- `mypy` for static checking (see `mypy.ini`)
- `black` for automatic code formatting (see `pyproject.toml`)
- `pytest` for automatic testing - we currently don't have many tests...

# (REQUIRED) Development environment

Assuming you have the right Python version, you can create a virtual environment with all dependencies.

```sh
rm -rf venv-spotless-squad
python3.11 -m venv venv-spotless-squad

source venv-spotless-squad/bin/activate
python -m pip install --upgrade pip
pip install --force-reinstall -r requirements.txt
```

# (REQUIRED) pre-commit

!MAKE SURE YOU HAVE THE venv ACTIVATED!

Don't know what pre-commit is? Check it out, https://pre-commit.com/ .

First time setup:

```sh
pre-commit
pre-commit install
```

If you're curious about what's going on, check `.pre-commit-config.yaml`

Do this from time to time:

```sh
pre-commit autoupdate
```

Run before commiting:

```sh
pre-commit run --all
pre-commit run ruff --all
```
