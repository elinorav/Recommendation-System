import pandas as pd
import recoSystem
import csv

if __name__ == '__main__':
    reco = recoSystem.RecoSystem()
    data = pd.read_csv(r'ds_anstrex_tb.csv')
    df = pd.DataFrame(data, columns=['url'])
    for d in df.values:
        html_page, e = reco.scan_landing_page("https://www.oceandraw.com/worldwide/former-wrestlers-ta?utm_campaign=t-od-wrestlers-s-d-ww-091220&utm_medium=taboola&utm_source=taboola&utm_term=disqus-widget-safetylevel20longtail09")
        # html_page, e = reco.scan_landing_page(d[0])
        if html_page is not None:
            f = open('test.txt', 'w+')
            tags = html_page.find_all()
            str_res = ""
            for t in tags:
                str_res += t.text
            f.write(str_res)
