#!/bin/bash

CUSTOM_INSTALL_DIR="$1"

create_symlink () {
    local SCRIPT DIR INSTALL_DIR;
    SCRIPT=`realpath $0`
    DIR=`dirname $SCRIPT`

    if [ -n "$CUSTOM_INSTALL_DIR" ]; then
        INSTALL_DIR=$(realpath "$CUSTOM_INSTALL_DIR")

        if [ ! -d ~/.config/git-gud ]; then
            mkdir ~/.config/git-gud
        fi

        echo "$INSTALL_DIR" > ~/.config/git-gud/install-dir
    else
        INSTALL_DIR="/usr/local/bin"
    fi

    if [ ! -f "$INSTALL_DIR/$1" ]; then
        ln -s "$DIR/src/$1" "$INSTALL_DIR/$1"
    fi
}

create_symlink gg-menu
create_symlink gg-checkout-branch
create_symlink gg-checkout-branch-remote
create_symlink gg-checkout-tag
create_symlink gg-branch-tag
create_symlink gg-merge-branch
create_symlink gg-merge-tag
create_symlink gg-merge-squash
create_symlink gg-upstream-push
create_symlink gg-get-branch-name
create_symlink gg-get-tag-name
create_symlink gg-push-tag
create_symlink gg-delete-branch
create_symlink gg-delete-branch-force
create_symlink gg-delete-tag
create_symlink gg-delete-tag-remote
create_symlink gg-reset
create_symlink gg-reset-hard
