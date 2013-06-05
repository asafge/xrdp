import subprocess
import socket

import retry


def isProcess(name):
    ps = subprocess.Popen("ps -ef | grep %s | grep -v grep" %name, shell=True, stdout=subprocess.PIPE)
    out = ps.stdout.read()
    ps.stdout.close()
    ps.wait()
    return True if out else False


def killProcess(name):
    ps = subprocess.Popen("pkill %s" % name, shell=True)
    ps.wait()
    return


def isTcpListen(host, port):
    s = socket.socket()
    try:
        s.connect((host, port))
        return True
    except:
        return False


@retry(Exception, tries=3, delay=3, backoff=2)
def checkxrdp(path, host, port):
    print "Check process: %s \t" % path,
    if isProcess(path):
        print "[OK]"
        print "Check connection: \t"
        if isTcpListen(host, port):
            print "[OK]"
        else:
            print "[ERR]"
            print "Killing %s" %path
            killProcess(path)
    else:
        print "[ERR]"
        raise Exception()


if __name__ == "__main__":
    checkxrdp("xrdp", "0.0.0.0", "3389")
