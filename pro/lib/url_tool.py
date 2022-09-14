import sys

def clip_url(data_yaml,rorid):
    """give a rorid generate its openAlex link

    Args:
        rorid (str): the signal of one university

    Returns:
        str: a url can be interviewed in openAlex
    """
    base_url = "https://api.openalex.org/{w}?mailto={m}&per-page={p}&filter={f}:{y},institutions.ror:".format( w = data_yaml['URL']['entity'],
                                                                                                                m = data_yaml['URL']['mailto'],
                                                                                                                p = data_yaml['URL']['per-page'],
                                                                                                                f = data_yaml['URL']['filter'],
                                                                                                                y = data_yaml['URL']['year']
                                                                                                                )
    #base_url = "https://api.openalex.org/works?mailto=675589296@qq.com&per-page=50&filter=publication_year:2011,institutions.ror:"
    additions = rorid + "&cursor="
    new_url = base_url + additions
    return new_url


def splice_url(doi):
    """give me a doi generate its openAlex link

    Args:
        doi (str): the doi of this paper

    Returns:
        str: a url can be interviewed in openAlex
    """
    if isinstance(doi,str):
        prefix = "https://api.openalex.org/works/https://doi.org/"
        url_str = prefix + doi.rstrip()
        return url_str
    else:
        return None