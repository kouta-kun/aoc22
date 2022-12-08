import requests
def readfile(f):
    with open(f,'r') as fin:
        return fin.readline().strip()
SESSION_ID = readfile('session.env')

def get_input(day):
    for line in requests.get(
        f'https://adventofcode.com/2022/day/{day}/input',
        headers={
            'Cookie':f'session={SESSION_ID}',
            'User-Agent':
            'https://github.com/kouta-kun/aoc22 AoC Automation by darkfm@vera.com.uy'
        }).content.decode('UTF-8').split('\n'):
        yield line
