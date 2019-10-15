#!/bin/bash

CUSTOM_INSTALL_DIR="$1"

create_symlink () {
    local SCRIPT DIR INSTALL_DIR;
    SCRIPT=`realpath $0`
    DIR=`dirname $SCRIPT`

    if [ -n "$CUSTOM_INSTALL_DIR" ]; then
        # if a custom install directory was provided, symlink to there
        INSTALL_DIR=$(realpath "$CUSTOM_INSTALL_DIR")

        # only create the config directory if it doesn't exist
        if [ ! -d ~/.config/git-gud ]; then
            mkdir ~/.config/git-gud
        fi

        # save the install directory for uninstall
        echo "$INSTALL_DIR" > ~/.config/git-gud/install-dir
    else
        # default installation directory if none provided
        INSTALL_DIR="/usr/local/bin"
    fi

    # do not overwrite existing file in install directory
    if [ ! -f "$INSTALL_DIR/$1" ]; then
        ln -s "$DIR/src/$1" "$INSTALL_DIR/$1"
        echo "Created $INSTALL_DIR/$1"
    else
        echo "$INSTALL_DIR/$1 already exists"
    fi
}

create_symlink gud
