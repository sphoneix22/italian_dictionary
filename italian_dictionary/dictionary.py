from italian_dictionary import scraper


# ------italian_dictionary-------
def get_definition(word, all_data=True, limit=None):
    if all_data:
        return scraper.get_data(word)
    else:
        defs = scraper.get_data(word, all_data=False)
        if limit is not None and len(defs) > limit:
            del defs[limit:]
        return defs
