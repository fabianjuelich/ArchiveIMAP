# ArchiveIMAP
Synchronize your remote Maildirs with the local repository (OfflineIMAP), archive them in backups and clean up older ones (run regularly with systemd timer)
## Preconditions
### Install [OfflineIMAP](https://github.com/OfflineIMAP/offlineimap3)
- See the official [Quick Start Guide](https://www.offlineimap.org/doc/quick_start.html).
- If necessary, adjust the binary in the [Python script](./archiveimap.py). (Defaults to `offlineimap`)
- If you haven't already, add the passwords in plain text to `remotepass=` of the `[Repository xyz]` section in __offlineimap.conf__ (or offlineimaprc) to make sure the script can be run non-interactively.

## Setup

### Installation
1. `git pull https://github.com/fabianjuelich/ArchiveIMAP.git`
2. `cd ArchiveIMAP`
3. `./install.sh`
4. Check with `systemctl list-timers --all`

### Configuration
- Edit __/etc/archiveimap/archiveimap.conf__ to match your local Maildir repos and their storage time (m=minute, h=hour, d=day, w=week).
- Edit __/etc/systemd/system/archiveimap.timer__ to fulfill your routine requirements. (Defaults to __12am__ with up to 30min delay)
