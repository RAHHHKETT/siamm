# SCM Notes - Merge Conflict Resolution

## What Happened
While merging the feature/release-notes branch into dev, a merge conflict occurred in CI and Change Log/release-notes.md because two members edited the same file simultaneously.

## How We Resolved It
1. Ran `git pull origin dev` to fetch the latest changes
2. Git flagged the conflict in release-notes.md
3. Opened the file and manually chose which changes to keep
4. Removed the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`)
5. Saved the file, ran `git add .` and `git commit` to complete the merge

## Lesson Learned
Always pull the latest changes before starting work on a shared file to minimize conflicts.