# Some `pre-commit` hooks I use

Various git pre-commit or pre-push hooks using http://pre-commit.com/. 


1. Have Python's pip package manager installed. `brew install python`
2. `pip install pre-commit`
    * If your version of `pre-commit` is less than 0.7, you need `pip install --upgrade pre-commit`
3. Put a `.pre-commit-config.yaml` at the root of a repo. See below.
4. `pre-commit install` # this installs pre-commit hooks
5. `pre-commit install --hook-type pre-push`

Here is a sample [`.pre-commit-config.yaml`](https://github.com/marick/pre-commit-hooks/blob/master/dot-pre-commit-config.yaml.sample) file:

```yaml
-   repo: /Users/marick/src/pre-commit-hooks
    sha: d6dee96f56bf9290f7ebb852c4252c50b8f6215d
    stages: [commit, push]
    hooks:
    -   id: only-branch-pushes
        args: [prevent, ^(production|master)$]

    -   id: prohibit-suspicious-patterns
        args: [AKIA..........., --] # matches AWS keys
```
General notes:
*  The `sha` can be updated to the repo's most recent version with `pre-commit autoupdate`.

Notes on `only-branch-pushes`:
* Despite the name, `only-branch-pushes` actually can be applied during the `commit` stage (as it is here, according to the `stages` key). The name is not so good, but I'm too lazy to change it.
* The first argument must be `prevent`. The second is used in a
  `=~`-style shell pattern match. That is, it's
  compared like this:
  
      if [[ "$branch" =~ $pattern ]]; then
  
  If you want to prohibit just one branch, such as `production`, do this:
  
      args: [prevent, ^production$]
  

Notes on `prohibit-suspicious-patterns`:
* The first arg searches for a pattern that matches AWS keys. I use it as a [suspenders and belt](http://www.investopedia.com/terms/b/belt-and-suspenders.asp) strategy, alongside the `detect-aws-keys` hook from the [standard repo](https://github.com/pre-commit/pre-commit-hooks).
* The patterns are [Ruby regular expressions](http://ruby-doc.org/core-1.9.3/Regexp.html), compiled with `Regexp.compile`.
* As such, you can't use the "outside-the-pattern" syntax for modifiers like "match any case. That is, instead of `/TODO/i`, you must use this: 
  
      args: ["(?i-mx:TODO)", --]

* If you want to disable checking for a particular line, include `git commit ok` on that line. (You can replace the spaces with any *single* character.)
* In violation of the spirit of `pre-commit`, this hook assumes Ruby already exists on your system.

