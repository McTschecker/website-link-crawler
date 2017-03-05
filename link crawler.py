import  urllib.request
def read_Website (url):
	
	response = urllib.request.urlopen('http://python.org/')   #get website
	html = response.read().decode("utf-8")#convert
	html.lower()#lowercase
	html.replace("'",'"')#replace ' with "
##	print (html) debug
	
	return html
def get_links(a_str):
	start = 0
	sub= "href"
	sub2 = ">"
##	print ("searching startpoints")  Debug
	while True:
	   start = a_str.find(sub, start) #find href

	   if start == -1: return

	   urlstart = a_str.find('"',start  ) # find start of url

	   urlend = a_str.find('"', urlstart +1 ) #find end of url
##	   print ("suche ende") Debug
##	   print (urlstart, ":" , urlend) Debug
	   

	   print (a_str[urlstart +1  :urlend - 1 ]) #prints url out
	   start += len(sub)
              
##url = "http://python.org/"      # debug
url = input("Url:")
html = read_Website(url)
get_links(html)
