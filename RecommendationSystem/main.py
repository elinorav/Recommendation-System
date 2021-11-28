from urllib.request import urlopen


if __name__ == '__main__':
    landing_page = input('Please enter a URL of a lending page')
    print('You have entered:' + landing_page)
    page = urlopen(landing_page)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    print(html)


    title_index = html.find("<title>")
    start_index = title_index + len("<title>")
    end_index = html.find("</title>")
    title = html[start_index:end_index]
    print('The title of the page is: ' + title)


