import sys, threading, time
import concurrent.futures

from fetch_hrefs import fetch_hrefs
from format_link_block import format_link_block

try:
  root = sys.argv[1]
  root_links = fetch_hrefs(root)
except: 
  print("Please enter a URL!")
  sys.exit(1)


def webcrawler(link): 
  curr_links = fetch_hrefs(link)
  format_link_block(link, curr_links)
  
  print('task executed by {}'.format(threading.current_thread()))

def main():
  format_link_block(root, root_links)

  with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    # executor.submit(webcrawler())
    # executor.submit(webcrawler())
    # executor.submit(webcrawler())
    # executor.submit(webcrawler())
    # executor.submit(webcrawler())

    for link in root_links:
      executor.submit(webcrawler, link)
    # future_to_url = {executor.submit(webcrawler, url): url for url in root_links}
    # for future in concurrent.futures.as_completed(future_to_url):
    #   url = future_to_url[future]
      # data = future.result()
        # except Exception as exc:
        #     print('%r generated an exception: %s' % (url, exc))
        # else:
        #     print('%r page is %d bytes' % (url, len(data)))


if __name__ == '__main__':
  start_time = time.time()
  main()
  duration = time.time() - start_time
  print(f"in {duration} seconds")



# def webcrawler(fragment_num, num_workers):
#   start_idx = int((fragment_num - 1) / num_workers * len(root_links))
#   end_idx = int(fragment_num / num_workers * len(root_links))
  
  
#   for link in root_links[start_idx:end_idx]:
#     curr_links = fetch_hrefs(link)
#     format_link_block(link, curr_links)
  
#   print('task executed by {}'.format(threading.current_thread()))

# def main():
#   format_link_block(root, root_links)

#   # # synchronous implementation (not calling webcrawler())
#   # for link in root_links:
#   #   curr_links = fetch_hrefs(link)
#   #   format_link_block(link, curr_links)

#   # concurrent implementation
#   num_workers = 5

#   with ThreadPoolExecutor(max_workers=num_workers) as executor:      
#     executor.submit(webcrawler(1, num_workers))
#     executor.submit(webcrawler(2, num_workers))
#     executor.submit(webcrawler(3, num_workers))
#     executor.submit(webcrawler(4, num_workers))
#     executor.submit(webcrawler(5, num_workers))

# if __name__ == '__main__':
#   start_time = time.time()
#   main()
#   duration = time.time() - start_time
#   print(f"in {duration} seconds")
