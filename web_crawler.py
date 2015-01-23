__author__ = 'rsukla'

import requests
import re
import urlparse

# regex
email_re = re.compile(r'([\w\.,]+@[\w\.,]+\.\w+)')
link_re = re.compile(r'href="(.*?)"')


def crawl(url):

    result = set()

    req = requests.get(url)

    # Check if successful
    if(req.status_code != 200):
        return []

    # Find links
    links = link_re.findall(req.text)

    print "\nFound {} links".format(len(links))

    # Search links for emails
    for link in links:

        # Get an absolute URL for a link
        link = urlparse.urljoin(url, link)

        # Find all emails on current page
        result.update(email_re.findall(req.text))

    return result

if __name__ == '__main__':
    emails = crawl('http://www.realpython.com')

    print "\nScrapped e-mail addresses:"
    for email in emails:

        print email
    print "\n"

