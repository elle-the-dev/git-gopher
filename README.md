# Git Gud

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

```
alias gg="gg-menu"
alias gitc="gg-checkout"
alias gitca="gg-checkout-all"
alias gitct="gg-checkout-tag"
alias gitbt="gg-branch-tag"
alias gitm="gg-merge"
alias gitmt="gg-merge-tag"
alias gitms="gg-merge-squash"
alias gitd="gg-delete"
alias gitup="git-upstream-push"
```

| command              | alias     | description                                              |
| -------------------- | --------- | -------------------------------------------------------- |
| gg-menu              | gg        | Open menu with these commands                            |
| gg-checkout          | gitc      | Checkout a local branch                                  |
| gg-checkout-all      | gitca     | Checkout a local or remote branch                        |
| gg-checkout-tag      | gitct     | Checkout a tag                                           |
| gg-branch-tag        | gitbt     | Create and checkout a new branch from a tag              |
| gg-merge             | gitm      | Merge a branch into the current branch                   |
| gg-merge-tag         | gitmt     | Merge a tag into the current branch                      |
| gg-merge-squash      | gitms     | Merge and squash a branch into the current branch        |
| gg-delete            | gitd      | Force delete a branch                                    |
| gg-upstream-push     | gitup     | Push the current branch to remote, setting the upstream  |
