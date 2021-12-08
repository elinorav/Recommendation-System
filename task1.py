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


if __name__ == '__main__':
	i = 0
	data = pd.read_csv(r'ds_anstrex_tb.csv')
	data["keywords"] = ""

	df = pd.DataFrame(data, columns=['url'])
	for d in df.values:
		try:
			list = extract_keywords(d[0])
			data['keywords'].iloc[i] = list
			data.to_csv("ds_anstrex_tb.csv", index=False)
		except Exception as e:
			print("index: " + str(i) + ": " + str(e))
		i = i+1
