import sys
import whois


def whoisnew(domain):
	print "\t\t\t[+] Gathering WhoIs Information...\n"
	whoisdict = {}
	w = whois.whois(domain)
	return w


def main():
	domain = sys.argv[1]
	print whoisnew(domain)
	print "\n-----------------------------\n"


if __name__ == "__main__":
	main()
