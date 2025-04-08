import argparse
import os
import json

### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ###

try:
    import whois
    import socket
except ImportError:
    print("Please install ipwhois first: pip install ipwhois")
    exit(1)

### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ###

def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('--user_input', required=True, help='IP Address to Get Whois Information For')
        args = parser.parse_args()

        ip_address = args.user_input
        # ip_address = "8.8.8.8"  # Example IP address (Google's Public DNS)
        # # ip_address = "192.168.1.1" # Example of a private IP
        ###
        # Perform the WHOIS lookup
        w = whois.whois(ip_address)

        # The result 'w' is an object (or dictionary-like) containing parsed fields
        print(f"--- WHOIS lookup results for {ip_address} ---")
        if w:
                # Access specific fields if they exist (availability varies)
            print(f"Raw Text:\n{w.text}\n") # Often useful to see the raw server response
            print(f"Parsed Data:")
            # Print all attributes of the result object
            for key, value in w.items():
                    print(f"  {key}: {value}")
        else:
            print("No WHOIS data returned.")
            return 1
        ###
        return 0
    except socket.gaierror as e:
        print(f"Error resolving IP address or connecting: {e}")
    except Exception as e:
        print(f"[!] Error: {str(e)}")
        return 1

### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ###

if __name__ == "__main__":
    exit(main())
