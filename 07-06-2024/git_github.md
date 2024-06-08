### Basic Git Commands

Here is a comprehensive list of essential Git commands along with their descriptions:

#### **Configuration**
- `git config --global user.name "Your Name"`: Sets the username for all repositories on your system.
- `git config --global user.email "your_email@example.com"`: Sets the email for all repositories on your system.
- `git config --global color.ui auto`: Enables colorization of Git output.

#### **Repository Creation**
- `git init`: Initializes a new Git repository.
- `git clone <repository_url>`: Clones an existing repository from a URL.

#### **Basic Snapshotting**
- `git add <file>`: Stages a file for commit.
- `git add .`: Stages all changes in the current directory for commit.
- `git commit -m "commit message"`: Commits the staged changes with a message.
- `git status`: Shows the status of changes as untracked, modified, or staged.
- `git diff`: Shows the differences between working directory and staging area.
- `git diff --staged`: Shows the differences between the staging area and the last commit.

#### **Branching and Merging**
- `git branch`: Lists all branches in the repository.
- `git branch <branch_name>`: Creates a new branch.
- `git checkout <branch_name>`: Switches to the specified branch.
- `git checkout -b <branch_name>`: Creates and switches to a new branch.
- `git merge <branch_name>`: Merges the specified branch into the current branch.
- `git branch -d <branch_name>`: Deletes the specified branch.

#### **Remote Repositories**
- `git remote add origin <repository_url>`: Adds a remote repository.
- `git remote -v`: Shows all remotes and their URLs.
- `git fetch <remote>`: Fetches changes from the remote but does not merge them.
- `git pull <remote> <branch>`: Fetches and merges changes from the remote branch.
- `git push <remote> <branch>`: Pushes commits to the remote branch.

#### **Rewriting History**
- `git reset <file>`: Unstages a file.
- `git reset --hard <commit>`: Resets the working directory and staging area to the specified commit.
- `git commit --amend`: Amends the last commit with staged changes.
- `git rebase <base_branch>`: Reapplies commits on top of another base tip.

#### **Stashing and Cleaning**
- `git stash`: Stashes changes in a dirty working directory.
- `git stash apply`: Applies the most recent stash.
- `git stash pop`: Applies the most recent stash and removes it from the stash list.
- `git stash list`: Lists all stashes.
- `git clean -fd`: Removes untracked files and directories.

#### **Inspection and Comparison**
- `git log`: Shows the commit history.
- `git log --oneline`: Shows a compact version of the commit history.
- `git show <commit>`: Shows various types of objects (commits, trees, blobs).
- `git blame <file>`: Shows what revision and author last modified each line of a file.

### Example Workflow

Here's a typical workflow using these commands:

1. **Initialize a Repository**:
   ```bash
   git init
   ```

2. **Clone a Repository**:
   ```bash
   git clone https://github.com/user/repository.git
   ```

3. **Make Changes and Commit**:
   ```bash
   git add .
   git commit -m "Initial commit"
   ```

4. **Create and Switch to a New Branch**:
   ```bash
   git checkout -b new-feature
   ```

5. **Make Changes, Stage, and Commit**:
   ```bash
   git add .
   git commit -m "Add new feature"
   ```

6. **Merge the New Branch into Main Branch**:
   ```bash
   git checkout main
   git merge new-feature
   ```

7. **Push Changes to Remote**:
   ```bash
   git push origin main
   ```

8. **Handle Remote Changes**:
   ```bash
   git pull origin main
   ```

9. **Stash Changes**:
   ```bash
   git stash
   ```

10. **Apply Stash**:
    ```bash
    git stash apply
    ```
