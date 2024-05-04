#!/usr/bin/python3

import argparse
import os
from configparser import ConfigParser
import tarfile
import time
from datetime import datetime, timedelta
import subprocess

def config(file):
    if os.path.exists(file):
        try:
            config = ConfigParser()
            config.read(file)
            return config
        except Exception as e:
            raise e
    else:
        print('No config found')
        exit(1)

def sync():
    process = subprocess.run('offlineimap', shell=False)
    if process.returncode:
        exit(1)

def compress(src, dest):
    file = dest + '.tgz'
    name = os.path.basename(src)
    print('Start compressing ' + name)
    try:
        with tarfile.open(file, 'w:gz') as tar:
            tar.add(src, arcname=name)
        print('Finished compressing to ' + os.path.basename(file))
    except:
        print('Error while compressing ' + src)
        exit(1)

def prune(archives, retention):
    time_delta = {
        'm': timedelta(minutes=1),
        'h': timedelta(hours=1),
        'd': timedelta(days=1),
        'w': timedelta(weeks=1)
    }
    unit = retention.strip('0123456789')
    digits = int(retention[:-len(unit)])
    now = datetime.now()
    try:
        delta = time_delta[unit] * digits
        deadline = now - delta
    except KeyError:
        print('Unknown unit ' + unit)
        exit(1)
    print('Remove backups older than ' + str(deadline))
    for archive in os.listdir(archives):
        path = os.path.join(archives, archive)
        if datetime.fromtimestamp(os.path.getctime(path)) < deadline:
            try:
                os.remove(path)
                print('Remove ' + archive)
            except:
                print('Error while removing ' + path)
                exit(1)

def main(args):
    repos = config(args.config)
    sync()
    for repo in repos.sections():
        path = os.path.expanduser(repos[repo]['path'])
        retention = repos[repo]['retention']
        archives = os.path.join(args.target, repo)
        if not os.path.exists(archives):
            os.makedirs(archives)
        compress(src=path, dest=os.path.join(archives, repo+time.strftime("_%Y%m%d-%H%M%S")))
        prune(archives=archives, retention=retention)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Synchronize your remote Maildirs with the local repository (OfflineIMAP), archive them to backups and clean up older ones (run regularly with archiveimap.target and archiveimap.timer)')
    parser.add_argument('--config', type=str, default=os.path.join(os.path.dirname(__file__), '/etc/archiveimap/archiveimap.conf'), required=False, help='path to config file')
    parser.add_argument('--target', type=str, default=os.path.join(os.path.dirname(__file__), '/var/lib/archiveimap'), required=False, help='path to archive directory')
    args = parser.parse_args()
    main(args)
