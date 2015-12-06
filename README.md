# pre-commit
Various git pre-commit or pre-push hooks using http://pre-commit.com/


1. Have Python's pip package manager installed. `brew install python`
2. `pip install pre-commit`
3. Put a `.pre-commit-config.yaml` at the root of a repo. See below.
4. `pre-commit install`
5. `pre-commit install --hook-type pre-push`

The following YAML file is from the [standard repo](https://github.com/pre-commit/pre-commit-hooks) (not mine). 
`detect-aws-credentials` looks for the patterns in `~/.aws/credentials` in files. 
`detect-private-keys` looks for patterns that indicate private keys.

```yaml
-   repo: https://github.com/pre-commit/pre-commit-hooks.git
    sha: e306ff3b7d0d9a6fc7d128ef9ca2e0b6e6e76e8f
    stages: [commit, push]
    hooks:
    -   id: detect-aws-credentials
    -   id: detect-private-key
```

Note that the `sha` can be updated to the repo's most recent version with `pre-commit autoupdate`.

Here are my hooks:

```yaml
-   repo: https://github.com/marick/pre-commit-hooks.git
    sha: e306ff3b7d0d9a6fc7d128ef9ca2e0b6e6e76e8f
    stages: [commit, push]
    hooks:
    -   id: detect-aws-credentials
    -   id: detect-private-key
```

