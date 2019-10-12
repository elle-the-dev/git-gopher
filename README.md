# git-gud

Improving the Git CLI experience with fzf

![image](https://i.imgur.com/oeupneT.gif)

## Requirements

[git](https://github.com/git/git) and [fzf](https://github.com/junegunn/fzf) must be installed.

## Installation

To automatically configure, run

```
sudo ./install.sh
```

which will symlink the commands to `/usr/local/bin`

An uninstall script is also provided to remove the symlinks

```
sudo ./uninstall.sh
```

To install manually, you can add the project directory to your `$PATH`

With or without the install script, to use the command aliases, the following definitions need to be added to your `.bashrc`, `.zshrc` or configuration file for whichever Unix shell being used.

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
```
## Usage

There are several commands added to make use of `fzf` and make interacting with basic git commands faster and easier.

Commands will list out the available branches or tags in `fzf` as a fuzzy searchable menu rather than requiring that they be provided up front.

| command                   | alias     | description                                              |
| ------------------------- | --------- | -------------------------------------------------------- |
| gg-menu                   | gg        | Open menu with these and other commands                  |
| gg-checkout-branch        | ggc       | Checkout a local branch                                  |
| gg-checkout-branch-remote | ggcr      | Checkout a local or remote branch                        |
| gg-checkout-tag           | ggct      | Checkout a tag                                           |
| gg-branch-tag             | ggbt      | Create and checkout a new branch from a tag              |
| gg-merge-branch           | ggm       | Merge a branch into the current branch                   |
| gg-merge-tag              | ggmt      | Merge a tag into the current branch                      |
| gg-merge-squash           | ggms      | Merge and squash a branch into the current branch        |
| gg-delete-branch          | ggd       | Delete a branch                                          |
| gg-delete-branch-force    | ggdf      | Force delete a branch                                    |
| gg-delete-tag             | ggdt      | Delete a tag locally                                     |
| gg-delete-tag-remote      | ggdtr     | Delete a tag both locally and on remote                  |
| gg-upstream-push          | ggup      | Push the current branch to remote, setting the upstream  |
| gg-push-tag               | ggpt      | Push a tag to a remote                                   |

## Custom Menu Options

If you want to add your own commands to the `gg-menu` command, created `~/.gg-options` with the options listed in it, one per line, with the command description separated by `|`.

Note: Commands cannot contain 2 consecutive spaces (`git log`: good, `git  log`: bad). The options are formatted using `column` and the two spaces are how the command column is delimited.

```
git dosomething      | Description of my command
git dosomethingelse  | Description of my other command
```
