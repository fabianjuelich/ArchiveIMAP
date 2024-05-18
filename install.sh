# Install ArchiveIMAP 
cp archiveimap.py /usr/bin/
mkdir /etc/archiveimap
cp archiveimap.conf /etc/archiveimap/
mkdir /var/lib/archiveimap
# Activate regular autostart
cp archiveimap.service /etc/systemd/system/
cp archiveimap.timer /etc/systemd/system/
systemctl enable archiveimap.timer
