# Find the type of IP Address using Regex

import re

def get_ip_type(ip):
    ipv4_pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    ipv6_pattern = r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'

    if re.match(ipv4_pattern, ip):
        parts = ip.split('.')
        if all(0 <= int(part) <= 255 for part in parts):
            return "IPv4"
    elif re.match(ipv6_pattern, ip):
        return "IPv6"
    return "Invalid"

if __name__ == "__main__":
    ip = input("Enter IP address: ")
    print(get_ip_type(ip))

# Code by Harshit