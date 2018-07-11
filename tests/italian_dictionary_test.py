import pytest

from italian_dictionary import get_all_data, get_only_definition, exceptions, scraper

import bs4

class Test_ItalianDictionary():
    def test_getonlydef(self):
        word = 'cane'
        defs = get_only_definition(word)
        assert type(defs) is list
        assert len(defs) > 0
        limit_defs = get_only_definition(word, limit=1)
        assert len(limit_defs) == 1
    def test_alldata(self):
        word = 'albero'
        data = get_all_data(word)
        assert type(data) is dict
        for key in data.keys():
            assert data[key] is not None

class TestErrors:
    def test_errors(self):
        with pytest.raises(exceptions.WordNotFoundError):
            get_all_data('nfdifneif')
        with pytest.raises(exceptions.WordNotFoundError):
            get_only_definition('afefemmm')

class TestEngine:
    def test_engine(self):
        soup = scraper.get_soup("https://www.google.it")
        assert isinstance(soup, bs4.BeautifulSoup)
        lemma = scraper.get_lemma('cane')
        assert isinstance(lemma,str)
        pronuncia = scraper.get_pronuncia('cane')
        assert isinstance(pronuncia,str)
        grammatica = scraper.get_grammatica('cane')
        assert isinstance(grammatica,str)
        locuzione = scraper.get_locuzioni('cane')
        assert isinstance(locuzione,list)


