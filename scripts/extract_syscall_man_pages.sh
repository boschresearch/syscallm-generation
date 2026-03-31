#!/bin/bash

# Copyright (c) 2026 Robert Bosch GmbH and its subsidiaries.
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# __author__      = "Min Hee Jo"
# __copyright__   = "Copyright 2026, Robert Bosch GmbH"
# __license__     = "AGPL"
# __version__     = "3.0"
# __email__       = "minhee.jo@de.bosch.com"

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