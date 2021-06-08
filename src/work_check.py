import requests
from bs4 import BeautifulSoup as BS
import codecs
from random import choice




headers = [
    {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},

    {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},

    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:53.0) Gecko/20100101 Firefox/53.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
           ]

# url = 'https://www.work.ua/ru/jobs-kyiv-python/'
# resp = requests.get(url, headers=headers)
# soup = BS(resp.content, 'html.parser')
# domain = 'https://www.work.ua'
# jobs = []
# errors = []
# if resp.status_code == 200:
#     soup = BS(resp.content, 'html.parser')
#     main_div = soup.find('div', id='pjax-job-list')
#     if main_div:
#         div_list = main_div.find_all('div', attrs={'class': 'job-link'})
#         for div in div_list:
#             # print(div, end='\n\n\n\n\n\n\n') # обрати внимание, на какие элементы разделяется div_list # CHECK
#             title = div.find('h2')
#             # print(title.a.string)  # CHECK
#             href = title.find('a')
#             # print(href, domain + href['href']) # CHECK
#             content = div.p.text#.strip()
#             # print(content, type(content))    # CHECK
#             logo = 'Unknown'
#             if div.img:
#                 # print(div.img)    # CHECK
#                 logo = div.img['alt']
#                 # print(logo)
#             jobs.append({
#                 'title': title.a.string,
#                 'url': domain + href['href'],
#                 'description': content,
#                 'logo': logo
#             })
#             # print(title.a.string,domain+href['href'],sep='\n',end='\n\n\n') # CHECK
#     else:
#         errors.append({'url': url, 'cause': 'Div does not exist', 'status_code': resp.status_code,})
#         pass
# else:
#     errors.append({'url': url, 'cause': 'Page does not response', 'status_code': resp.status_code})
#
#
#
#
#
# def rabota_CHECK():
#     jobs = []
#     errors = []
#     domain = 'https://rabota.ua'
#     url = 'https://rabota.ua/zapros/python/%d0%ba%d0%b8%d0%b5%d0%b2'
#     resp = requests.get(url=url, headers=headers)
#     soup = BS(resp.content, 'html.parser')
#
#     # CHECK find() -----------------------------------------------------------------------------------------------------
#     print('soup = BS(resp.content, "html.parser")', type(soup), *dir(soup), type(soup).mro(), sep='\n', end='\n'*10)
#     # CHECK find() -----------------------------------------------------------------------------------------------------
#
#     if resp.status_code == 200:
#         table = soup.find('table', id='ctl00_content_vacancyList_gridList')
#         if table:
#             tr_list = table.find_all('tr', attrs={'id': True}) # там id указаны как id="8360908" (любое другое число)
#
#             # CHECK find() --------------------------------------------------------------------------------------------------------------
#             print('soup.find("tag", attrs={"k":"v"})', type(table), *dir(table), type(table).mro(), sep='\n',
#                   end='\n' * 10)
#             # CHECK find() --------------------------------------------------------------------------------------------------------
#
#             # CHECK find_all() -------------------------------------------------------------------------------------------------------
#             print('soup.all_find("tag", attrs={"k":"v"})', type(tr_list),
#                   *dir(tr_list), type(tr_list).mro(), sep='\n', end='\n'*10)
#             # CHECK find_all() ---------------------------------------------------------------------------------------------------
#         # print(*table, sep='\n'*15)
#
# rabota_CHECK()
#
# # print(*jobs,sep='\n')
#
# # div_list (после метода find_all) - представляет из себя практически список. Но это не список.
# # Это объект <class 'bs4.element.ResultSet'>
# # метод find дает другой тип данных - <class 'bs4.element.Tag'>
# # Ознакомься внимательно с тремя предыдущими строчками
# # аттрибуты text и string достают текст между тегами (string если мало текста, text если много)
# # -------------------------------------------------------------------------------------
# # print(*dir(div_list), type(div_list),sep='\n')
# # print(*div_list,sep='\n\n\n\n\n\n\n')
# # print(type(div_list).mro()) # <class 'bs4.element.ResultSet'> унаследован от list
# # -------------------------------------------------------------------------------------
# запомни метод tagStack у soup. Этот метод возвращает список из всех тегов. Но не как метод find_all,
# Очень полезный lifehak можно узнать весь список тегов вызвав у soup find_all() без аргументов:
# all_tags_in_documents = soup.find_all()
# где мы ищем конкретное имя тега и находим все такие теги
# к каждому тегу можно обращаться attrs. Если у тега есть аттрибуты, то он вернет словарь из этих аттрибутов
# помимо find и find_all есть еще select. select может искать классы тегов .some-class и
# id тегов #some-id
#
#
# # with codecs.open('work.txt', 'w', 'utf-8') as f:
# #     f.write(str(jobs))
#
#
#
# url_hh = 'https://hh.ru/search/vacancy?area=1&fromSearchLine=true&st=searchVacancy&text=python'
#
# resp_hh = requests.get(url=url_hh, headers=headers)

# with codecs.open('hh_work.html', 'w', 'utf-8') as f:
#     f.write(str(resp_hh.text))

"""
{'title': title,
         'url': href,
         'description': content,
         'company': company,
         'city_id': city,
         'language_id': language,}
"""

def record_jobs(jobs, title, href, content, company):
    jobs.append(
        {'title': title,
         'url': href,
         'description': content,
         'company': company,}

    )


# url = 'https://www.rabota.ru/vacancy/?query=python&location.regionId=3&location.name=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0&sort=relevance'
# resp = requests.get(url, choice(headers))
#
# soup = BS(resp.content, 'html.parser')
# domain = 'https://www.rabota.ru'
# jobs = []
# errors = []
# if resp.status_code == 200:
#     main = soup.find('main', attrs={'class': 'page__main'})
#     if main:
#         artile_list = main.find_all('article', attrs={'itemscope': 'itemscope',})
#         for article in artile_list:
#             header = article.find('header')
#             if header:
#                 title = header.a.text.strip()
#                 href = header.a['href']
#                 div = article.find('div', attrs={'itemscope': 'itemscope'})
#                 company = 'unknown'
#                 if div:
#                     try:
#                         company = div.a['title'].strip()
#                     except KeyError:
#                         company = div.a.text
#                 content = article.find('div', attrs={'class': 'vacancy-preview-card__content'}).text.strip()
#                 record_jobs(jobs=jobs,
#                             title=title,
#                             href=domain+href,
#                             content=str(content),
#                             company=company)
#             else:
#                 print('таааа-шаааа 1')
#     else:
#         print('таааа-шаааа 2')
# else:
#     print('таааа-шаааа 3')



# print(*jobs,sep='\n')

url = "https://www.superjob.ru/vacancy/search/?keywords=python&geo%5Bt%5D%5B0%5D=4&order_by%5Bupdated_at%5D=desc"
domain = 'https://www.superjob.ru'
resp = requests.get(url=url, headers=choice(headers))

soup = BS(resp.content, 'html.parser')
items = soup.find_all('div', attrs={'class': 'f-test-search-result-item'})
jobs = []
for i, div in enumerate(items):
    a = div.a


    if a != None:
        title = div.a.text
        href = domain + div.a['href']
        company = 'unknown'
        content = ''
        all_spans = div.find_all('span')
        for span in all_spans:
            try:
                company = span.a.text
                break
            except AttributeError:
                pass
        record_jobs(jobs, title, href, content, company)


print(*jobs, sep='\n')



"""
        'title': title,
         'url': href,
         'description': content,
         'company': company,
"""
# with open('../super_job.html', 'w', encoding='utf-8') as f:
#     f.write(str(resp.text))



url = "https://www.superjob.ru/vacancy/search/?keywords=python&geo%5Bt%5D%5B0%5D=4&order_by%5Bupdated_at%5D=desc"
yandex = "https://rabota.yandex.ru/moskva/vakansii/?text=python&top_days=3&sort=cr_date"
s = "https://spb.careerist.ru/vakansii/middle-python-developer-24184610.html"
v = "https://job-piter.ru/vacancy/view/73825463/?_openstat=rabota.yandex.ru;;3597289800112853163;organic"

# with codecs.open('content.txt', 'w', 'utf-8') as p:
#     p.write(str(resp.text))

