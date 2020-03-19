from time import sleep
from subprocess import run
if __name__ == "__main__":
    branch = "master"
    minutes = 15
    while True:
        run(['python3', 'scrapeHelperBoi.py'])
        run(['git', 'fetch'])
        run(['git', 'pull', 'origin', 'master'])
        run(['git', 'add', '.'])
        run(['git', 'commit', '-m', 'Update : '])
        run(['git', 'push', 'origin', 'master'])
        sleep(60 * minutes)