import subprocess
import sys

from fabric.api import env, sudo
from fabric.contrib import files

import os.path
import requests

LOGIN_HOST = 'tools-login.wmflabs.org'
TOOL_DIR = None
DEST_DIR = None
REPO_URL = 'https://github.com/DamianZaremba/cbng-interface.git'

# Internal settings
env.hosts = [LOGIN_HOST]
env.use_ssh_config = True
env.sudo_prefix = "/usr/bin/sudo -ni"


def _check_workingdir_clean():
    p = subprocess.Popen(['git', 'diff', '--exit-code'],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    p.communicate()

    if p.returncode != 0:
        print('There are local, uncommited changes.')
        print('Refusing to deploy.')
        sys.exit(1)


def _check_remote_up2date():
    p = subprocess.Popen(['git', 'ls-remote', REPO_URL, 'master'],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    remote_sha1 = p.communicate()[0].split(b'\t')[0].strip()

    p = subprocess.Popen(['git', 'rev-parse', 'HEAD'],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    local_sha1 = p.communicate()[0].strip()

    if local_sha1 != remote_sha1:
        print('There are comitted changes, not pushed to github.')
        print('Refusing to deploy.')
        sys.exit(1)


def _setup():
    PARENT_DEST_DIR = os.path.dirname(DEST_DIR)
    if not files.exists(PARENT_DEST_DIR):
        sudo('mkdir -p "%(dir)s"' % {'dir': PARENT_DEST_DIR})

    if not files.exists(DEST_DIR):
        print('Cloning repo')
        sudo('git clone "%(url)s" "%(dir)s"' %
             {'dir': DEST_DIR, 'url': REPO_URL})

    VE_DIR = os.path.join(DEST_DIR, 've')
    if not files.exists(VE_DIR):
        sudo('virtualenv "%(dir)s"' % {'dir': VE_DIR})


def stop():
    sudo('webservice uwsgi-plain stop')


def start():
    sudo('webservice uwsgi-plain start')


def _migrate():
    ve_activate = os.path.join(DEST_DIR, 'bin', 've_wrapper')
    sudo('cd %(dir)s && %(ve)s ./manage.py migrate' % {
        've': ve_activate,
        'dir': DEST_DIR
    })


def _update_code():
    ve_activate = os.path.join(DEST_DIR, 'bin', 've_wrapper')
    sudo('cd "%(dir)s" && git reset HEAD --hard' % {'dir': DEST_DIR})
    sudo('cd "%(dir)s" && git clean -fd' % {'dir': DEST_DIR})
    sudo('cd "%(dir)s" && git pull origin master' % {'dir': DEST_DIR})
    sudo('cd "%(dir)s" && %(ve)s pip install -r requirements.txt --upgrade' % {
        'dir': DEST_DIR,
        've': ve_activate,
    })
    sudo('rsync %s/uwsgi.ini %s/uwsgi.ini' % (DEST_DIR, TOOL_DIR))


def _test_api():
    r = requests.get('http://tools.wmflabs.org/cluebotng/report/api/v1/')
    if r.status_code != 200:
        print('Deploy failed - non 200 returned')
        sys.exit(2)


def _deploy():
    global TOOL_DIR, DEST_DIR
    assert TOOL_DIR is not None
    assert DEST_DIR is not None

    _setup()
    _check_workingdir_clean()
    _check_remote_up2date()

    stop()
    _update_code()
    _migrate()
    start()
    _test_api()

def deploy():
    global TOOL_DIR, DEST_DIR
    TOOL_DIR = '/data/project/cluebotng/'
    DEST_DIR = '/data/project/cluebotng/apps/cbng_interface'
    env.sudo_user = 'tools.cluebotng'
    _deploy()
