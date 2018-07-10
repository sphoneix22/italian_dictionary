import bs4
import urllib.request as request

from italian_dictionary import exceptions

URL = "https://www.dizionario-italiano.it/dizionario-italiano.php?parola={}"

def get_soup(url):
    sauce = request.urlopen(url).read()
    soup = bs4.BeautifulSoup(sauce, 'lxml')
    return soup


def get_lemma(word):
    soup = get_soup(URL.format(word))
    lemma = soup.find('span', class_='lemma')
    if lemma is not None:
        return lemma.text
    else:
        raise exceptions.WordNotFoundError()

def get_pronuncia(word):
    soup = get_soup(URL.format(word))
    pronuncia = soup.find('span', class_="paradigma")
    return pronuncia.text[10:]


def get_grammatica(word):
    soup = get_soup(URL.format(word))
    gram = soup.find('span', class_="grammatica")
    return gram.text

def get_locuzioni(word):
    soup = get_soup(URL.format(word))
    bad_loc = soup.find_all('span', class_='cit_ita_1')
    loc = [x.text for x in bad_loc]
    return loc


def get_defs(word):
    soup = get_soup(URL.format(word))
    defs = []
    for definitions in soup.find_all('span', class_='italiano'):
        children_content = ''
        for children in definitions.findChildren():
            children_content += children.text
            children.decompose()
        if children_content != '':
            defs.append(f"{children_content.upper()} -- {definitions.text}")
        else:
            defs.append(definitions.text)
    if len(defs) == 0:
        raise exceptions.WordNotFoundError()
    return defs


def get_all_data(word):
    data = {'lemma': None, 'pronuncia': None,'grammatica': None,  'definizione': None, 'locuzioni': None,}
    data['lemma'] = get_lemma(word)
    data['pronuncia'] = get_pronuncia(word)
    data['grammatica'] = get_grammatica(word)
    data['locuzioni'] = get_locuzioni(word)
    data['definizione'] = get_defs(word)
    return data