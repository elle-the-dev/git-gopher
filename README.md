# git-gud

Improving the Git CLI experience with fzf

![image](https://i.imgur.com/1tWisyl.gif)

## What is this?

Rather than needing to remember the exact name of the branch, tag or remote, or the exact syntax of the different git commands needed, **git-gud** will provide a list to choose from.

By using `fzf` for these lists, finding and choosing which item can be done by fuzzy searching the text.

And unlike the git GUIs out there, **git-gud** will say exactly what it's doing by displaying the command it will run before the selection is made.

## Requirements

[git](https://github.com/git/git) and [fzf](https://github.com/junegunn/fzf) must be installed.

## Installation

Clone the repository to a location where it can live in perpetuity.

```
git clone https://github.com/derekhamilton/git-gud.git
```

To automatically configure, run

```
sudo ./install.sh
```

which will symlink the commands to `/usr/local/bin` and create `~/.config/git-gud`

To use a different install directory, pass it as the first argument to the command

```
sudo ./install.sh ~/.local/bin
```

An uninstall script is also provided to remove the symlinks. If a custom install path was provided, it will have been saved to `~/.config/git-gud/install-dir` and use that. Uninstalling will also delete `~/.config/git-gud`

```
sudo ./uninstall.sh
```

To install manually without a script, add the project directory to `$PATH` and create `~/.config/git-gud`

With or without the install script, to use the command aliases, the following definitions need to be added to `.bashrc`, `.zshrc` or whichever configuration file is appropriate for the Unix shell being used.

```
alias gg="gg-menu"
alias ggc="gg-checkout-branch"
alias ggcr="gg-checkout-branch-remote"
alias ggct="gg-checkout-tag"
alias ggbt="gg-branch-tag"
alias ggm="gg-merge-branch"
alias ggmt="gg-merge-tag"
alias ggms="gg-merge-squash"
alias ggup="gg-upstream-push"
alias ggpt="gg-push-tag"
alias ggd="gg-delete-branch"
alias ggdf="gg-delete-branch-force"
alias ggdt="gg-delete-tag"
alias ggdtr="gg-delete-tag-remote"
alias ggrs="gg-reset"
alias ggrsh="gg-reset-hard"
alias ggdi="gg-diff-commits"
alias ggdit="gg-difftool-commits"
alias ggdd="gg-difftool-commits-dir-diff"
```

## Usage

**gid-gud** is run from the command line, same as `git`. The commands will be standard git commands, as if running them directly in the current working directory.

### Menu

The `gg-menu` command (alias `gg`) will bring up a fzf list of all the commands that git-gud provides, as well as additional standard git commands.

![image](https://i.imgur.com/enbjTFo.png)

Custom commands can be added to menu by creating `~/.gg-options` with the options listed in it, one per line, with the command and description separated by `|`.

Note: Commands cannot contain 2 consecutive spaces (`git log`: good, `git  log`: bad). The options are formatted using `column` and the two spaces are how the command column is delimited.

```
git dosomething      | Description of my command
git dosomethingelse  | Description of my other command
```

### Individual commands

There are several commands added to make use of `fzf` and make interacting with basic git commands faster and easier.

Commands will list out the available branches or tags in `fzf` as a fuzzy searchable menu rather than requiring that they be provided up front.

| command                      | alias     | description                                                |
| ---------------------------- | --------- | ---------------------------------------------------------- |
| gg-menu                      | gg        | Open menu with these and other commands                    |
| gg-checkout-branch           | ggc       | Checkout a local branch                                    |
| gg-checkout-branch-remote    | ggcr      | Checkout a local or remote branch                          |
| gg-checkout-tag              | ggct      | Checkout a tag                                             |
| gg-branch-tag                | ggbt      | Create and checkout a new branch from a tag                |
| gg-merge-branch              | ggm       | Merge a branch into the current branch                     |
| gg-merge-tag                 | ggmt      | Merge a tag into the current branch                        |
| gg-merge-squash              | ggms      | Merge and squash a branch into the current branch          |
| gg-delete-branch             | ggd       | Delete a branch                                            |
| gg-delete-branch-force       | ggdf      | Force delete a branch                                      |
| gg-delete-tag                | ggdt      | Delete a tag locally                                       |
| gg-delete-tag-remote         | ggdtr     | Delete a tag both locally and on remote                    |
| gg-upstream-push             | ggup      | Push the current branch to remote, setting the upstream    |
| gg-push-tag                  | ggpt      | Push a tag to a remote                                     |
| gg-reset                     | ggrs      | Unstage changes after the selected commit                  |
| gg-reset-hard                | ggrsh     | Revert to the selected commit, discarding changes          |
| gg-diff-commits              | ggdi      | Select two commits and show the changes between them       |
| gg-difftool-commits          | ggdit     | Select two commits and show the changes using difftool     |
| gg-difftool-commits-dir-diff | ggdd      | Select two commits and show the changed files by directory |
