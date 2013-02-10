
import bs4

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


