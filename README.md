# Simple example of using pybind11 with poetry

This project is a fork of [Octavifs repository](https://github.com/octavifs/poetry-pybind11-integration) updated with the configuration tweaks to act as a scaffold to integrate [poetry >=1.6](https://pybind11.readthedocs.io/en/stable/) and [pybind11 >=2.11](https://pybind11.readthedocs.io/en/stable/). 

See this [link to explanation](https://octavifs.com/post/pybind11-multithreading-parallellism-python/) about performing the parallelism and benchmarking it as I've skipped this in the demo here.

# Setup
- Ensure you have poetry installed using whatever package manager floats your boat
- Clone this repo and cd into it
- `poetry install`
- `poetry run pytest`
