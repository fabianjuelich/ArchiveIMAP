# ArchiveIMAP
Synchronize your remote Maildirs with the local repository (OfflineIMAP), archive them in backups and clean up older ones (run regularly with systemd timer)
## Preconditions
### Install [OfflineIMAP](https://github.com/OfflineIMAP/offlineimap3)
- See the official [Quick Start Guide](https://www.offlineimap.org/doc/quick_start.html).
- If necessary, adjust the binary in the [Python script](./archiveimap.py). (Defaults to `offlineimap`)

## Setup
### Install ArchiveIMAP
1. `git pull https://github.com/fabianjuelich/ArchiveIMAP.git`
2. `cd ArchiveIMAP`
3. `cp archiveimap.py /usr/bin/`
4. `mkdir /etc/archiveimap`
5. `cp archiveimap.conf /etc/archiveimap/`
6. `mkdir /var/lib/archiveimap`

### Activate regular autostart
- If you haven't already, add the passwords in plain text to `remotepass=` in offlineimap.conf to make sure the script can be run non-interactively.
1. `cp archiveimap.service /etc/systemd/system/`
2. `cp archiveimap.timer /etc/systemd/system/`
3. `systemctl enable archiveimap.timer`
4. Check with`systemctl list-timers --all`

### Configure
- Edit __/etc/archiveimap/archiveimap.conf__ to match your local Maildir repos and their storage time (m=minute, h=hour, d=day, w=week).
- Edit __/etc/systemd/system/archiveimap.timer__ to fulfill your routine requirements. (Defaults to __12am__ with up to 30min delay)
