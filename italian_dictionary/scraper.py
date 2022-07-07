import bs4
import urllib.request as request
from urllib import parse

from italian_dictionary import exceptions

URL = "https://www.dizionario-italiano.it/dizionario-italiano.php?parola={}100"


def build_url(base_url):
    scheme, netloc, path, query, fragment = parse.urlsplit(base_url)
    query = parse.quote(query, safe="?=/")
    return parse.urlunsplit((scheme, netloc, path, query, fragment))  # replacing special characters


def get_soup(url):
    sauce = request.urlopen(url).read()
    soup = bs4.BeautifulSoup(sauce, 'html.parser')
    return soup


def get_lemma(soup):
    lemma = soup.find('span', class_='lemma')
    if lemma is not None:
        return lemma.find(string=True, recursive=False).rstrip() # Getting only span text + removing white spaces at the end


def get_sillabe(soup, word):
    lemma = soup.find(class_='lemma')
    small_list = lemma.find_all_next('small')
    for el in small_list:
        if el.parent not in lemma.children:
            try:
                sillabe = el.span.find(string=True, recursive=False)
            except AttributeError:  # Word has no syllable division
                return [word]
            break

    split_indexes = [pos for pos, char in enumerate(sillabe) if char == "|"]
    # necessario perchè le sillabazioni contengono gli accenti di pronuncia
    tmp = list(word)
    for i in split_indexes:
        tmp = tmp[0:i] + ["|"] + tmp[i:]
        sillabe = ''.join(tmp).split("|")
    return sillabe


def get_pronuncia(soup):
    pronuncia = soup.find('span', class_="paradigma")
    return pronuncia.text[10:]


def get_grammatica(soup):
    gram = soup.find_all('span', class_="grammatica")
    return [x.text for x in gram]


def get_locuzioni(soup):
    bad_loc = soup.find_all('span', class_='cit_ita_1')
    loc = [x.text for x in bad_loc]
    return loc


def get_defs(soup):
    defs = []
    for definitions in soup.find_all('span', class_='italiano'):
        children_content = ''
        for children in definitions.findChildren():
            if children.string is None:
                continue
            try:
                if children.attrs['class'][0] in ('esempi', 'autore'):
                    continue
                else:
                    children_content += children.text
                    children_content += ' '
                    children.decompose()
            except KeyError:
                continue
        if children_content != '':
            defs.append(f"{children_content.upper()} -- {definitions.text.replace('()', '')}")
        else:
            defs.append(definitions.text)
    if len(defs) == 0:
        raise exceptions.WordNotFoundError()
    return defs


def get_data(word, properties, all_data=True):
    url = build_url(URL.format(word))
    soup = get_soup(url)
    data = {}

    if len(properties) == 0:
        # Should never happen if this function is only called from get_definition() in dictionary.py
        raise LookupError("No properties specified.")
    for property in properties:
        if property == "definizione":
            data["definizione"] = get_defs(soup)
        elif property == "lemma":
            data["lemma"] = get_lemma(soup)
        elif property == "sillabe":
            data["sillabe"] = get_sillabe(soup, word)
        elif property == "pronuncia":
            data["pronuncia"] = get_pronuncia(soup)
        elif property == "grammatica":
            data["grammatica"] = get_grammatica(soup)
        elif property == "locuzioni":
            data["locuzioni"] = get_locuzioni(soup)
        elif (property in data) is False:
            raise exceptions.InvalidPropertyError("Property {} not found in data returned from {}".format(property, url))
            
    return data
