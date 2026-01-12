## For Contributors
### Precommit Setup

We use Google docstring format for our docstrings and the pre-commit library to check our code. To install pre-commit, run the following command:

```bash
conda install pre-commit  # or pip install pre-commit
pre-commit install
```

The pre-commit hooks will run automatically when you try to commit changes to the repository.


### Commit Message Guidelines
All commit messages should be clear, concise, and follow this format:
```
<type>: <short summary>

[optional body explaining the change]
```
Recommended types:
+ feat: A new feature
+ fix: A bug fix
+ docs: Documentation changes
+ refactor: Code restructuring without behavior changes
+ style: Code style changes (formatting, linting)
+ test: Adding or updating tests
+ chore: Non-code changes (e.g., updating dependencies)

Example:
```
feat: add user login API
```

### Issue Guidelines
+ Use clear titles starting with [Bug] or [Feature].
+ Describe the problem or request clearly.
+ Include steps to reproduce (for bugs), expected behavior, and screenshots if possible.
+ Mention your environment (OS, browser/runtime, version, etc.).

### Pull Request Guidelines
+ Fork the repo and create a new branch (e.g., feature/your-feature, fix/bug-name).
+ Keep PRs focused: one feature or fix per PR.
+ Follow the project’s coding style and naming conventions.
+ Test your changes before submitting.
+ Link related issues using Fixes #issue-number if applicable.
+ Add comments or documentation if needed.

We appreciate clean, well-described contributions! 🚀
