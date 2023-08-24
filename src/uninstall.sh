#!/bin/bash

remove_symlink () {
    if test -h "/usr/local/bin/$1"; then
        rm "/usr/local/bin/$1"
    fi
}

remove_symlink gg-menu
remove_symlink gg-checkout
remove_symlink gg-checkout-all
remove_symlink gg-checkout-tag
remove_symlink gg-branch-tag
remove_symlink gg-merge
remove_symlink gg-merge-tag
remove_symlink gg-merge-tag
remove_symlink gg-upstream-push
remove_symlink gg-get-branch-name
remove_symlink gg-get-tag-name
remove_symlink gg-push-tag
remove_symlink gg-delete-branch
remove_symlink gg-delete-branch-force
remove_symlink gg-delete-tag
remove_symlink gg-delete-tag-remote
