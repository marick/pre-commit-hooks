# pre-commit
Various git pre-commit or pre-push hooks using http://pre-commit.com/. 


1. Have Python's pip package manager installed. `brew install python`
2. `pip install pre-commit`
3. Put a `.pre-commit-config.yaml` at the root of a repo. See below.
4. `pre-commit install`
5. `pre-commit install --hook-type pre-push`

Here is a sample [`.pre-commit-config.yaml`](https://github.com/marick/pre-commit-hooks/blob/master/dot-pre-commit-config.yaml.sample) file:

-   repo: /Users/marick/src/pre-commit-hooks
    sha: d6dee96f56bf9290f7ebb852c4252c50b8f6215d
    stages: [commit, push]
    hooks:
    -   id: only-branch-pushes
        args: [prevent, production|master]

    -   id: prohibit-suspicious-patterns
        args: [AKIA..........., --]
        # AKIA matches AWS keys.

General notes:
*  The `sha` can be updated to the repo's most recent version with `pre-commit autoupdate`.

Notes on `only-branch-pushes`:
* `only-branch-pushes` actually can be applied during the `commit` stage (as it is here, according to the `stages` key). The name is not so good, but I'm too lazy to change it.
* The first argument must be present as shown. The second is a `[[`-style shell pattern match. That is, it's
  compared like this:
  ```bash
      if [[ "$branch" =~ $pattern ]]; then
  ```
  If you want to prohibit just one branch, such as `production`, do this:
  ```
      args: [prevent, production]
  ```

Notes on `prohibit-suspicious-patterns`:
* The first line searches for a pattern that matches AWS keys. I use it as a [suspenders and belt](http://www.investopedia.com/terms/b/belt-and-suspenders.asp) strategy, alongside the `detect-aws-keys` hook from the [standard repo](https://github.com/pre-commit/pre-commit-hooks).
* The patterns are [Ruby regular expressions](http://ruby-doc.org/core-1.9.3/Regexp.html), compiled with `Regexp.compile`.
* As such, you can't use the "outside-the-pattern" syntax for modifiers like "match any case. That is, instead of `/TODO/i`, you must use this: 
  ```
  args: ["(?i-mx:TODO)", --]
  ```
* In violation of the spirit of `pre-commit`, this hook assumes Ruby already exists on your system.




The following YAML file uses the [standard repo](https://github.com/pre-commit/pre-commit-hooks) (not mine). 
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

Note that 

Here is a 

```yaml
-   repo: https://github.com/marick/pre-commit-hooks.git
    sha: e306ff3b7d0d9a6fc7d128ef9ca2e0b6e6e76e8f
    stages: [commit, push]
    hooks:
    -   id: detect-aws-credentials
    -   id: detect-private-key
```

