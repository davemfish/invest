import unittest

from natcap.invest import keywords


class TestKeywords(unittest.TestCase):
    """Test and validate characteristics of the keywords vocabulary."""

    def test_unique(self):
        """Test values, aliases, and urls are all unique."""
        values = set()  # values and aliases together must be unique
        urls = set()
        for keyword in keywords.to_list():
            self.assertNotIn(
                keyword.name, values,
                msg=f'\n duplicate value {keyword.name} on {keyword}')
            values.add(keyword.name)
            for alias in keyword.aliases:
                self.assertNotIn(
                    alias, values,
                    msg=f'\n duplicate alias {alias} on {keyword}')
                values.add(alias)
            if keyword.url:
                self.assertNotIn(
                    keyword.url, urls,
                    msg=f'\n duplicate url on {keyword}')
                urls.add(keyword.url)
