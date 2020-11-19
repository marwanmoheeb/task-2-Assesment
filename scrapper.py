## this program gets the first 100 stories from the url  'https://news.un.org/en/news/region/middle-east' and outputs them into a json file
## since each page has 10 stories it gets 10 stories from 10 pages
# library to imprt html pagea
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import json

session = HTMLSession()
data = []
count = 0
#iterate through the pages
for x in range(10):
    URL ='https://news.un.org/en/news/region/middle-east?page=' + str(x)
    print(URL)
    # get html code from url
    page = session.get(URL)
    # parse the html content 
    parsed = BeautifulSoup(page.content, 'html.parser')
    # iterate through the stroies of on the page
    for x in range(10):
        x = x+1 
        storyClass = 'views-row views-row-' + str(x)
        if (x % 2) == 0:
            storyClass = storyClass + ' views-row-even'
        else:
            storyClass = storyClass + ' views-row-odd'
        if (x == 1):
            storyClass = storyClass + ' views-row-first'
        if (x==10):
            storyClass = storyClass + ' views-row-last'
        storyClass = storyClass +  ' clearfix'
        story = parsed.find('div', class_=storyClass )
        #print(story)
        title = story.find('h1', class_='story-title')
        link = title.find('a')['href']
        summary = story.find('p')
        data.append({
            'Title': title.text,
            'Link': URL + link ,
            'Summary': summary.text   
        })
        # check count of stories
        count = count +1
print(count)
# output to file in json format
with open('result.json', 'w') as outfile:
       json.dump(data, outfile)