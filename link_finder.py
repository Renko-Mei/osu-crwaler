from html.parser import HTMLParser
from urllib import parse

class LinkFinder(HTMLParser):

    # Initializer
    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    # Overwrite built in method
    def handle_starttag(self, tag, attrs):
        # Only consider links
        if tag == 'a':
            # An attribute tupple is <href = link_value>
            for (attribute, value) in attrs:
                if attribute == 'href':
                    # Join relative url with base url
                    # Do nothing if value is a full url
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url)

    # Output method
    def page_links(self):
        return self.links

    def error(self, message):
        pass
