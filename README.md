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

which will symlink the `gud` to `/usr/local/bin`

To use a different install directory, pass it as the first argument to the command

```
sudo ./install.sh ~/.local/bin
```

An uninstall script is also provided to remove the symlinks. If a custom install path was provided, it will have been saved to `~/.config/git-gud/install-dir` and use that. Uninstalling will also delete `~/.config/git-gud`

```
sudo ./uninstall.sh
```

To install manually without a script, add the project directory to `$PATH` and create `~/.config/git-gud`

### Updating

To update `git-gud` simply pull the latest version. Since install creates a symlink, the updated repository will mean everything is up-to-date.

## Usage

**gid-gud** is run from the command line, same as `git`. The commands will be standard git commands, as if running them directly in the current working directory.

### Menu

The `gud` command with no arguments will bring up a fzf list of all the commands that git-gud provides, as well as additional standard git commands.

![image](https://i.imgur.com/enbjTFo.png)

Custom commands can be added to menu by creating `~/.gud-options` with the options listed in it, one per line, with the command and description separated by `|`.

Note: Commands cannot contain 2 consecutive spaces (`git log`: good, `git  log`: bad). The options are formatted using `column` and the two spaces are how the command column is delimited.

```
git dosomething      | Description of my command
git dosomethingelse  | Description of my other command
```

### Individual commands

There are several commands added to make use of `fzf` and make interacting with basic git commands faster and easier.

Commands will list out the available branches or tags in `fzf` as a fuzzy searchable menu rather than requiring that they be provided up front.

| command                       | alias   | description                                                |
| ----------------------------- | --------| ---------------------------------------------------------- |
| gud menu                      | gud     | Open menu with these and other commands                    |
| gud checkout-branch           | gud c   | Checkout a local branch                                    |
| gud checkout-branch-remote    | gud cr  | Checkout a local or remote branch                          |
| gud checkout-tag              | gud ct  | Checkout a tag                                             |
| gud branch-tag                | gud bt  | Create and checkout a new branch from a tag                |
| gud merge-branch              | gud m   | Merge a branch into the current branch                     |
| gud merge-tag                 | gud mt  | Merge a tag into the current branch                        |
| gud merge-squash              | gud ms  | Merge and squash a branch into the current branch          |
| gud delete-branch             | gud d   | Delete a branch                                            |
| gud delete-branch-force       | gud df  | Force delete a branch                                      |
| gud delete-tag                | gud dt  | Delete a tag locally                                       |
| gud delete-tag-remote         | gud dtr | Delete a tag both locally and on remote                    |
| gud upstream-push             | gud up  | Push the current branch to remote, setting the upstream    |
| gud push-tag                  | gud pt  | Push a tag to a remote                                     |
| gud reset                     | gud rs  | Unstage changes after the selected commit                  |
| gud reset-hard                | gud rsh | Revert to the selected commit, discarding changes          |
| gud diff-commits              | gud di  | Select two commits and show the changes between them       |
| gud difftool-commits          | gud dit | Select two commits and show the changes using difftool     |
| gud difftool-commits-dir-diff | gud dd  | Select two commits and show the changed files by directory |
