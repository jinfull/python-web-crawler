import sys, threading, time
import concurrent.futures

from fetch_hrefs import fetch_hrefs
from print_link_block import print_link_block

root = sys.argv[1]
queue = fetch_hrefs(root)

seen = set()

def main():
  print_link_block(root, queue)


  with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    while queue:
      # curr_link = queue.pop(0)
      executor.submit(webcrawler, queue)
      # print (queue)
    # curr_links = fetch_hrefs(curr_link)


    # print_link_block(curr_link, curr_links)
  print('-----------------------------------------------------------------------------------------')
  print (queue)
  print('-----------------------------------------------------------------------------------------')



def webcrawler(links): 
  # print('-----------------------------------------------------------------------------------------')
  # print (queue)
  # print('-----------------------------------------------------------------------------------------')

  curr_link = queue.pop(0)
  curr_links = fetch_hrefs(curr_link)

  print_link_block(curr_link, curr_links)

  for fetched_link in curr_links:
    if fetched_link in seen:
      break
    else:
      seen.add(fetched_link)
      queue.append(fetched_link)

  # queue += curr_links
  # links_set.add(queue.pop(0))

  print('task executed by {}'.format(threading.get_ident()))


# def main():
#   print_link_block(root, queue)

#   with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:

#     for link in queue:
#       executor.submit(webcrawler, link)


if __name__ == '__main__':
  # start_time = time.time()
  main()
  # duration = time.time() - start_time
  # print(f"This took {duration} seconds.")