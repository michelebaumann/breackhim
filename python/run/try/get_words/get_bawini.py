import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def find_word_in_website(base_url, word):
    visited_links = set()
    links_to_visit = [base_url]

    for _ in range(2):  # Go two levels deep
        new_links_to_visit = []
        for link in links_to_visit:
            if link not in visited_links:
                visited_links.add(link)
                try:
                    page = requests.get(link)
                    soup = BeautifulSoup(page.content, 'html.parser')
                    if word in soup.text:
                        print(f'Found "{word}" in {link}')
                    new_links_to_visit.extend(urljoin(link, new_link.get('href')) for new_link in soup.find_all('a') if new_link.get('href') and new_link.get('href').startswith(('http://', 'https://')))
                except requests.exceptions.RequestException:
                    pass  # Ignore invalid links
        links_to_visit = new_links_to_visit

if __name__ == '__main__':
    find_word_in_website('https://twitter.com/g_apru', 'baniwis')