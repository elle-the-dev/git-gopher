#!/bin/bash

create_symlink () {
    local SCRIPT DIR;
    SCRIPT=`realpath $0`
    DIR=`dirname $SCRIPT`

    if [ ! -f "/usr/local/bin/$1" ]; then
        ln -s "$DIR/src/$1" "/usr/local/bin/$1"
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
