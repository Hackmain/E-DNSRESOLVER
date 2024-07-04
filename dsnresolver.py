import dns.resolver

def resolve_dns_with_dnspython(domain_name):
    try:
        result = dns.resolver.resolve(domain_name, 'A')  # 'A' for IPv4 address
        for record in result:
            print(f"IPv4 Address for {domain_name}: {record.address}")
    except dns.resolver.NXDOMAIN:
        print(f"Domain {domain_name} does not exist.")
    except dns.resolver.NoAnswer:
        print(f"No DNS records found for {domain_name}")

# Example usage:
domain_to_resolve = "www.google.com"
resolve_dns_with_dnspython(domain_to_resolve)
print("follow me in instagram @esefkh740_")
