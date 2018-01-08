import requests
from lxml import etree
import os


def movie(url):
	headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
    }
	response = requests.get(url,headers=headers)
	HTML = etree.HTML(response.text)
	movie_list = HTML.xpath('//div[@class="mod-bd"]/ul/li[@class="list-item"]/ul/li[@class="stitle"]/a/@href') + HTML.xpath('//div[@class="mod-bd"]/ul/li[@class="list-item hidden"]/ul/li[@class="stitle"]/a/@href')

	for movieurl in movie_list:
		response = requests.get(movieurl,headers=headers) 
		HTML = etree.HTML(response.text)
		movie_name = HTML.xpath('//div[@id="content"]/h1/span/text()')[0]
		movie_director = HTML.xpath('//div[@id="info"]/span[1]/span[@class="attrs"]/text()')
		movie_actor = HTML.xpath('//div[@id="info"]/span[3]/span[2]/a/text()')
		movie_type = HTML.xpath('//span[@property="v:genre"]/text()')
		movie_score = HTML.xpath('//div[@class="rating_self clearfix"]/strong/text()')
		dirname  = os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)),'zzzzz'),movie_name +'.txt')
		with open(dirname,'w',encoding='utf-8') as f:
			f.write('/'.join(movie_director))
			f.write('/'.join(movie_actor))
			f.write('/'.join(movie_type))
			f.write('/'.join(movie_score))

url  = 'https://movie.douban.com/cinema/nowplaying/shenzhen/'
if __name__ = '__main__':
	movie(url)
