# Greta

:seedling:
Python library for Green Computing:
Execute code at low carbon intensity.
:seedling:

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
and functions
which change the behaviour of your code
based on the carbon intensity:
skip heavy functions,
run more function iterations
if the carbon intensity is low,
and much,
much more.
The future is green
with Greta.

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

Refer to the [changelog](./CHANGELOG.md)
for the latest features.

### Setup

Available on PyPi,
so run

```Python
pip install greta
```

to install.

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
