#!/bin/bash

CUSTOM_INSTALL_DIR="$1"

remove_symlink () {
    if [ -n "$CUSTOM_INSTALL_DIR" ]; then
        DIR=$(realpath "$CUSTOM_INSTALL_DIR")
    elif [ -f ~/.config/git-gud/install-dir ]; then
        DIR=$(cat ~/.config/git-gud/install-dir)
    else
        DIR="/usr/local/bin"
    fi

    if test -h "$DIR/$1"; then
        rm "$DIR/$1"
    fi
}

remove_symlink gg-menu
remove_symlink gg-checkout-branch
remove_symlink gg-checkout-branch-remote
remove_symlink gg-checkout-tag
remove_symlink gg-branch-tag
remove_symlink gg-merge-branch
remove_symlink gg-merge-tag
remove_symlink gg-merge-squash
remove_symlink gg-upstream-push
remove_symlink gg-push-tag
remove_symlink gg-delete-branch
remove_symlink gg-delete-branch-force
remove_symlink gg-delete-tag
remove_symlink gg-delete-tag-remote
remove_symlink gg-reset
remove_symlink gg-reset-hard
remove_symlink gg-diff-commits
remove_symlink gg-difftool-commits
remove_symlink gg-difftool-commits-dir-diff

remove_symlink gg-get-branch-name
remove_symlink gg-get-tag-name
remove_symlink gg-get-commit-hash

if [ -d ~/.config/git-gud ]; then
    rm -rf ~/.config/git-gud
fi
