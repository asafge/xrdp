import subprocess
import socket
import glob
import os

import retry


def is_process(name):
    print "Check process: %s \t" % name,
    ps = subprocess.Popen("ps -ef | grep %s | grep -v grep" %name, shell=True, stdout=subprocess.PIPE)
    out = ps.stdout.read()
    ps.stdout.close()
    ps.wait()
    if out:
        print "[OK]"
        return True
    else:
        print "[ERR]"
        return False


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
        print "Check connection: \t",
        s.connect((host, port))
        print "[OK]"
        return True
    except:
        print "[ERR]"
        return False


#@retry(Exception, tries=3, delay=3, backoff=2)
def check_xrdp(path, host, port):
    if is_process(path):
        if not is_tcp_listen(host, port):
            kill_process(path)
            rm_files("/var/run/xrdp.pid")
            #rm_files("/var/tmp/.xrdp/xrdp-[^sescv")
    else:
        return 


if __name__ == "__main__":
    check_xrdp("/usr/local/sbin/xrdp", "0.0.0.0", "3389")

