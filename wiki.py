import requests

class WikiClient():
    """A wrapper around MediaWiki's API

    Exposes all methods needed to request data from MediaWiki's APIs

    Args:
        url (str): The url of the MediaWiki powered site.
            ex. https://www.wikidata.org/w/api.php

    Attributes:
        url (str) The url of the MediaWiki powered site
            ex. https://www.wikidata.org/w/api.php
    """

    def __init__(self, url):
        self.url = url


    def get_backlinked_pages(self, title, limit=0):
        """Finds all pages that backlink to the `title` page

        Args:
            title (str): The title of the page that is backlinked to
            limit (int, optional): The total number of pages to return.
                Use 0 to return all pages. Defaults to 0.

        Returns:
            list(str): The titles of pages that backlink to `title`
        """
        # The largest batch size allowed by WikiData is 500
        # Ensure our limit is less than that.
        if limit > 500:
            limit = 500

        page_ids = list()
        params = {
                'action':'query',
                'format':'json',
                'list':'backlinks',
                'bltitle':title,
                'bllimit':limit
                }


        need_to_continue = True
        while need_to_continue:
            r = requests.get(self.url, params=params)
            data = r.json()
            for backlink in data['query']['backlinks']:
                page_ids.append(backlink['title'])

            # Check if we need to continue making requests
            if limit != 0 and len(page_ids) >= limit:
                need_to_continue = False
            elif 'continue' not in data:
                need_to_continue = False
            else:
                params['continue'] = data['continue']['continue']
                params['blcontinue'] = data['continue']['blcontinue']

        return page_ids

    def get_page_data(self, title):
        """Returns the full text of the requested page

        Args:
            title (str): The title of the page to return

        Returns:
            str: The `str` representation of the requested page's JSON
        """

        params = {
                'action':'wbgetentities',
                'format':'json',
                'ids':title,
                'languages':'en'
                }

        r = requests.get(self.url, params=params)
        data = r.json()

        return data
