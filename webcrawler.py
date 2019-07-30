import sys, threading, time
import concurrent.futures

from fetch_hrefs import fetch_hrefs
from print_link_block import print_link_block

root = sys.argv[1]
root_links = [] + fetch_hrefs(root)

queue = []
seen = set()

def main():
  print_link_block(root, root_links)

  while root_links:
    curr_link = root_links.pop(0)
    curr_links = fetch_hrefs(curr_link)

    for link in curr_links:
      if link in seen:
        continue
      else:
        root_links.append(link)
        seen.add(link)

    print_link_block(curr_link, curr_links)


def webcrawler(link): 
  curr_links = fetch_hrefs(link)
  print_link_block(link, curr_links)

  # root_links += curr_links
  # links_set.add(root_links.pop(0))

  # print('task executed by {}'.format(threading.current_thread()))


# def main():
#   print_link_block(root, root_links)

#   with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
#     # while len(root_links) > 0:
#       # executor.submit(webcrawler, root_links[0])

#     for link in root_links:
#       executor.submit(webcrawler, link)


if __name__ == '__main__':
  # start_time = time.time()
  main()
  # duration = time.time() - start_time
  # print(f"This took {duration} seconds.")