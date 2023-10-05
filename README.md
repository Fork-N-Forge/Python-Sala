# Python-Sala
Python-Sala is the Hub of standard python projects.

# Contribution Rules📚:

- You are allowed to make pull requests that break the rules. We just merge it ;)
- Do NOT add any build steps e.g npm install (we want to keep this a simple static site)
- Do NOT remove other content.
- Styling/code can be pretty, ugly or stupid, big or small as long as it works
<!-- - Add your name to the contributorsList file. -->
- Try to keep pull requests small to minimize merge conflicts


### Installation

1. Clone the repo
```sh
git clone https://github.com/Fork-N-Forge/Python-Sala
```
2. Start a new branch.
```sh
Check Contributing topic to find out about branching
```

3. And start your contributions.

----------

## Steps to follow :scroll:

### 0. Star The Repository :star2:

Star the repository by pressing the topmost-right button to start your wonderful journey.

### 1. Fork it :fork_and_knife:

You can get your own fork/copy of [Python-Sala](https://github.com/Fork-N-Forge/Python-Sala) by using the <a href="https://github.com/Fork-N-Forge/Python-Sala/fork"><kbd><b>Fork</b></kbd></a> button.


### 2. Clone it :busts_in_silhouette:

`NOTE: commands are to be executed on Linux, Mac, and Windows(using Powershell)`

You need to clone or (download) it to local machine using

```sh
$ git clone https://github.com/Fork-N-Forge/Python-Sala.git
```

> This makes a local copy of the repository in your machine.
Once you have cloned the `Python-Sala` repository in Github, move to that folder first using change directory command on Linux, Mac, and Windows(PowerShell to be used).

```sh
# This will change directory to a folder Python-Sala
$ cd Python-Sala
```

Move to this folder for all other commands.

### 3. Set it up :arrow_up:

Run the following commands to see that *your local copy* has a reference to *your forked remote repository* in Github :octocat:

```sh
$ git remote -v
origin  https://github.com/Your_Username/Pyhton-Sala.git (fetch)
origin  https://github.com/Your_Username/Python-Sala.git (push)
```

Now, let's add a reference to the original [Python-Sala](https://github.com/Fork-N-Forge/Python-Sala) repository using


### 4. Sync it :recycle:

Always keep your local copy of the repository updated with the original repository.
Before making any changes and/or in an appropriate interval, run the following commands *carefully* to update your local repository.

```sh
# Fetch all remote repositories and delete any deleted remote branches
$ git fetch --all --prune
# Switch to `main` branch
$ git checkout main
# Reset local `main` branch to match the `upstream` repository's `main` branch
$ git reset --hard upstream/main
# Push changes to your forked `Python-Sala` repo
$ git push origin main
```


### 5. Create a new branch :bangbang:

Whenever you are going to contribute. Please create a separate branch using command and keep your `main` branch clean (i.e. synced with remote branch).

```sh
# It will create a new branch with name Branch_Name and switch to branch Folder_Name
$ git checkout -b BranchName
```

Create a separate branch for contribution and try to use the same name of the branch as of folder.

To switch to the desired branch

```sh
# To switch from one folder to other
$ git checkout BranchName
```

To add the changes to the branch. Use

```sh
# To add all files to branch Folder_Name
$ git add .
```

Type in a message relevant for the code reviewer using

```sh
# This message get associated with all files you have changed
$ git commit -m 'relevant message'
```

Now, Push your awesome work to your remote repository using

```sh
# To push your work to your remote repository
$ git push -u origin BranchName
```

###### *We will do our best to merge as much as possible from everyone. However, time is limited and the merge conflicts are horrible :astonished: <3*
