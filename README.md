# Simple example of using pybind11 with Poetry

This project is a fork of [Octavifs repository](https://github.com/octavifs/poetry-pybind11-integration) updated with the configuration tweaks to work with poetry 1.6 and pybind11 >2.11. It is a scaffold for on how to setup a [*pybind11*](https://pybind11.readthedocs.io/en/stable/) build with [*Poetry*](https://python-poetry.org/). 

See this [link to explanation](https://octavifs.com/post/pybind11-multithreading-parallellism-python/) about performing the parallelism, as I skip this in this scaffold. 

# Setup
- Ensure you have poetry installed using whatever package manager floats your boat
- Clone this repo and cd into it
- `poetry install`
- `poetry run pytest`
