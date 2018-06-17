import re
import pickle
import json
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
usernamesfile = open('usernames.txt', 'r')
usernames = usernamesfile.read().split('\n')
data = {}  # all data

for index, username in enumerate(usernames):

    baseurl = 'https://www.instagram.com'
    link = baseurl + '/' + username
    userdata = []

    print('\r Scraping username {} of {}'.format(index+1,
                                                 len(usernames)), end="")
    driver.get(link)

    soup = BeautifulSoup(driver.page_source, 'lxml')

    # find links to pictures by href tag
    span = soup.find('span', attrs={'id': 'react-root'})
    posts = span.select('a[href$=taken-by={}]'.format(username))

    # filter out videos
    pictures = list(filter(lambda p: p.find('span',
                                            class_='coreSpriteVideoIconLarge') is None, posts))

    thumbnails = list(map(lambda p: p.find_all('img',
                                               class_="FFVAD", limit=1)[0]["src"], pictures))

    # links to the page of the actual photo
    photo_links = list(map(lambda p: baseurl + p['href'], pictures))

    for index, link in enumerate(photo_links):

        # open the picture link
        driver.get(link)
        soup = BeautifulSoup(driver.page_source, 'lxml')

        # extract source link of image
        span = soup.find('span', attrs={'id': 'react-root'})
        image = soup.find_all('img', class_="FFVAD", limit=1)[0]
        imglarge = image["src"]

        # extract number of likes on image
        likespan = span.find_all('span', class_="zV_Nj", limit=1)[0]
        text = likespan.text
        numlikes = int(''.join(re.findall('[0-9]+', text)))

        # save high and low quality version of pictures and likes num
        userdata.append({'img-large': imglarge,
                         'img-small': thumbnails[index],  'likes': numlikes})

    data[username] = userdata

driver.quit()

# save to an external file
with open('../data/scraped.json', 'w') as outfile:
    datastr = json.dumps(data, indent=4, sort_keys=True)
    outfile.write(datastr)

# save with pickle too just in case
with open('../data/pickledump', 'wb') as picklefile:
    pickle.dump(data, picklefile)
