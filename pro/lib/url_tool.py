def clip_url(rorid):
    """give a rorid generate its openAlex link

    Args:
        rorid (str): the signal of one university

    Returns:
        str: a url can be interviewed in openAlex
    """
    base_url = "https://api.openalex.org/works?mailto=234058612@qq.com&per-page=50&filter=publication_year:2020,institutions.ror:"
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
        url_str = prefix + _.rstrip()
        return url_str
    else:
        return None