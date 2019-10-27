# git-gopher

Improving the Git CLI experience with fzf

![image](https://i.imgur.com/H1R5NxU.gif)

## What is this?

Rather than needing to remember the exact name of the branch, tag or remote, or the exact syntax of the different git commands needed, **git-gopher** will provide a list to choose from.

By using `fzf` for these lists, finding and choosing which item can be done by fuzzy searching the text.

And unlike the git GUIs out there, **git-gopher** will say exactly what it's doing by displaying the command it will run before the selection is made.

## Requirements

The following must be installed

 - Python 3.5+
 - Python module `colorama` (`pip3 install colorama`)
 - [git](https://github.com/git/git)
 - [fzf](https://github.com/junegunn/fzf)

To use syntax highlighting in commands with preview windows like `stash-pop`, [bat](https://github.com/sharkdp/bat) is required.

## Installation

Install via pip

```
pip3 install git_gopher
```

## Usage

**gid-gopher** is run from the command line, same as `git`. The commands will be standard git commands, as if running them directly in the current working directory.

### Menu

The `ggo` command with no arguments will bring up a fzf list of all the commands that git-gopher provides, as well as additional standard git commands.

![image](https://i.imgur.com/E8RsDeS.png)

Custom commands can be added to menu by creating `~/ggo-options.dat` with the options listed in it, one per line, with the command, shortcut, and description separated by `|`.

Note: Commands cannot contain 2 consecutive spaces (`git log`: good, `git  log`: bad). The options are formatted into `columns` and the two spaces are how the command column is delimited.

```
git dosomething      | shortcut  | Description of my command
git dosomethingelse  | shortcut2 | Description of my other command
```

### Individual commands

There are several commands added to make use of `fzf` and make interacting with basic git commands faster and easier.

Commands will list out the available branches or tags in `fzf` as a fuzzy searchable menu rather than requiring that they be provided up front.

Run any command or alias by passing it to the `ggo` command

```
ggo [command|alias]
```

| command                    | alias | description                                                         |
| -------------------------- | ----- | ------------------------------------------------------------------- |
| menu                       |       | Open menu with these and other commands                             |
| checkout-branch            | c     | Checkout a local branch                                             |
| checkout-branch-remote     | cr    | Checkout a local or remote branch                                   |
| checkout-tag               | ct    | Checkout a tag                                                      |
| branch-branch              | bb    | Create and checkout a new branch from another branch                |
| branch-tag                 | bt    | Create and checkout a new branch from a tag                         |
| merge-branch               | m     | Merge a branch into the current branch                              |
| merge-tag                  | mt    | Merge a tag into the current branch                                 |
| merge-squash               | ms    | Merge and squash a branch into the current branch                   |
| add                        | a     | Track and stage selected files                                      |
| fetch                      | f     | Retrieve repo information from selected remote                      |
| track-remote               | tr    | Change which remote upstream to track                               |
| upstream-push              | up    | Push the current branch to remote, setting the upstream             |
| push-tag                   | pt    | Push a tag to a remote                                              |
| tag-increment-version      | tiv   | Create a new tag, incremented by major, minor or patch              |
| delete-branch              | d     | Delete a branch                                                     |
| delete-branch-force        | df    | Force delete a branch                                               |
| delete-tag                 | dt    | Delete a tag locally                                                |
| delete-tag-remote          | dtr   | Delete a tag both locally and on remote                             |
| reset                      | rs    | Unstage changes after the selected commit                           |
| reset-hard                 | rsh   | Revert to the selected commit, discarding changes                   |
| cherry-pick                | cp    | Merge specific commits into the current branch                      |
| diff-commits               | di    | Select two commits and show the changes between them                |
| difftool-commits           | dit   | Select two commits and show the changes using difftool              |
| difftool-commits-dir-diff  | dd    | Select two commits and show the changed files by directory          |
| history                    | h     | Show the history of commands run                                    |
| history-dir                | hd    | Show the history of commands run in the current working directory   |
| stash-apply                | sta   | Apply the selected stash to the current branch                      |
| stash-pop                  | stp   | Apply the selected stash to the current branch and delete the stash |
| stash-message              | stm   | Stash changes with a message                                        |
| stash-drop                 | std   | Delete a stash
