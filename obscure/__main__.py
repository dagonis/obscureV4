import argparse
import ipaddress
import socket
import sys

import obscure

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('ip', help="The IP address you want to obscure.")
    parser.add_argument("--payload", help="Payload to insert obscured IP into. Use \I as replacement var.")
    args = parser.parse_args()
    try:
        ipaddress.IPv4Address(args.ip)
        ip = args.ip
    except:
        try:
            ip = socket.gethostbyname(args.ip)
        except:
            print(f"Input {args.ip} can't be turned into an ipaddress")
            sys.exit(-1)
    o = obscure.ObscureIP(ip)
    for obscure_ip in o.obscure_ips:
        if args.payload:
            print(args.payload.replace("\I", obscure_ip))
        else:
            print(obscure_ip)
