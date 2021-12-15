from threading import Lock
from threading import Thread
from time import sleep

import recoSystem
import pandas as pd
import csv


def extract_title(url):
    reco = recoSystem.RecoSystem()
    result = reco.extract_title_from_landing_page(url)
    if not result:
        return ["Can't extract the data from this url... working on it:)"]
    return result


def extract_keywords(url):
    reco = recoSystem.RecoSystem()
    result = reco.extract_keywords_from_landing_page(url)
    if len(result) == 0:
        return ["Can't extract the data from this url... working on it:)"]
    return result

def scrap(url):
    reco = recoSystem.RecoSystem()
    result = reco.scrap_page(url)
    if len(result) == 0:
        return ["Can't extract the data from this url... working on it:)"]
    return result


def thread_extract_data_from_url(lock_for_count, lock_for_file):
    lock_for_file.acquire()
    data = pd.read_csv(r'ds_anstrex_tb.csv')
    data["keywords"] = ""

    df = pd.DataFrame(data, columns=['url'])
    lock_for_file.release()
    while True:
        # init
        i = -1

        lock_for_count.acquire()
        global curr_index
        global count

        if curr_index > count:
            return
        i = curr_index
        print(str(i))

        curr_index += 1
        lock_for_count.release()
        try:
            list = extract_keywords(df.url[i])
            sleep(1)
            lock_for_file.acquire()

            data['keywords'].iloc[i] = list
            data.to_csv("ds_anstrex_tb.csv", index=False)
            lock_for_file.release()
        except Exception as e:
            print("index: " + str(i) + ": " + str(e))


def print_hi():
    while True:
        print("hi")


if __name__ == '__main__':
    url = "https://www.sonoviastore.co.il/blogs/news/%D7%94%D7%9E%D7%A1%D7%9B%D7%94-%D7%94%D7%98%D7%95%D7%91%D7%94-%D7%91%D7%99%D7%95%D7%AA%D7%A8-%D7%9C%D7%98%D7%99%D7%A1%D7%95%D7%AA-%D7%91%D7%A9%D7%A0%D7%AA-2021-%D7%A1%D7%95%D7%A0%D7%95%D7%91%D7%99%D7%94?utm_source=taboola&utm_medium=referral&utm_campaign=TB_Blog_AirTravel_IL_PC&tblci=GiDbJRndUImP9rc80Mls7KW1gFpDdEMCGlkTelmGFUrFzyDq3U8oxaqc6ZT4jY_QAQ#tblciGiDbJRndUImP9rc80Mls7KW1gFpDdEMCGlkTelmGFUrFzyDq3U8oxaqc6ZT4jY_QAQ"
    print(scrap(url))
    # i = 0
    # data = pd.read_csv(r'ds_anstrex_tb.csv')
    #
    # data["keywords"] = ""
    #
    # df = pd.DataFrame(data, columns=['url'])

    # count urls
    # count = df.count()[0]
    # curr_index = 0
    # lock_for_count = Lock()
    # lock_for_file = Lock()
    # for i in range(5):
    #     thread = Thread(target=thread_extract_data_from_url, args=(lock_for_count, lock_for_file))
    #     thread.start()

    # executor.submit(thread_extract_data_from_url)

    #
    # for d in df.values:
    #    try:
    #        list = extract_keywords(d[0])
    #        data['keywords'].iloc[i] = list
    #        data.to_csv("ds_anstrex_tb.csv", index=False)
    #    except Exception as e:
    #        print("index: " + str(i) + ": " + str(e))
    #    print(str(i))
    #    i = i + 1
