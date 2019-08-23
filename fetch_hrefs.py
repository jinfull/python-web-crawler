import requests
import bs4

def fetch_hrefs(link):
  links_set = set()
  links_arr = []

  try: 
    res = requests.get(link)
    res_soup = bs4.BeautifulSoup(res.text, 'html.parser')
  except: 
    return []

  for link in res_soup.find_all('a'):
    curr_link = str(link.get('href'))
    # print(type(link.get('href')))
    # print(type(curr_link))

    # if (curr_link == 'None'):
    #   continue

    if (curr_link[0:4] == 'http' and curr_link not in links_set):
      links_set.add(curr_link)
      links_arr.append(curr_link)

  
  print (links_arr)
  return(links_arr)


link = 'http://jinfull.com'

fetch_hrefs(link)