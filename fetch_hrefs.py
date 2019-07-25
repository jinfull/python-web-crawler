import requests, bs4

# fetch_hrefs('http://jinfull.com') => ['http://github.com/jinfull', 'http://asano.herokuapp.com', ...]
def fetch_hrefs(link):
  links_arr = []

  link_res = requests.get(link)
  link_res_soup = bs4.BeautifulSoup(link_res.text, 'html.parser')

  for link in link_res_soup.find_all('a'):
    curr_link = str(link.get('href'))

    if (curr_link == 'None'):
      continue

    if (curr_link[0:4] == 'http'):
      links_arr.append(curr_link)

  print links_arr

fetch_hrefs('http://rescale.com')