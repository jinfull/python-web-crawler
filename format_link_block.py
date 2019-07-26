from fetch_hrefs import fetch_hrefs

def format_link_block(link, link_arr):
  link_arr.insert(0, link)
  print("\n  ".join(link_arr))

# format_link_block('http://rescale.com', fetch_hrefs('http://rescale.com'))