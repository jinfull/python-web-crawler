import sys, threading
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
      executor.submit(webcrawler, queue)


def webcrawler(links): 
  curr_link = queue.pop(0)
  curr_links = fetch_hrefs(curr_link)

  print_link_block(curr_link, curr_links)

  for fetched_link in curr_links:
    if fetched_link in seen:
      break
    else:
      seen.add(fetched_link)
      queue.append(fetched_link)

if __name__ == '__main__':
  main()