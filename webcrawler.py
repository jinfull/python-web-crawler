import sys, threading
from concurrent.futures import ThreadPoolExecutor

from fetch_hrefs import fetch_hrefs
from format_link_block import format_link_block

try:
  root = sys.argv[1]
  root_links = fetch_hrefs(root)
except: 
  print("Please enter a URL!")
  sys.exit(1)

def webcrawler(fragment_num, num_workers):
  start_idx = int((fragment_num - 1) / num_workers * len(root_links))
  end_idx = int(fragment_num / num_workers * len(root_links))
  
  
  for link in root_links[start_idx:end_idx]:
    curr_links = fetch_hrefs(link)
    format_link_block(link, curr_links)
  
  print('task executed by {}'.format(threading.current_thread()))

def main():
  format_link_block(root, root_links)

  num_workers = 3

  with ThreadPoolExecutor(max_workers=num_workers) as executor:
    executor.submit(webcrawler(1, num_workers))
    executor.submit(webcrawler(2, num_workers))
    executor.submit(webcrawler(3, num_workers))

if __name__ == '__main__':
  main()