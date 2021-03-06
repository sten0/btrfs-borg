# btrfs-borg
Btrfs-borg makes snapshots and backs up a list of btrfs snapshotted subvolumes using Borg.  It will also optionally back up a list of directories without first creating snapshots for them.  It includes special support for containers managed by LXC's btrfs backend.  Finally it supports building manifests of directories that won't be backed up.  If you configure manifest support, please make sure that the target location of the manifest will be on one of the subvolumes that you back up.

eg: if SUBS=`@home rootfs`, but you also have a subvolume called @backups mounted at /home/backups, then 1) /home/backups will not be part of your borg backup, because btrfs-subvolume snap does not back up child subvolumes.  2) If your manifest goes to /home/backups/manifest then it will not be backed up.  If /home/backups is not a separate subvolume, then /home/backups/manifest will be part of the btrfs snapshot and part of the borg backup.

The master branch is a combined feature+debugging branch, but I tag releases before doing something experimental.

At some point I plan split it into a script+config file, because most people prefer to configure once and enable features as they need them, rather than reconfiguring with every new release...
