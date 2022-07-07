from italian_dictionary import scraper


# ------italian_dictionary-------
def get_definition(word, all_data=True, limit=None, properties=['definizione']):
    if all_data:
        return scraper.get_data(word, ['definizione', 'sillabe', 'lemma', 'pronuncia', 'grammatica', 'locuzioni'])
            # data = {'definizione': get_defs(soup), 'sillabe': get_sillabe(soup, word), 'lemma': get_lemma(soup),
    #         'pronuncia': get_pronuncia(soup), 'grammatica': get_grammatica(soup), 'locuzioni': get_locuzioni(soup),
    #         'url': url}
    else:
        data = scraper.get_data(word, all_data=False, properties=properties)
        if ('definizione' in properties):
            if limit is not None and len(data['definizione']) > limit:
                del data['definizione'][limit:]
        # If just one property is requested, return the property value, not the dictionary
        if len(properties) == 1:
            return data[properties[0]]
        else:
            return data
