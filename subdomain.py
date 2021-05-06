import requests
import pyfiglet

def domain_scanner(domain_name, sub_domnames):
    print('----URL after scanning subdomains----')

    for subdomain in sub_domnames:

        url = f"https://{subdomain}.{domain_name}"

        try:
            requests.get(url)

            print(f'[+] {url}')

        except requests.ConnectionError:
            pass


if __name__ == '__main__':
    print("Made By")
    result = pyfiglet.figlet_format("Harshit Kumar")
    print(result)
    dom_name = input("Enter the Domain Name:")

    with open('subdomain.txt', 'r') as file:
        name = file.read()

        sub_dom = name.splitlines()

    domain_scanner(dom_name, sub_dom)

