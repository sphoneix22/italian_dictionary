from italian_dictionary import scraper

URL = "https://www.dizionario-italiano.it/dizionario-italiano.php?parola={}"


# ------italian_dictionary-------
def get_only_definition(word, limit=None):
     defs = scraper.get_defs(word)
     if limit is not None and len(defs) > limit:
         del defs[limit:]
     return defs

def get_all_data(word):
    return scraper.get_all_data(word)



