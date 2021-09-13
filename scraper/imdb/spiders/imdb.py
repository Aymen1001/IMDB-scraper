import scrapy, re
from scrapy import Request
from .parameters import shows_type, categories, start_date, end_date, rating_range


dates = ','.join([start_date, end_date])
link = f'https://www.imdb.com/search/title/?title_type={shows_type}&release_date={dates}&user_rating={rating_range}&genres={categories}&count=100'


class ImdbSpider(scrapy.Spider):
    name = 'imdb'

    start_urls = [link]

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
