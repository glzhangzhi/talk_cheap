```bash
# make a new branch
git branch newBranchName

# delete a branch
git branch -d features1
# it will remain all commits, 

# switch to a existing branch
git checkout branchName

# make and switch to a new branch
git checkout -b newBranchname

# merge branchA into branchB
git checkout branchB; git merge branchA
git checkout branchA; git merge branchB
# so that it can keep both branchs update
# it seem like branchB come close to current branch

# rabase the bugFix after main branch
git checkout bugFix
git rebase main
git checkout main
git rebase bugFix
# the final state is same as last command combo
# but the branch graph is a single line

# checkout can not only be used to switch between branch
# it can be used to make HEAD pointer move to any commit
git checkout main
git commit
git checkout C2
git checkout C1

# but im Rahmen the commit hash is very long, not easy to use
# so we can use relative reference
git checkout main^  # move HEAD to relative main last one
git checkout main^2 # another father commit
git checkout main~3  # move HEAD to relative main last third
git checkout HEAD~^2~2

# most use this to move branch pointer to some commit
git checkout main
git branch -f main HEAD~3

# back to last commit
git reset HEAD~1
git revert HEAD~1
# differece is that 'resert' commit a commit about this change
# or simplly use this as default like ctrl + z
git reset --hard
# specific for merge operation
git merge --abort

# use cherry-pick to pick some commit from other branch
git cherry-pick C2 C4
# this is very important for only picking useful commit to your branch
# i.e. not pick those dev commit code
git cherry-pick C4

# last command is good to pick commit, but if you want to pick lots of commit
# it will have very long hash, which is definely we dont want
# instead we can use interactive rebase
git rebase -i HEAD~4
# it can also be used when you want to modify some commit in history
git rebase -i  # to move that commit to the front
git commit --amend  # amend commit, it will not add a new commit, only modify it
git rebase -i  # move the commit sequence to its origin like
# but if this order is to complex for you
# you can just use cherry-pick
git cherry-pick
git commit --amend
git cherry-pick

# add tag to some commit and can use it to move in commit history
git tag v1 sdflskg
git checkout v1

# describe now situation
git describe main
# this will show which tag is closest to main branch, in this how many commit it have and main pointer HASH

# copy the remote repo on local
git clone https://github.com/...git

# when you checkout on a remote branch like origin/dev and commit
# it will not appear actually on this remote branch
# but instead the HEAD will dispart and give a commit
# the remote branch just about the state of remote branch
git checkout origin/main
git commit

# get the data and update from repo
git fetch origin
# there are two steps behind this:
# 1. get the new commit that dont exist in local
# 2. update the remote branch pointer

# there are many way to update this new commit in local
git cherry-pick o/main
git rebase o/main
git merge o/main

git pull = git fetch + git merge

# push your local change to repo
# default is upstream
# you should check your push.default about your configuration
git push

# sometime you can push because the lastest change on remote make your change in local conflict
# so you must update your local and move your current work based on lastest change
git fetch
git rebase origin/main
git push
# you can also achieve this with merge
git fetch
git merge origin/main
git push
# this two look different, but have same effect

git pull --rebase = git fetch + git rebase
# or
git pull

# if you work in a big team, the main branch may be locked
# that's mean you can not directly push commit to main branch
# instead you have to use pull request
# you must create a new branch, all new commit must in this branch
# and give a pull request to merge this new branch and main branch in repo
# but before this, you must make sure, before any of you change, the state of repo must be same like remote one
# so if you have done some commit in your local main
# you must reset that
git reset --hard o/main
git checkout -b feature C2
git push origin feature

# there are two way to set remote track relationship
git checkout -b totallyNotMain origin/main
git branch -u origin/main totallyNotMain (default git branch -u origin/main if you are now in totallyNotMain branch)

# use parameter to specific which local branch you want to push to remote
git push origin main
git push origin source:destination
git fetch origin source:destiantion
# notice that the source and destination is opposite in push and fetch

# delete remote branch
git push origin :foo

git pull origin foo
=
git fetch origin fll
git merge o/foo

git pull origin bar~1:bugFix
=
git fetch origin bar~1:bugFix
git merge bugFix
```