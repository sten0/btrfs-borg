#!/usr/bin/env python3
#
# btrfs-borg makes and backs up a list of btrfs snapshotted subvolumes
# using Borg.  It supports a list of other (probably) non-btrfs
# directory sources, and 1 second granularity of backups.
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public
# License v2 as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# Copyright (C) 2016-2018  Nicholas D Steeves <nsteeves@gmail.com>
#
# Requires: bash >=4.0, coreutils (specifically install, cut, tr,
#           and stat), btrfs-progs, borg
# Optional: ssh, gnupg || gpg


import os
import sys

btrfs_borg_version = 0.80
config_file = "/etc/default/btrfs-borg"


def check_config(str):
    print("Checking syntax of %s" % config_file)
    # exit with if there's an error
    # sys.exit(os.EX_CONFIG)


def load_config():
    check_config(config_file)
    print("Loading %s" % config_file)


def check_superpowers():
    if os.getuid() != 0:
        no_superpowers = """
Warning, normal user Detected!
Please run with superuser permissions.

Allowing normal users to create subvolumes is a denial of service
attack vector, because if more than about 300 subvolumes are created
btrfs can crash, or halt with an ENOSPC error; additionaly, performance
will suffer with more than ~250 subvolumes or more than a 50 snapshots
of a volume.

Finally root is required to remove subvolumes, unless
'user_subvol_rm_allowed' is specified for the volume in /etc/fstab.
That said, I firmly maintain that normal user subvolume creation and
deletion should be avoided for the foreseeable future.

Btrfs-borg will terminate now.
"""
        print(no_superpowers)
        sys.exit(os.EX_NOPERM)


def dummy_function():
    # pass is a null operation I can use for stubs
    pass


#

# I need to support "btrfs-borg -u UNIT_NAME" arguments/execution
# This will backup the unit defined in the YAML config
# Also, I need to support --dry-run, which will print what
# the program will do, without actually doing it.
# A --debug option would also be a good idea, both to help with debugging
# and to be completely transparent about what btrfs-borg is doing.

#


# main()
load_config()
check_superpowers()
