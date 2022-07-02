#!/usr/bin/env python3

import os

def zeppelin():
    path = "/home/vagrant/"
    install_curl = "sudo yum install curl -y"
    wget = "wget https://dlcdn.apache.org/zeppelin/zeppelin-0.10.1/zeppelin-0.10.1-bin-all.tgz --no-check-certificate | tar -xvf zeppelin-0.10.1-bin-all.tgz"


    os.chdir(path)
    os.system(install_curl)
    os.system(wget)

if __name__ == "__main__":
    zeppelin()