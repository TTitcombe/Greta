# Contributing to this repository <!-- omit in toc -->

## Getting started <!-- omit in toc -->

Before you begin:
- Check out the [existing issues](https://github.com/TTitcombe/Greta/issues)

### Don't see your issue? Open one

If you spot something new, open an issue.
Types of issues include:

- A bug
  - Describe what the bug does; steps to reproduce; and your system information
- A feature
  - We're always looking for new ideas
- A question
  - We're happy to help with any questions about Greta and green computing

### Ready to make a change to the codebase?

- If there isn't an issue relating to the change you want to make,
create an issue first
- Comment on the issue to let us know you want to work on it
- [Fork the repo](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo#fork-an-example-repository)
so that you can make your changes
without affecting the original project
until you're ready to merge them.

### Make your update:

 - Create a new branch off `origin/master`
 - Make changes to the file(s) you need to update
 - Make sure the follow our [coding style](#coding-style)
 - If you are fixing a bug, create a unit test to check we don't reintroduce the bug
 - If you are creating a feature, create unit tests

### Open a pull request

When you're done making changes and you'd like to propose them for review,
open a pull request (PR).
Your PR should clearly explain:

- What it does
- How a reviewer should test that the changes work as expected
  - i.e. manual steps to use the new feature/test the bug fix

### Your PR is merged!

Congratulations!
We thank you for your help making Python that little bit greener. :seedling:

## Coding Style

- Standard Python style unless otherwise stated
  - E.g. camel_case
- `black` to format code
- `isort` to format inputs; using "black" style
- Numpy-style docstrings on functions and methods
- Type hints where it makes sense
  - Don't use `Any` or overly complex `List`,`Tuple`,`Dict` constructs
