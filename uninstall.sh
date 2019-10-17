#!/bin/bash

CUSTOM_INSTALL_DIR="$1"

remove_symlink () {
    if [ -n "$CUSTOM_INSTALL_DIR" ]; then
        # if a directory is provided, remove from that directory
        DIR=$(realpath "$CUSTOM_INSTALL_DIR")
    elif [ -f ~/.config/git-gud/install-dir ]; then
        # check custom directory from install
        DIR=$(cat ~/.config/git-gud/install-dir)
    else
        # default install directory
        DIR="/usr/local/bin"
    fi

    # remove the symlink if it exists
    if test -h "$DIR/$1"; then
        rm "$DIR/$1"
        echo "Deleted $DIR/$1"
    fi
}

remove_symlink gud

# if config directory exists, delete it
if [ -d ~/.config/git-gud ]; then
    rm -rf ~/.config/git-gud
    echo "Deleted ~/.config/git-gud"
fi

SCRIPT=`realpath $0`
DIR=`dirname $SCRIPT`
hook_file="$DIR/.git/hooks/post-merge"
if [ -f "$hook_file" ]; then
    rm "$hook_file"
fi
