import urllib.request
import random


def read_Website(url):

    response = urllib.request.urlopen(url)  # get website
    html = response.read().decode("utf-8")  # convert
    html.lower()  # lowercase
    html.replace("'", '"')  # replace ' with "
    print(html)
    return html


def get_links(a_str, url):
    start = 0
    sub = "href"
    sub2 = ">"
    # opens url dump file
    add = random.getrandbits(50)  # generates random name
    urlname = "urldump" + str(add)
    urlout = urlname + ".txt"
    urls = open(urlout, "w")
    header = "dump of url" + url + "\n"
    urls.write(header)
    # scan through file
    print("searching startpoints")  # Debug
    while True:
        start = a_str.find(sub, start)  # find href

        if start == -1:
            return

        urlstart = a_str.find('"', start)  # find start of url

        urlend = a_str.find('"', urlstart + 1)  # find end of url
        print("suche ende")  # Debug
        print(urlstart, ":", urlend)  # Debug
        urlstring = a_str[urlstart + 1:urlend] + "\n"
        print(urlstring)  # prints url out
        urls.write(urlstring)  # writes string
        start += len(sub)
         # closes file
        print(urlname)
        urls.close

   


urlgiven = "http://python.org/"  # debug
#urlgiven = input("Url:")
html = read_Website(urlgiven)

get_links(html, urlgiven)
