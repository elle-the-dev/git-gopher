# git-gud

Improving the Git CLI experience with fzf

## Requirements

[fzf](https://github.com/junegunn/fzf) must be installed.

## Installation

To automatically configure, run

```
sudo ./install.sh
```

which will symlink the commands to `/usr/local/bin`

To install manually, you can add the project directory to your `$PATH`

## Usage

There are several commands added to make use of `fzf` and make interacting with basic git commands faster and easier.

To use the aliases, the following definitions need to be added to your `.bashrc`, `.zshrc` or configuration file for whichever Unix shell being used.

Commands will list out the available branches or tags in `fzf` as a fuzzy searchable menu rather than requiring that they be provided up front.

```
alias gg="gg-menu"
alias ggc="gg-checkout"
alias ggca="gg-checkout-all"
alias ggct="gg-checkout-tag"
alias ggbt="gg-branch-tag"
alias ggm="gg-merge"
alias ggmt="gg-merge-tag"
alias ggms="gg-merge-squash"
alias ggd="gg-delete"
alias ggup="git-upstream-push"
alias ggdtr="git-delete-tag-remote"
```

| command              | alias     | description                                              |
| -------------------- | --------- | -------------------------------------------------------- |
| gg-menu              | gg        | Open menu with these commands                            |
| gg-checkout          | ggc       | Checkout a local branch                                  |
| gg-checkout-all      | ggca      | Checkout a local or remote branch                        |
| gg-checkout-tag      | ggct      | Checkout a tag                                           |
| gg-branch-tag        | ggbt      | Create and checkout a new branch from a tag              |
| gg-merge             | ggm       | Merge a branch into the current branch                   |
| gg-merge-tag         | ggmt      | Merge a tag into the current branch                      |
| gg-merge-squash      | ggms      | Merge and squash a branch into the current branch        |
| gg-delete            | ggd       | Force delete a branch                                    |
| gg-upstream-push     | ggup      | Push the current branch to remote, setting the upstream  |
| gg-push-tag          | ggpt      | Push a tag to a remote                                   |
| gg-delete-tag-remote | ggdtr     | Delete a tag both locally and on remote                  |
