import pytest

from italian_dictionary.dictionary import get_definition
from italian_dictionary import exceptions

class Test_ItalianDictionary():
    def test_getonlydef(self):
        word = 'albero'
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
        for letter in data['lemma']:
            assert letter != ' '
    def test_specialcharacter(self):
        word = 'perchè'
        data = get_definition(word)
        assert type(data) is dict
        assert len(data) > 0
    def test_one_syllable(self):
        word = 'a'
        data = get_definition(word)
        assert type(data) is dict
        assert len(data) > 0
        assert len(data['sillabe']) == 1
    def test_verb(self):
        word = 'essere'
        data = get_definition(word)
        assert type(data) is dict
        assert len(data) > 0

class TestErrors:
    def test_errors(self):
        with pytest.raises(exceptions.WordNotFoundError):
            get_definition('nfdifneif')
        with pytest.raises(exceptions.WordNotFoundError):
            get_definition('afefemmm')
