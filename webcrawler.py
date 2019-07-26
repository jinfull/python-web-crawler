# import requests, bs4
from fetch_hrefs import fetch_hrefs


root = 'https://www.rescale.com/'

links_queue = [root]
links_set = set()

while (links_queue):
  # pop off the first item in links_queue and assign to curr_link
  curr_link = links_queue.pop(0)
  
  print (curr_link)

  # get all links of the curr_link and assign (array) to curr_links
  curr_links = fetch_hrefs(curr_link)

  print (curr_links)

  # iterate through of all the current link's links
  # if they are already in our 'seen', we continue
  # else add them to the end of our links_queue
  for link in curr_links:
    if link in links_set:
      continue
    else:
      links_queue.append(link)
      links_set.add(link)
    

  # print curr_links
  

# ==========================================
# ==========================================

# IGNORE ME


# fetch_hrefs('http://rescale.com')
# fetch_hrefs('http://jinfull.com') => ['http://github.com/jinfull', 'http://asano.herokuapp.com', ...]




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