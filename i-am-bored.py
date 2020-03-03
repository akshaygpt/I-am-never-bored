import requests
from bs4 import BeautifulSoup
from csv import writer
import random

response = requests.get('https://techcrunch.com/')
soup = BeautifulSoup(response.text, 'html.parser')
posts = soup.select('.post-block')

'''
Find the first occurence of an HTML element (findThis) 
inside another HTML element (fromThat)
using a class name
css selector, html element => html element
'''
def findThisFromThat(findThis, fromThat):
    # print(locals().values())
    return fromThat.find(class_=findThis)

'''
Extract post content from the list of posts
array of html elements => none
'''
def extractPostsContent(posts):
    for index, post in enumerate(posts):
        headingEl = findThisFromThat('post-block__title__link', post)
        heading = headingEl.getText().replace('\n','')
        link = headingEl

        datetimeEl = post.find(class_='river-byline__time')
        datetimeUnformatted = datetimeEl['datetime']
        dateFormatted = datetimeEl.getText()

        content = post.find(class_='post-block__content').getText()

        print(heading, '\n', link)

'''
Print a random post from posts array
'''
if __name__ == '__main__':
    post = random.choice(posts)
    print(findThisFromThat('post-block__title__link', post).getText().replace('\n',''), \
        findThisFromThat('post-block__title__link', post)['href'])
