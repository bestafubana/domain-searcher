import whois

def check_domains(filename):
    with open(filename, 'r') as file:
        names = file.read().splitlines()

    available_domains = []
    for name in names:
        domain = f"{name}.com"
        try:
            w = whois.whois(domain)
            if w.domain_name is None:
                print(f"{domain} is available!")
            else:
                print(f"{domain} is already taken.")
        except Exception as e:
            print(f"Could not check {domain}: {e}")
            # If it's a "No match" error, the domain is likely available
            if "No match for" in str(e):
                available_domains.append(domain)
    
    # Print just the available domains at the end
    print("\nAvailable domains:")
    for domain in available_domains:
        print(domain.upper())

if __name__ == "__main__":
    check_domains('domains.txt')
