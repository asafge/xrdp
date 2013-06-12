import subprocess
import socket

import retry


def is_process(name):
    ps = subprocess.Popen("ps -ef | grep %s | grep -v grep" %name, shell=True, stdout=subprocess.PIPE)
    out = ps.stdout.read()
    ps.stdout.close()
    ps.wait()
    return True if out else False


def kill_Process(name):
    ps = subprocess.Popen("pkill %s" % name, shell=True)
    ps.wait()
    return


def is_tcp_listen(host, port):
    s = socket.socket()
    try:
        s.connect((host, port))
        return True
    except:
        return False


@retry(Exception, tries=3, delay=3, backoff=2)
def check_xrdp(path, host, port):
    print "Check process: %s \t" % path,
    if is_process(path):
        print "[OK]"
        print "Check connection: \t"
        if is_tcp_listen(host, port):
            print "[OK]"
        else:
            print "[ERR]"
            print "Killing %s" %path
            kill_process(path)
    else:
        print "[ERR]"
        raise Exception()


if __name__ == "__main__":
    check_xrdp("xrdp", "0.0.0.0", "3389")
