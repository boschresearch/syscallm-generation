#!/bin/bash

# Copyright (c) 2025 Robert Bosch GmbH
# SPDX-License-Identifier: AGPL-3.0

# variables
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKING_DIR="$(dirname "$(dirname "$SCRIPT_DIR")")"
MAN_DIR="$WORKING_DIR/data/man"
MISSING_FILE="${MAN_DIR}/missing.txt"

# clean up
rm -rf "$MAN_DIR" 
mkdir -p "$MAN_DIR"

rm -f "$MISSING_FILE"

# check for required packages
if ! dpkg -s manpages-dev >/dev/null 2>&1; then
    echo "manpages-dev not found. Installing..."
    sudo apt update
    sudo apt install -y manpages-dev
fi

if ! dpkg -s auditd >/dev/null 2>&1; then
    echo "auditd not found. Installing..."
    sudo apt update
    sudo apt install -y auditd
fi

# get list of syscalls
syscalls=$(ausyscall --dump | awk 'NR > 1 {print $2}' | sort | uniq)

# extract man pages
for syscall in $syscalls; do
    if man 2 "$syscall" > /dev/null 2>&1; then
        man 2 "$syscall" > "${MAN_DIR}/${syscall}.txt" 2>/dev/null
        sed -i '1,2d' "${MAN_DIR}/${syscall}.txt"
        sed -i '/^STANDARDS/,/^[A-Z ]\{3,\}$/d' "${MAN_DIR}/${syscall}.txt"
        sed -i '/^SEE ALSO/Q' "${MAN_DIR}/${syscall}.txt"
        echo "$syscall"	
    else
        echo "$syscall" >> "$MISSING_FILE"
    fi
done