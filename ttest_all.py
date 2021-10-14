import os, sys, getopt
import subprocess

print("executando os.system")
os.system("ls -lath")


print("executando subprocess.run")
run = subprocess.run(["ls", "-lathr"])


print(run.stdout, run.stderr)


