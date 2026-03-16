import argparse
import ipaddress
import socket
import sys

from obscure import ObscureIP


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('ip', help="The IP address you want to have obscured.")
    parser.add_argument("--payload", help="Payload to insert obscured IP into. Use \\I as replacement var.")
    args = parser.parse_args()
    try:
        ipaddress.IPv4Address(args.ip)
        ip = args.ip
    except Exception:
        try:
            ip = socket.gethostbyname(args.ip)
        except Exception:
            print(f"Input {args.ip} can't be turned into an ipaddress")
            sys.exit(-1)
    o = ObscureIP(ip)
    for obscure_ip in o.obscure_ips:
        if args.payload:
            print(args.payload.replace("\\I", obscure_ip))
        else:
            print(obscure_ip)


if __name__ == '__main__':
    main()
