import scrapy, re
from scrapy import Request
from .parameters import shows_type, categories, start_date, end_date, rating_range

"""
links = ['comedy', 'sci-fi', 'horror', 'romance', 'action', 'thriller', 'drama', 'mystery', 'crime', 'animation', 'adventure', 'fantasy', 'comedy,romance', 'action,comedy', 'superhero']
all_cat = [f'https://www.imdb.com/search/title/?genres={j}' for j in links]
for i in range(1, 9952, 50):
        start_urls.append(f'{all_cat[1]}&start={i}&ref_=adv_nxt')
"""

dates = ','.join([start_date, end_date])
last_link = f'https://www.imdb.com/search/title/?title_type={shows_type}&release_date={dates}&user_rating={rating_range}&genres={categories}&count=100'


class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    # 'https://www.imdb.com/search/title/?release_date=2000-01-01,'

    start_urls = [last_link]

    def parse(self, response):

        all_movies = response.css('.lister-item-content')
        for movie in all_movies:
            title = movie.css('.lister-item-header a::text').get()
            genre = movie.css('.genre::text').get()
            description = movie.css('.ratings-bar+ .text-muted::text , .text-muted+ .text-muted::text').get()
            year = movie.css('.text-muted.unbold::text').get()
            duration = movie.css('.runtime::text').get()
            rating = movie.css('.ratings-imdb-rating strong::text').get()
            votes = movie.css('.sort-num_votes-visible span:nth-child(2)::text').get()
            # actors = response.css('.lister-item-content').xpath('//*[@id="main"]/div/div[3]/div/div[1]/div[3]/p[3]').get()p a
            actors = movie.css('p a::text').getall()
            yield {'title': title,
                   'genre': genre,
                   'year': year,
                   'description': description,
                   'duration': duration,
                   'rating': rating,
                   'votes': votes,
                   'director/actors': actors,
                   }
        next_page = response.css('.next-page::attr(href)').getall()[1]
        if next_page is not None:
            next = 'https://www.imdb.com' + next_page
            yield Request(next, callback=self.parse)
