# ------------------------------------------------------- Запуск Django в не самого проекта
import os, sys


proj = os.path.dirname(os.path.abspath('manage.py'))    # устанавливаем абсолютный путь

# тут мы добавляем путь в системные переменные путей
sys.path.append(proj)

os.environ['DJANGO_SETTINGS_MODULE'] = 'scraping_service.settings'
# for p in os.environ:
#     print(f'{p} - {os.environ[p]}')
import django

django.setup()
# ------------------------------------------------------- Запуск Django в не самого проекта
import codecs
import asyncio
import json
from datetime import date
from django.shortcuts import get_object_or_404
from django.db import DatabaseError
from django.contrib.auth import get_user_model
from scraping.parsers import *
from scraping.models import City, Language, Vacancy, Error, Url
from scraping.utils import get_object_or_null




parsers = (
            (work, 'work'),
            (rabota, 'rabota'),
            (job_dou, 'dou'),
            (djinni, 'djinni'),
            (rabota_ru, 'rabota_ru'),
            (super_job, 'super_job'),
           )

User = get_user_model()

jobs, errors = [], []

def get_settings():
    qs = User.objects.filter(mailing=True).values()# здесь в values() можно добавить city_id и language_id
    # а то он достает все поля User. А может и не добавлять, может так быстрее.
    settings_lst = set((q['city_id'], q['language_id']) for q in qs)
    return settings_lst


def get_url(_settings):
    """
                json.loads нужен только для postgresql в production сервере
                на локальном нужно разкомментить строку без json.loads

                """
    qs = Url.objects.all().values()
    url_dict = {(q['city_id'], q['language_id']): q['url_data'] for q in qs}
    urls = []
    for pair in _settings:
        if pair in url_dict:
            tmp = {}
            tmp['city'] = pair[0]
            tmp['language'] = pair[-1]
            url_data = url_dict.get(pair, {})
            if isinstance(url_data, str):
            ## для production сервера:
                tmp['url_data'] = json.loads(url_data)
            else:
            ## для локального сервера:
                tmp['url_data'] = url_data
            urls.append(tmp)
    return urls


# await запускает функцию, и при этом происходт переключение на другое выполнение,
# тем самым достигается распараллеливание, и как следствие - увеличение скорости работы
# но перед этим необходимо пометить, что наша функция и потавить ключевое слово async перед
# определением фукции.
# executor - исполнитель (implementer, performer)
# async def main(value):
#     func, url, city, language = value
#     job, err = await loop.run_in_executor(None, func, url, city, language)
#     jobs.extend(job)
#     errors.extend(err)




_settings = get_settings()
url_list = get_url(_settings)
# print(*url_list,sep='\n')



# import time
# start = time.time()

# # ---------------------------------------------------------------------    Асинхронный способ выполнения
# # for i in range(10):
# loop = asyncio.get_event_loop() #  сздаем loop для асинхронного программирования
# tmp_tasks = [(func, data['url_data'].get(key, None), data['city'], data['language'])
#                  for data in url_list
#                  for func, key in parsers]
#
# ## когда wait вызывается - он регулирует переключение интерпритатора, для той  или иной таски
# tasks = asyncio.wait([loop.create_task(main(f)) for f in tmp_tasks])
# loop.run_until_complete(tasks)
# loop.close()
# # ---------------------------------------------------------------------    Асинхронный способ выполнения

            #                   OR
"""
python run_scraping.py
"""
# =====================================================================    Неасинхронный способ выполнения
for i in range(10):
    for data in url_list:
        for func, key in parsers:
            if not isinstance(data['url_data'], str):
                url = data['url_data'].get(key, None)
                if url:
                    # вот эта строчка - блокирующий вызов. Самый узкий проход нашего кода, бутылочное горлышко
                    # весь код не может быть выполнен, пока не пройдут эти функции
                    # поэтому мы здесь и используем асинхронный подход
                    j, e = func(url, city=data['city'], language=data['language'])
                    jobs.extend(j)
                    errors.extend(e)
            else:
                print(data['url_data'], type(data['url_data']))
# =====================================================================    Неасинхронный способ выполнения

# print((time.time() - start) / 10)
# print(*jobs,len(jobs), sep='\n')
# print(errors)


for vacancy in jobs:

    v = Vacancy(**vacancy)
    try:
        v.save()
    except DatabaseError:
        pass

errors_exp = [{
        'url': 'https://www.amalgama-lab.com/songs/m/misfits/mars_attacks.html',
        'cause': 'HZ',
        'status_code': 200,}]


"""
for production server choose section 1 ------- 
for local server choose section 2 ========
"""
# if errors_exp:
if errors:
    err = get_object_or_null(Error, datestamp=date.today())
    if err:
        # 1 -----------------------------------------
        # for production server (db PostgreSQL)
        data = err.data
        if isinstance(data, str):
            data = json.loads(err.data)
            data['errors'].extend(errors)
            err.data = json.dumps(data)
            err.save()
        # --------------------------------------------

        # # 2 ============================================
        # # for local server (db SQLite):
        else:
            err.data['errors'].extend(errors)
            err.save()
        # #  ============================================

    else:
        # 1 -----------------------------------------
        # for production server (db PostgreSQL)
        err = Error(data=json.dumps({'errors': errors, 'feedback': [],})).save()
        # --------------------------------------------

        # # 2 ============================================
        # # for local server (db SQLite):
        # err = Error(data={'errors': errors, 'feedback': [],}).save()
        # #  ============================================


# ------------------------------------------------------------------
# if __name__ == '__main__':
#     print(*jobs, sep='\n')
#     print('count jobs -', len(jobs))
#     print('errors -', errors)

# with codecs.open('work.txt', 'w', 'utf-8') as f:
#     f.write(str(jobs))