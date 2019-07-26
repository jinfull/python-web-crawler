# import requests, bs4
from fetch_hrefs import fetch_hrefs
from format_link_block import format_link_block


root = 'https://www.rescale.com/'
root_links = fetch_hrefs(root)

format_link_block(root, root_links)

for link in fetch_hrefs(root):
  curr_links = fetch_hrefs(link)
  format_link_block(link, curr_links)






  

# ==========================================

# Queue implementation to search iteratively with a Queue through every link and every link's associated link
# Forever (more than one level deep)

# links_queue = [root]
# links_set = set()

# while (links_queue):
#   # pop off the first item in links_queue and assign to curr_link
#   curr_link = links_queue.pop(0)
  
#   print (curr_link)

#   # get all links of the curr_link and assign (array) to curr_links
#   curr_links = fetch_hrefs(curr_link)

#   print (curr_links)

#   # iterate through of all the current link's links
#   # if they are already in our 'seen', we continue
#   # else add them to the end of our links_queue
#   for link in curr_links:
#     if link in links_set:
#       continue
#     else:
#       links_queue.append(link)
#       links_set.add(link)

#   print curr_links

# ==========================================
