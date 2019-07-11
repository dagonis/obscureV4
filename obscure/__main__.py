import argparse

import obscure

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('ip', help="The IP address you want to obscure.")
    args = parser.parse_args()
    o = obscure.ObscureIP(args.ip)