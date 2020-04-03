import pytest

from italian_dictionary.dictionary import get_definition
from italian_dictionary import exceptions, scraper

import bs4

class Test_ItalianDictionary():
    def test_getonlydef(self):
        word = 'cane'
        defs = get_definition(word, all_data=False)
        assert type(defs) is list
        assert len(defs) > 0
        limit_defs = get_definition(word, limit=1, all_data=False)
        assert len(limit_defs) == 1
    def test_alldata(self):
        word = 'albero'
        data = get_definition(word)
        assert type(data) is dict
        for key in data.keys():
            assert data[key] is not None

class TestErrors:
    def test_errors(self):
        with pytest.raises(exceptions.WordNotFoundError):
            get_definition('nfdifneif')
        with pytest.raises(exceptions.WordNotFoundError):
            get_definition('afefemmm')
        with pytest.raises(exceptions.WordNotFoundError):
            scraper.get_lemma('adaff')

class TestEngine:
    def test_engine(self):
        soup = scraper.get_soup("https://www.google.it")
        assert isinstance(sillabe, list)
        lemma = scraper.get_lemma('cane')
        assert isinstance(soup, bs4.BeautifulSoup)
        sillabe = scraper.get_sillabe('cane')
        assert isinstance(lemma,str)
        pronuncia = scraper.get_pronuncia('cane')
        assert isinstance(pronuncia,str)
        grammatica = scraper.get_grammatica('cane')
        assert isinstance(grammatica,str)
        locuzione = scraper.get_locuzioni('cane')
        assert isinstance(locuzione,list)


