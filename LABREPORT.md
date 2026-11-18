# Assignment Lab Report: Student Task Manager DevOps & Version Control

## Executive Summary
This report outlines the implementation and DevOps workflow of the **Student Task Manager** project. The project demonstrates end-to-end version control using Git, remote repository management on GitHub, isolated feature branching, code review via Pull Requests, merge conflict resolution, automated testing with Python `unittest`, Continuous Integration (CI) with GitHub Actions, and semantic release publishing.

---

## 1. Git vs. GitHub & Core Lifecycle Commands

### Differences Between Git and GitHub
| Dimension | Git | GitHub |
| :--- | :--- | :--- |
| **Type** | Distributed Version Control System (VCS) | Cloud-based hosting service & collaboration platform |
| **Operation** | Operates entirely locally on the developer's computer without requiring internet | Operates as a remote cloud service requiring internet access |
| **Core Role** | Tracks changes in source code, manages commit history, trees, and local branches | Provides remote backup, pull requests, issue tracking, code reviews, and CI/CD automation |
| **Installation** | CLI or desktop tool installed on host OS | Accessed through browser, GitHub CLI (`gh`), or REST/GraphQL APIs |

### Purpose of Add, Commit, and Push
1. **`git add`**:
   - Moves changes from the **Working Directory** to the **Staging Area** (Index).
   - Allows granular control over which changes and files should be bundled into the next snapshot, preventing accidental inclusion of temporary files or unrelated modifications.
2. **`git commit`**:
   - Captures a permanent, cryptographic snapshot (SHA hash) of the staged changes in the local repository history.
   - Each commit records an author, timestamp, parent commit ID, and a descriptive message explaining *why* the modification was introduced.
3. **`git push`**:
   - Transfers local commit objects and updates remote branch references on the GitHub remote server.
   - Publishes local commits so team members can access, review, and synchronize with the updated codebase.

---

## 2. Branching, Pull Requests & Merge Conflict Dynamics

### Why Branches and Pull Requests are Used
- **Branching**:
  - Provides isolated environments where developers can build new features, experiment, or fix bugs without destabilizing the production `main` branch.
  - Enables parallel development across multiple team members, reducing dependencies and blocking states.
- **Pull Requests (PRs)**:
  - Serve as the peer-review gatekeeper before branch integration.
  - Enable code review, discussion, automated testing checks (CI status), and security linting before code enters production.
  - Provide an auditable trail of decisions and architectural discussions linked to project issues.

### What Causes Merge Conflicts
A merge conflict occurs when Git attempts to combine changes from two branches that modified the **exact same line(s) of a file** differently since their common ancestor commit, or when one branch modified a file that the other branch deleted. Because Git cannot make arbitrary assumptions about which version is authoritative, it pauses the merge, inserts conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`), and leaves the resolution to the developer.

---

## 3. Git Operations: Fetch vs. Pull & Merge vs. Rebase

### `git fetch` vs. `git pull`
- **`git fetch`**:
  - Downloads new commits, files, and branches from the remote repository into remote tracking branches (e.g., `origin/main`).
  - **Does not modify** the local working directory or current branch. It is a completely safe inspection command.
- **`git pull`**:
  - Performs a `git fetch` followed immediately by a `git merge` (or `git rebase` if configured).
  - Actively modifies the local working tree by attempting to integrate remote commits into the current active branch.

### `git merge` vs. `git rebase`
- **`git merge`**:
  - Combines two branches by creating a new **merge commit** with two parents.
  - Preserves the chronological and structural history of both branches exactly as they occurred.
- **`git rebase`**:
  - Rewrites history by moving the base of the current branch onto the tip of another branch, sequentially replaying commits.
  - Results in a linear history with no merge commit, but rewrites commit SHA hashes, which should be avoided on shared public branches.

---

## 4. GitHub Issues and GitHub Actions in Team Collaboration

### GitHub Issues
- Function as the central project backlog and task tracking system.
- Categorize requirements through labels (`enhancement`, `bug`, `documentation`), milestones, and assignees.
- Integrates seamlessly with Pull Requests using closing keywords (e.g., `Closes #1`), ensuring issues close automatically upon PR merge and maintaining bidirectional traceability between tasks and code.

### GitHub Actions (CI/CD)
- Automates quality gates on every push and pull request.
- Runs automated unit tests, lint checks, and security audits in a clean virtualized environment (e.g., `ubuntu-latest`).
- Prevents regressions by catching broken assertions before merge approval, establishing rapid feedback loops that enhance software reliability.

---

## 5. Challenges Faced and Resolutions

### Challenge: Simultaneous Status Edits Resulting in Merge Conflict
- **Scenario**: When establishing the project status in `README.md`, two divergent branches (`conflict-feature-a` and `conflict-feature-b`) modified the line `Project status: Planning` into different statuses (`Development in Progress` vs. `Under QA and Review`).
- **Impact**: Merging the second branch into `main` resulted in:
  ```text
  CONFLICT (content): Merge conflict in README.md
  Automatic merge failed; fix conflicts and then commit the result.
  ```
- **Resolution**:
  1. Opened `README.md` and located the Git conflict markers (`<<<<<<< HEAD`, `=======`, `>>>>>>> conflict-feature-b`).
  2. Synthesized both team requirements into a unified status statement: `Project status: Active Development & Quality Review`.
  3. Removed all conflict demarcation lines.
  4. Staged the resolved file with `git add README.md` and finalized the merge commit (`git commit -m "fix(merge-conflict): resolve status conflict between feature-a and feature-b"`).
  5. Pushed the clean merge commit to `main`, successfully resolving the collision while preserving repository integrity.

---

## 6. Repository Artifacts Summary
- **Repository URL**: `https://github.com/HuzaifaSiddqui/studenttaskmanager`
- **Release Version**: `v1.0.0`
- **Total Commits**: 18+ commits
- **Feature Branches**: `feature/addtask`, `feature/completetask`, `feature/deletetask`
- **Tracked Issues**: #1, #2, #3, #4
- **Merged PRs**: 5 merged Pull Requests (#5, #6, #7, #9, #10)
- **CI Status**: Automated workflow executing on GitHub Actions with passing tests.
