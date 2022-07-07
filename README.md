[![Build Status](https://travis-ci.org/sphoneix22/italian_dictionary.svg?branch=master)](https://travis-ci.org/sphoneix22/italian_dictionary)
[![codecov](https://codecov.io/gh/sphoneix22/italian_dictionary/branch/master/graph/badge.svg)](https://codecov.io/gh/sphoneix22/italian_dictionary)
[![PyPI version](https://badge.fury.io/py/italian-dictionary.svg)](https://badge.fury.io/py/italian-dictionary)
![Python](https://img.shields.io/pypi/pyversions/Django.svg)
![PRS](https://img.shields.io/badge/PRs-Welcome-green.svg)


# ItalianDictionary

This package searches for word meanings on [dizionario-italiano](https://www.dizionario-italiano.it).
## Install
```bash
pip install italian-dictionary
```
## Usage
```python
import italian_dictionary

# Use this to get only the meaning 
definition = italian_dictionary.get_definition('cane', limit=3, all_data=False) 

# Use this to get all data for a word (all_data default is True)
data = italian_dictionary.get_definition('albero')

# Use this to get a subset of the properties, for example 'grammatica' and 'pronuncia'
data = italian_dictionary('albero', all_data=False, properties=['grammatica', 'pronuncia'])

# Use this to get single property other than the meaning, for example 'lemma'
# Will return the value of the property, not a dictionary containing the one value.
data = italian_dictionary('albero', all_data=False, properties=['lemma'])

```
 ### Complete data response
 This function will return a dictionary like this:
 ```python
{
    'sillabe': ['al', 'be', 'ro'],
    'lemma': 'àlbero', 
    'pronuncia': ' /ˈalbero/', 
    'grammatica': ['sostantivo maschile'], 
    'definizione': ['pianta con fusto alto, legnoso, provvisto di rami nella parte superiore', 
                    "MARINERIA --  palo che regge i pennoni con le vele e tutta l'attrezzatura", 
                    'MECCANICA --  parte rotante, generalmente cilindrica, che, in una macchina, ha la funzione di trasmettere potenza meccanica da un organo a un altro'], 
    'locuzioni': ["linea d'asse o d'alberi di una nave", 
                'ad albero che cade dàgli dàgli', 
                'svasare un albero', 
                'albero portaelica', 
                'albero a calcese', 
                'albero castalio', 
                'albero matricino', 
                'alberi a mezzovento', 
                'albero optronico', 
                'albero pizzuto', 
                'andare agli alberi pizzuti', 
                'alberi rinterzati', 
                'albero del sego'] 
}
```
## Tests
To run tests you need ```pytest```.

When in project folder:
```python -m pytest```
