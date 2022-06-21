# Where to go
An educational project 

## Configuration

Configuration is stored in src/app/.env, for examples see src/app/.env.ci

## Installation

This project requires python3.10 and running postgres

```
pip install --upgrade pip pip-tools
make install
cd src
cp app/.env.ci app/.env  # default environment variables
```

To update dependencies, add the new one to `requirements.in` file and run

```
make freeze
```
