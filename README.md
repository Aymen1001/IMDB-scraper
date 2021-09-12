# IMDB-scraper
![imdb](https://user-images.githubusercontent.com/83681204/132999883-c0a9ded3-5f51-4552-a93d-70947c383465.jpg)

IMDB scraper allows to collect movies and tv shows data from the imdb website.
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
<br>
To run the code you need to :
<br>
install scrapy : pip install scrapy
<br>
enter the filtering parameters in the parameters.py file
<br>
excute the command in the terminal/cmd : scrapy crawl imdb -o name_of_the_file.csv
<br>
name_of_the_file is the file where you save the data
<br>


