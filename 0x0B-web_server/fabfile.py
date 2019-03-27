#!/usr/bin/env python3
from fabric import *
'''
Fabric task for deploying holberton web app
'''

tar_file = "holbertonwebapp.tar.gz"


@task
def pack(c):
    """Packs the files in the current directory

    Args:
        c : Frabic object
    """

    c.run("tar cpzf holbertonwebapp.tar.gz .")


@task
def deploy(ctc, usr="ubuntu", host="104.196.3.52", key_file=""):
    """deploy the packed files to the remote server at /tmp/ and unpack the
    files into /tmp/holbertonwebapp

    Args:
        usr     (str): username to ssh in with default to 'ubuntu'
        host    (str): IP address to ssh to default to my server
        key_file (str): ssh key file
    """
    with Connection(
            host,
            user=usr,
            connect_kwargs={"key_filename": key_file}
    ) as c:
        c.run("mkdir -p /tmp/holbertonwebapp")
        c.put(tar_file, "/tmp/")
        c.run("tar xpfz /tmp/{} -C /tmp/holbertonwebapp".format(tar_file))


@task
def clean(c):
    """remote the pack file localy
    """
    c.run("rm {}".format(tar_file))
