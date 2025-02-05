## Git Cheat Sheet. By Augusto Damasceno.
> Copyright (c) 2023, 2024, Augusto Damasceno.  
> All rights reserved.  
> SPDX-License-Identifier: CC-BY-4.0  

## Contact
> [augustodamasceno@protonmail.com](mailto:augustodamasceno@protonmail.com)

# Git Cheat Sheet

* List configuration.
```bash
git config --list
```
* Define name, email and signing key locally.
```bash
git config user.name <name>
git config user.email <email>
git config user.signingkey <key>
```
* Define name, email and signing key globally.
```bash
git config --global user.name <name>
git config --global user.email <email>
git config --global user.signingkey <key>
```
* Create an empty git repository  
```bash
git init
```
* Create a new git repository and update with GitHub  
```bash
echo "# <REPOSITORY-NAME>" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:<GIT-USER>/<REPOSITORY-NAME>.git
git push -u origin main
```
* Clone a repo.
```bash
git clone https://<IP>/<USER>/<REPO>
git clone git@<IP>:<USER>/<REPO>.git
```
* List branchs and show the HEAD
```bash
git branch
```

* Create Branch
```bash
git checkout -b <BRANCH-NAME>
```

* Tree-like representation of branches  
```bash
git log --oneline --graph --all --decorate
```
* Add file, folder or all files not defined in .gitignore to the index (staging).
```bash
git add <file>
git add <folder>
git add --all
```
* Undo add before commit
```bash
git reset <file>
```
* Remove file from remote
```bash
git rm --cached <file>
git commit -m "<message>"
git push -u origin <branch>
```
* Commit.
```bash
git commit -m "<message>"
```
* Undo commit and keep all files staged
```bash
git reset --soft HEAD~
```
* List which files are staged, unstaged, and untracked.
```bash
git status
```
* Undo changes in unstaged files.
```bash
git checkout -- <file>
```
* Pulls the changes from the remote repository.
```bash
git pull <remote> <branch>
git pull origin <branch>
```
* Sends local commits to the remote repository. 
```bash
git push <remote> <branch>
git push origin <branch>
```
* Delete local branch
```bash
git branch -d <branch>
```
* Delete remote branch
```bash
git push <remote> :<branch>
git push origin :<branch>
```
* Display the entire commit history 
git log
* Display the full diff of each commit.
```bash
git log -p
```
* Display n last commits
```bash
git log -<n>
```
* Show last commit informations  
```bash
git show
```
* Show a commit diff and other informations 
```bash
git show <COMMIT-HASH>
```
* Show an object informations  
```bash
git show <OBJECT>
```
* Show unstaged changes between your index and working directory.
```bash
git diff
git diff HEAD <FILE>
```
* Revert to a commit by a hash (variation of Charles Bailey's solution)
```bash
# Reset the index to the desired commit
git reset --hard <commit>

# Move the branch pointer back to the previous HEAD
git reset --soft HEAD@{1}

# Commit the changes
git commit -m "Revert to <commit>"
```

* Revert a file back to the HEAD version
```bash
git checkout HEAD -- <FILE>
```

* Git log filtering by files add timestamp
```bash
git log --diff-filter=A --name-status --pretty=format:"%ad - %an: %s" --date=iso
```

* Git log filter by expression
```bash
git log --grep <EXPRESSION>
```
 
* Keep current state and remove all history
> [!WARNING]
>  Deleting past commits erases history. Use with caution.
```bash
git checkout --orphan new-branch
git commit -m "Initial commit"
git push -f origin new-branch
# remove protection deletion for the main branch
# delete the other branches
# set the new branch as the main
# protect the new branch
# Remove releases with code you don't want to publish. 
```

*  Extension for versioning large files  
> git-lfs  

Set up Git LFS for your user account by running  
```bash
git lfs install
```

Track files  
```bash
git lfs track "*.psd"
```

Add .gitattributes  
```bash
git add .gitattributes
```