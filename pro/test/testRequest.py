import requests

url = "https://api.openalex.org/works?mailto=zd675589295@qq.com&per-page=50&filter=publication_year:2020,institutions.ror:https://ror.org/02kkvpp62&cursor="



proxy = '202.55.5.209:8090' 
proxies = {
     'http': 'http://' + proxy
}



resp = requests.get(url,verify=False,proxies=proxies)
print(resp.status_code,resp.json())  