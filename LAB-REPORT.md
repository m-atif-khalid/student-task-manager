# Lab Report: Student Task Manager Development and Version Control

## 1. Git and GitHub; add, commit, and push
Git is a distributed version-control system that tracks changes in files on a computer. GitHub is an online platform for hosting Git repositories and collaborating. `git add` stages selected changes, `git commit` saves a snapshot in the local repository, and `git push` uploads local commits to GitHub.

## 2. Branches, Pull Requests, and merge conflicts
Branches let developers work on separate features without changing the main branch directly. Pull Requests allow teammates to review and discuss changes before merging. A merge conflict happens when Git cannot automatically combine changes, commonly because two branches modify the same part of a file.

## 3. Fetch vs pull; merge vs rebase
`git fetch` downloads remote updates without integrating them into the current branch. `git pull` fetches and then integrates those updates. `git merge` combines branch histories and usually creates a merge commit. `git rebase` replays commits on top of another base commit, creating a more linear history and changing commit IDs.

## 4. GitHub Issues and Actions
GitHub Issues track bugs, tasks, and feature requests so work can be organized. GitHub Actions automates tasks such as running unit tests whenever code is pushed or a Pull Request is opened.

## 5. Difficulty faced and solution
A likely difficulty is resolving a merge conflict when two branches edit the same README line. The solution is to inspect the conflict markers, decide which information should remain, edit the file to remove the markers, test the result, and commit the resolution. Replace this paragraph with the actual difficulty you encountered during your lab.
