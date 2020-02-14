# data_engineering
This is a study project covering data engineering tools such as Flask, web scraping with scrapy, storage with mongoDB indexing and search engine with Elastic Search

# Apple Refurb project
the aim is to show products available in the apple refurb web site and compare them with another refurb website, for example Back market.
To run the project, first launch Docker and enter
```bash
docker-compose up -d
```
then run the python script 'web.py'
the apple should be available at http://127.0.0.1:2745/

<p align= "center">
<img src="img/landingPage.png"  align="middle">
</p>

Each time the app is run, the scraping is made from the python script - more technic details available in the document "documentation_technique"
