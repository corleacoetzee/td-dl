from fabric.api import (local, put, run, env)

# the user to use for the remote commands
env.user = 'ec2-user'
# the servers where the commands are executed
env.hosts = ['52.214.3.82']


def pack():
    # build the package
    local('python setup.py sdist --formats=gztar', capture=False)


def deploy():
    # figure out the package name and version
    dist = local('python setup.py --fullname', capture=True).strip()
    filename = '%s.tar.gz' % dist

    # upload the package to the temporary folder on the server
    put('dist/%s' % filename, '/tmp/%s' % filename)

    # upload env
    run('mkdir -p /home/ec2-user/td_dl')
    run('mkdir -p /home/ec2-user/td_dl/scripts')
    run('mkdir -p /home/ec2-user/td_dl/media/uploads')
    run('sudo rm -rf /home/ec2-user/td_dl/venv')
    run('virtualenv -p python3 /home/ec2-user/td_dl/venv')

    # install the package in the application's virtualenv with pip
    run('/home/ec2-user/td_dl/venv/bin/pip install /tmp/%s' % filename)

    # remove the uploaded package
    run('rm -r /tmp/%s' % filename)

    # restart lineage service
    run('touch /home/ec2-user/td_dl/wsgi.py && \
         rm /home/ec2-user/td_dl/wsgi.py')
    put("wsgi.py", "/home/ec2-user/td_dl/wsgi.py")
    put("scripts/launchApp.sh",
        "/home/ec2-user/td_dl/scripts/launchApp.sh")
    put("scripts/importDBNeo4j.sh",
        "/home/ec2-user/td_dl/scripts/importDBNeo4j.sh")
    run("chmod 755 /home/ec2-user/td_dl/scripts/launchApp.sh")

    run("/home/ec2-user/td_dl/scripts/launchApp.sh stop && \
        /home/ec2-user/td_dl/scripts/launchApp.sh start")
