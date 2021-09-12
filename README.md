# IMDB-scraper
![images](https://user-images.githubusercontent.com/83681204/132999621-c6fa960b-7ce4-4ca4-a3f6-4b75a277f239.jpeg)

IMDB scraper allows to collect movies and tv shows data from the imdb website
The scraper is built with SCRAPY and can collect the following fields:
<ul>
  <li>Show Title</li>
  <li>Show Category</li>
  <li>Year of release</li>
  <li>Show Description</li>
  <li>Show Duration</li>
  <li>Users Ratings</li>
  <li>Number of Votes</li>
  <li>Actors/Directors</li>
</ul>
To run the code you need to :
install scrapy : pip install scrapy
enter the filtering parameters in the parameters.py file
excute the command in the terminal/cmd : scrapy crawl imdb -o name_of_the_file.csv
name_of_the_file is the file where you save the data


