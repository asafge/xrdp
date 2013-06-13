import subprocess
import socket
import glob
import os
import time


def print_row(action, param, status):
    print "   %-10s %-40s %-40s" % ("[OK]" if status else "[ER]", action, param)
    return status


def is_process(name, silent=False, invert=False):
    ps = subprocess.Popen("ps -ef | grep '%s$' | grep -v grep" %name, shell=True, stdout=subprocess.PIPE)
    out = ps.stdout.read().strip()
    ps.stdout.close()
    ps.wait()
    result = (len(out) is 0) if invert else (len(out) > 0)
    return print_row("Check process", name, result) if not silent else result


def start_process(name, silent=False):
    devnull = open('/dev/null', 'w')
    subprocess.Popen(name, shell=True, stdout=devnull)
    sleep(5, silent=True)
    return print_row("Starting process", name, is_process(name))


def kill_process(name):
    ps = subprocess.Popen("pkill %s" % name, shell=True)
    ps.wait()
    return print_row("Killing", name, is_process(name, silent=True, invert=True))


def rm_files(pattern):
    flag = True
    try:
        for f in glob.iglob(pattern):
            os.remove(f)
    except OSError:
        flag = False
    return print_row("Removing files", pattern, flag)


def is_tcp_listen(host, port):
    s = socket.socket()
    flag = True
    try:
        sleep(3, silent=True)
        s.connect((str(host), int(port)))
    except socket.error:
        flag = False
    return print_row("Checking TCP", "%s:%s" %(host,port), flag)


def sleep(sec, silent=False):
    if not silent:
        print_row("Waiting", "%s sec" % (sec), True)
    time.sleep(sec)

