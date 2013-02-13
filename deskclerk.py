
import time
import requests

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
        print r.content

    def repeat(self, form, repeat_field, repeat_values, static_data=None):
        """Repeatedly submit a form."""
        if static_data is not None:
            data = dict(static_data)
        else:
            data = dict()
        for count, value in enumerate(repeat_values):
            data.update({repeat_field: value})
            self.submit(form, data)
            if count < len(repeat_values) - 1:
                time.sleep(self.cooldown)
