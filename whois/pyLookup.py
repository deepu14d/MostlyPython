import whois
import sys

domain = sys.argv[1]
domain_info = whois.whois(domain)

print(domain_info)