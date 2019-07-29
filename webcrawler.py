import sys, threading, time
import concurrent.futures

from fetch_hrefs import fetch_hrefs
from print_link_block import print_link_block

root = sys.argv[1]
root_links = fetch_hrefs(root)

def webcrawler(link): 
  curr_links = fetch_hrefs(link)
  print_link_block(link, curr_links)
  
  # print('task executed by {}'.format(threading.current_thread()))


def main():
  print_link_block(root, root_links)

  with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    for link in root_links:
      executor.submit(webcrawler, link)


if __name__ == '__main__':
  # start_time = time.time()
  main()
  # duration = time.time() - start_time
  # print(f"This took {duration} seconds.")