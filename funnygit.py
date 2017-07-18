import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('cmtmsg')
args = parser.parse_args()
msg = args.cmtmsg
subprocess.Popen("cd .", shell=True, stdout=subprocess.PIPE).stdout.read()
subprocess.Popen("git pull", shell=True, stdout=subprocess.PIPE).stdout.read()
subprocess.Popen("git add .", shell=True, stdout=subprocess.PIPE).stdout.read()
subprocess.Popen("git commit -m \""+msg +"\"", shell=True, stdout=subprocess.PIPE).stdout.read()
subprocess.Popen("git push", shell=True, stdout=subprocess.PIPE).stdout.read()
