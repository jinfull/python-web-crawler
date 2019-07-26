import requests
import bs4

def fetch_hrefs(link):
  links_set = set()
  links_arr = []

  try: 
    link_res = requests.get(link)
    link_res_soup = bs4.BeautifulSoup(link_res.text, 'html.parser')
  except: 
    return []

  for link in link_res_soup.find_all('a'):
    curr_link = str(link.get('href'))

    if (curr_link == 'None'):
      continue

    if (curr_link[0:4] == 'http' and curr_link not in links_set):
      links_set.add(curr_link)
      links_arr.append(curr_link)

  return(links_arr)