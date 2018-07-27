# Contribution guide

Any contribution whether it's a feature/enhancement request or a bug report/fix is always welcome.
If you require a feature urgently or have a wish to improve the project - go ahead and just do it!

## Submitting a bug

If you'd like to submit a bug, please, create a new issue and include in it a concise Python code snippet reproducing the problem.
Also explain why the current behavior is incorrect and what you expect instead.

## Working with the code and submitting changes

### Version control

We use Git for version control and GitHub for hosting the project.
Also we adhere usual [GitHub pull-request workflow](https://guides.github.com/introduction/flow/).

### Code style and standards

It's important to write code that is not only functioning correctly, but at the same time is readable and easy to understand as much as possible.

We embrace well established and commonly used Python code standards.
During development follow [PEP8](https://www.python.org/dev/peps/pep-0008/).

To check your changes for PEP8 compliance you can run:

```
$ flake8
```

### Testing

Whatever changes are made, they should be covered with unit tests. For this purpose the project uses [pytests](https://docs.pytest.org/).

To run tests you can run:

```
$ pytest [<path-to-the-test-module>]
```

Or if you want to run any specific test:

```
$ pytest <path-to-the-test-module>::<test-function>
```

# Licensing

When you submit code to our library, you implicitly and irrevocably agree to adopt the associated licenses. You should be able to find this in the file named `LICENSE`.

We use the MIT license; which permits Commercial Use, Modification, Distribution and Private use of our code, and therefore also your contributions. It also provides good compatibility with other licenses, and is intended to make re-use of our code as painless as possible for all parties.
