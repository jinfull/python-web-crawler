import requests, bs4

from fetch_hrefs import fetch_hrefs


root = 'https://www.rescale.com/'
root_res = requests.get(root)
root_res_soup = bs4.BeautifulSoup(root_res.text, 'html.parser')

# print root
# print root_res
# print root_res_soup

links_queue = [root]

while (links_queue):
  # print links_queue.pop(0)
  curr_link = links_queue.pop(0)
  




fetch_hrefs('http://rescale.com')
# fetch_hrefs('http://jinfull.com') => ['http://github.com/jinfull', 'http://asano.herokuapp.com', ...]




# ==========================================
# ==========================================


# links_arr = []
# links_set = set()

# for link in root_res_soup.find_all('a'):
#   curr_link = str(link.get('href'))

#   if (curr_link == 'None'):
#     continue

#   if (curr_link[0:4] == 'http'):
#     links_arr.append(curr_link)
#     links_set.add(curr_link)


# print "\n".join(links_arr)
# print links_set