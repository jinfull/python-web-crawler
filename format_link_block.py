from fetch_hrefs import fetch_hrefs

def format_link_block(link, link_arr):
  print("\n  ".join([link] + link_arr))