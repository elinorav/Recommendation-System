import pandas as pd
import recoSystem
import csv

if __name__ == '__main__':
    reco = recoSystem.RecoSystem()
    data = pd.read_csv(r'ds_anstrex_tb.csv')
    df = pd.DataFrame(data, columns=['url'])
    index = 0
    for d in df.values:
        html_page, e = reco.scan_landing_page(d[0])
        if html_page is not None:
            f = open("page_"+str(index), 'w', encoding="utf-8")
            tags = html_page.find_all()
            str_res = ""
            for t in tags:
                str_res += t.text
            f.write(str_res)
            f.close()
        index += 1
