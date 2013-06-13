import subprocess
import socket
import glob
import os
import time



def is_process(name):
    print "Check process: %s \t" % name,
    ps = subprocess.Popen("ps -ef | grep '%s$' | grep -v grep" %name, shell=True, stdout=subprocess.PIPE)
    out = ps.stdout.read()
    ps.stdout.close()
    ps.wait()
    if out:
        print "[OK]"
        return True
    else:
        print "[ERR]"
        return False


def start_process(name):
    print "Starting process: %s \t" % name,
    devnull = open('/dev/null', 'w')
    ps = subprocess.Popen(name, stdout=devnull)
    sleep(3)
    return is_process(name)


def kill_process(name):
    print "Killing %s" %name
    ps = subprocess.Popen("pkill %s" % name, shell=True)
    ps.wait()


def rm_files(pattern):
    files_iter = glob.iglob(pattern)
    for f in files_iter:
        os.remove(f)


def is_tcp_listen(host, port):
    s = socket.socket()
    try:
        print "Check TCP connection to %s:%s: \t" %(host,port), 
        s.connect((host, int(port)))
        print "[OK]"
        return True
    except:
        print "[ERR]"
        return False


def sleep(sec):
    print "Waiting %s sec..." %sec
    time.sleep(sec)

