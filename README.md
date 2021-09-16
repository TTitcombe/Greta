# Greta

Python library for Green Computing:
Execute code at low carbon intensity.

Green computing is a set of principles to develop software
which is as good for the environment
as possible.
Carbon intensity is a measure of how much carbon
is involved in the energy you use
at any particular time.
This depends on
energy demand
and the mix of supply
from renewable
and non-renewable sources.
Greta provides function decorators
which allow you to set a carbon intensity threshold
below which the given function
should not run.

N.b. Greta currently only works for the UK.
If you know of carbon intensity APIs
for other countries,
please open an issue
or a pull request.

## How to use

### Examples

```Python
from greta import condition_variable, intensity_check_error

@intensity_check_error(limit="low")
def my_intensive_function():
    n_loops = condition_variable(50, 100, "very low")

# Will only run if intensity is "low" or "very low"
# Otherwise will raise greta.CarbonIntensityError
my_intensive_function()
```

### Setup

_Project has not yet been deployed to PyPi.
Package can instead by installed from this github._

- Developed in python 3.9,
but similar Python versions should work
- Clone this repository
- Run `pip install .`
in terminal

## Contributing

Pull requests,
issues
and feature requests are welcome!
If you're making a pull request,
please adhere to:

- Black code formatting
- isort import formatting
- numpy-style docstrings
- Type hints on functions and methods
- Unit testing with PyTest

## License

Distributed under GNU-3 license.
Read the [license](./LICENSE)
for full terms.
