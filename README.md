<!---Documatic-section-fixed: top-1-start--->
# Greta

**Last updated:** 2022-02-08\
_Document generation aided by **Documatic**_

:seedling: Python library for Green Computing: Execute code at low carbon intensity. :seedling:

Green computing is a set of principles to develop software which is as good for the environment as possible. Carbon intensity is a measure of how much carbon is involved in the energy you use at any particular time. This depends on energy demand and the mix of supply from renewable and non-renewable sources. Greta provides function decorators and functions which change the behaviour of your code based on the carbon intensity: skip heavy functions, run more function iterations if the carbon intensity is low, and much, much more.
<!---Documatic-section-fixed: top-1-end--->

<!---Documatic-section-group: helloworld-start--->


## Getting Started

The codebase has a flat structure, with 6 code files.
<!---Documatic-section-helloworld: setup-start--->
The codebase is compatible with Python 3.6 and above, because of f-string 3.6 in /Users/tom/Documents/personal/projects/Greta/greta/checks.py.
Install requirements with `pip install -r requirements.txt`.

Run `pip install -e .` in top-level directory to install
package in local directory.
Install from pypi with `pip install greta`.


<!---Documatic-section-helloworld: setup-end--->

<!---Documatic-section-helloworld: entrypoints-start--->

## Developers
<!---Documatic-section-dev: setup-start--->
* Install developer requirements with `pip install -r requirements-dev.txt`
* Tests are present in `tests/` (using pytest)


<!---Documatic-section-dev: setup-end--->

<!---Documatic-section-dev: ci-start--->
The project uses GitHub Actions for CI/CD.

| CI File | Purpose |
|:----|:----|
| test | Executes on push for any branch, pull_request for any branch. Linting (with black, isort) |


<!---Documatic-section-dev: ci-end--->

<!---Documatic-section-group: dev-end--->


## Code Overview

* The codebase has a flat structure, with 5 files, a few functions and no key classes
* There are 3 source code objects in top-level `__main__`/`__init__`:

### `condition_function` from `greta/conditionals.py`
 
```python
condition_function(low_func: Callable, high_func: Callable, limit: str, *args, **kwargs)

The function takes two functions as arguments. A limit, and arguments to give to a function.
It executes a function based on the carbon intensity.
```
### `condition_variable` from `greta/conditionals.py`
 
```python
condition_variable(low_value, high_value, limit: str)

It takes a low_value, high_value, and limit.
It returns a value from low_value or high_value, depending on the current value of the carbon intensity.
It does not raise or catch any errors.
```

### `get_current_intensity` from `greta/query.py`
 
```python
get_current_intensity() -> str

Get the current carbon intensity for the UK
from carbonintensity.org API.
Does not raise.
```

These entrypoints are broken down into the following modules:

* `greta.conditionals` has 2 entrypoints
* `greta.query` has 1 entrypoints


<!---Documatic-section-helloworld: entrypoints-end--->

<!---Documatic-section-group: helloworld-end--->

<!---Documatic-section-group: dev-start--->

<!---Documatic-section-fixed: bottom-1-start--->
## Contributing

Pull requests,
issues
and feature requests are welcome!
Please refer to the [contributing guide](./CONTRIBUTING.md)
for more information.

## License

Distributed under GNU GPL-3 license.
Read the [license](./LICENSE)
for full terms.
<!---Documatic-section-fixed: bottom-1-end--->
