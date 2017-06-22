#!/bin/sh

install -oroot -groot -m644 btrfs-borg-configuration /etc/default/btrfs-borg
install -oroot -groot -m755 btrfs-borg /usr/local/bin/btrfs-borg
install -d -oroot -groot -m755 /usr/local/etc
install -oroot -groot -m755 possible-future-btrfs-borg-config.csv /usr/local/etc/borg-config.csv
