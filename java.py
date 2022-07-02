#!/usr/bin/env python3


import subprocess
import shlex

def java():
    ### A biblioteca shlex faz com que tudo que esteja dentro vire uma lista, pois o Popen interpreta comandos como lista.
    s = shlex.shlex("sudo yum install java -y", punctuation_chars=True)
    time = subprocess.Popen(s, 
    stdout=subprocess.PIPE, 
    stderr=subprocess.PIPE)
    output, err = time.communicate()
    print (output)

if __name__ == "__main__":
    java()