import requests, bs4

# root_res = requests.get(raw_input('Please provide the root URL: '))
# print root_res.text

# root_res_soup = bs4.BeautifulSoup(root_res.text)

# for link in root_res_soup.find_all('a'):
#   print(link.get('href'))


root = 'https://www.rescale.com/'
root_res = requests.get(root)
root_res_soup = bs4.BeautifulSoup(root_res.text, 'html.parser')

# print root
# print root_res
# print root_res_soup
links_arr = []

for link in root_res_soup.find_all('a'):
  if (not link.get('href')):
    continue

  if (link.get('href')[0:4] == 'http'):
    links_arr.append(str(link.get('href')))
    print link.get('href')

# print links_arr