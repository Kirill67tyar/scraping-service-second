from bs4 import BeautifulSoup as BS
import requests
import json

url = 'https://earthquake.usgs.gov/fdsnws/event/1/'
response = requests.get(url=url)

if response.status_code == 200:

    soup = BS(response.content, 'html.parser')
    # print(soup.prettify())
    # print(soup.select('.page-header')[0].text)
    # print(soup.select('#url'))
    li = soup.select('li')
    li2 = soup.find_all('li')
    # print(li, type(li), len(li), dir(li),sep='\n\n')
    # print(li == li2)
    # print(type(li2), len(li2))
    lst = li
    lst.append('та-ша')
    # print(*li,sep='\n'*5)
    li.remove('та-ша')
    # for l in li:
    #     if l.a:
    #         print(l.a['href'])
    # all_a = soup.find_all('a')
    # print('\n'*5)
    # # print(all_a)
    # for a in all_a:
    #     if 'https' in a.get('href'):
    #         print(a.get('href'))

    # print(type(soup.text), len(soup.text), type(soup.get_text()), len(soup.get_text()))
    # for l in li:
    #     if l.a:
    #         print(l.a.attrs)
    all_div = soup.find_all('div')
    # for div in all_div:
    #     print(div.attrs)
    # print(*dir(soup),sep='\n')
    # with open('../../../../BS.txt', 'w') as f:
    #     for method in dir(soup):
    #         f.write(method + '\n')
    # print(soup.get_attribute_list('alert info"'))
    # print(soup.tagStack)

    # for tag in all_tags_in_document:
    #     print(tag, end='\n'*10)


    # for t in soup.handle_data():
    #     print(t)
    all_tags_in_document = soup.find_all()
    # print(all, len(all),sep='\n')
    # for tag in all_tags_in_document:
    #     if tag.text:
    #         print(tag.text.strip())
        # print(tag.attrs)
    divs = soup.select('.horizontal-scrolling')
    # print(divs, type(divs), len(divs), sep='\n')
    body = soup.find('body')
    # print(body.contents, type(body.contents),len(body.contents), sep='\n')
    # for tag in body.contents:
    #     print(tag,type(tag),sep='\n', end='\n'*10)
    # print(body.contents[1].a.next_element.next_element,end='\n\n')
    # print(body.contents[1].a.next_sibling.next_sibling,end='\n\n')
    # print(body.contents[1].a.find_next_sibling(attrs={'class': 'jumplink-navigation'}), end='\n\n')
    # print(body.contents[1])

response = requests.get('https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2019-01-01&endtime=2019-02-02&latitude=51.51&longitude=-0.12&maxradiuskm=2000&minmagnitude=2')

print(json.dumps(response.json(), indent=5))

