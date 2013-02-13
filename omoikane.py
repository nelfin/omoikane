
import time

import bs4
import requests

class SousChef(object):
    """Organise underlings to determine column values."""
    def __init__(self):
        self.soup = None
        self.callbacks = dict()

    def soupify(self, handle):
        """Produce a tag soup from a HTML file."""
        self.soup = bs4.BeautifulSoup(handle)

    def open(self, filename):
        """Open an HTML file and process it."""
        with open(filename) as html_file:
            self.soupify(html_file)

    def rowify(self, matcher):
        """Find sampled portions of tag soup."""
        return matcher(self.soup)

    def register(self, **callbacks):
        """Add one or more callbacks by keyword arguments."""
        self.callbacks.update(callbacks)

    def process(self, row_pattern):
        """TODO: magic."""
        rows = self.rowify(row_pattern)
        for row in rows:
            columns = dict((key, f(row))
                           for key, f in self.callbacks.iteritems())


class DeskClerk(object):
    """
    Fill out form inputs and save resulting reports.
    """
    def __init__(self, base_url, cooldown=2.0, init=True):
        self.base_url = base_url
        self.session = requests.session()
        self.cooldown = cooldown
        if init:
            self.session.get(base_url)

    def submit(self, form, data):
        """Auto-fill a form "intelligently"."""
        form_url = self.base_url + form
        r = self.session.post(form_url, data)
        return r.content

    def repeat(self, form, repeat_field, repeat_values, static_data=None):
        """Repeatedly submit a form."""
        if static_data is not None:
            data = dict(static_data)
        else:
            data = dict()
        def repeater():
            for count, value in enumerate(repeat_values):
                data.update({repeat_field: value})
                yield self.submit(form, data)
                if count < len(repeat_values) - 1:
                    time.sleep(self.cooldown)
        return repeater()


