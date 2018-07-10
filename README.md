# ItalianDictionary

This package searches for word meanings on [dizionario-italiano](www.dizionario-italiano.it).

## Usage
```python
import italian_dictionary

# Use this to get only the meaning 
definition = italian_dictionary.get_only_definition('cane', limit=3) #Optional: specify max number of defs

#Use this to get all datas of a word
datas = italian_dictionary.get_all_data('albero')
```
 #### get_all_data response
 This function will return a dictionary like this:
 ```python
{
'lemma': 'àlbero', 
'pronuncia': ' /ˈalbero/', 
'grammatica': 'sostantivo maschile', 
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