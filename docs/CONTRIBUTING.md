# Contributing to TecX_LM repo

Thank you for your interest in contributing!  
We follow a **Git‑Flow‑style** branching model:
```
main ← production‑ready releases
develop ← integration of all features / bug‑fixes
feature/* ← new feature work
release/* ← release preparation
hotfix/* ← emergency production patches
bugfix/* ← small, non‑feature bug fixes (optional)
experiment/*← prototypes, experiments (optional)
```

## Workflow

1. **Create a new branch** (feature, bugfix, etc.) from `develop` or `main` depending on the task.
2. **Push** the branch to GitHub and open a **Pull Request** against the appropriate target (`develop`, `main`, or both for releases/hotfixes).
3. **Let CI** run (GitHub Actions).  
   *All PRs must pass the CI and receive at least one approving review before merging.*
4. **Merge** using your team’s merge strategy (`Rebase and merge`, `Squash and merge`, or `Merge commit`).  
   After merging, delete the source branch (both locally and remotely).

### Pull‑Request labels

| Label      | Meaning                                   |
|------------|-------------------------------------------|
| `feature`  | New feature work                          |
| `bug`      | Bug‑fix or regression                     |
| `release`  | Release branch, prep for merge to `main`  |
| `hotfix`   | Emergency patch to `main` and `develop`   |
| `needs review` | Requires at least one approval        |
| `needs design` | Design/UX review needed              |

### Checklist for contributors

- [ ] Follow the branching convention.
- [ ] Write unit tests for any new code.
- [ ] Run `pytest` locally and ensure all tests pass.
- [ ] Ensure `flake8` and `black` succeed locally.
- [ ] Add a meaningful commit message (e.g., `feat: add user‑auth`).
- [ ] Open a PR and request the appropriate reviewers.

### Code of Conduct

All contributors must respect the guidelines in `CODE_OF_CONDUCT.md`.

## FAQ

- **Where does the final release tag go?**  
  After merging a `release/*` branch into `main`, tag it with `git tag -a vX.Y.Z -m "Release vX.Y.Z"`.  
- **Can I delete branches automatically?**  
  Yes – once merged, run `git branch -d <branch>` and `git push origin --delete <branch>`.

Happy hacking!
