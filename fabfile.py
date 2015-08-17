import subprocess
import sys
import os.path
import requests
from fabric.api import run, env, sudo
from fabric.contrib import files

LOGIN_HOST = 'tools-login.wmflabs.org'
DEST_TOOL = 'cluebotng'
DEST_DIR = '/data/project/%s/apps/cbng_interface' % DEST_TOOL
REPO_URL = 'https://github.com/DamianZaremba/cbng-interface.git'

# Internal settings
env.hosts = [LOGIN_HOST]
env.use_ssh_config = True
env.sudo_user = 'tools.%s' % DEST_TOOL
env.sudo_prefix = "/usr/bin/sudo -ni"


def check_workingdir_clean():
    p = subprocess.Popen(['git', 'diff', '--exit-code'],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    p.communicate()

    if p.returncode != 0:
        print('There are local, uncommited changes.')
        print('Refusing to deploy.')
        sys.exit(1)


def check_remote_up2date():
    p = subprocess.Popen(['git', 'ls-remote', REPO_URL, 'master'],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    remote_sha1 = p.communicate()[0].split('\t')[0].strip()

    p = subprocess.Popen(['git', 'rev-parse', 'HEAD'],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    local_sha1 = p.communicate()[0].strip()

    if local_sha1 != remote_sha1:
        print('There are comitted changes, not pushed to github.')
        print('Refusing to deploy.')
        sys.exit(1)


def setup():
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
    sudo('jstop webgrid-generic')


def start():
    sudo('jstart -q webgrid-generic %s' %
         os.path.join(DEST_DIR, 'bin', 'tools_run'))


def migrate():
    ve_activate = os.path.join(DEST_DIR, 've', 'bin', 'activate')
    sudo('. "%(ve)s" && cd %(dir)s && ./manage.py migrate' % {
        've': ve_activate,
        'dir': DEST_DIR
    })


def update_code():
    sudo('cd "%(dir)s" && git pull origin master' % {'dir': DEST_DIR})


def test_api():
    r = requests.get('http://tools.wmflabs.org/cluebotng/api/version')
    if r.status_code != 200:
        print('Deploy failed - API broken')
        sys.exit(2)

    if r.text.strip() != os.system('git rev-parse HEAD').strip():
        print('Deploy failed - version mis-match')
        sys.exit(3)


def deploy():
    check_workingdir_clean()
    check_remote_up2date()

    update_code()
    migrate()
    test_api()
