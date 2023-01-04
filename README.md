<h1 align="left">A WebScraper for a Security's Related News</h1>

  <p align="left">
    This system scraps text from articles related to a specific asset (stocks for v.1.0) and yields a polarity -- also known as sentiment -- score. It intends to automate the reading of financial news. It uses Flask in order to provide API functionality.
  </p>
</div>


<!-- ABOUT THE PROJECT -->
## About The Project

- Presented to Analytics Club Uniandes, Feb. 2020
- Author: Daniel Londoño B. 



### Built With

* 🌶️ Flask
* 🥣 BeautifulSoup
* 🐼 Pandas




<!-- GETTING STARTED -->
## Getting Started

In order to run the project, it is advised to follow the following steps. 

### Prerequisites

This project was developed using Python3.10.4. You can download it from here: https://www.python.org/downloads/

* Once you cloned the repository, on the project's root folder, run in order to activate the local environment:
  ```sh
  source env/bin/activate
  ```

* Followed by
  ```sh
  pip3 install -r requirements.txt
  ```

* To start the server, run:
  ```sh
  python3 backend.py
  ```

<!-- USAGE EXAMPLES -->
## Usage

Once the server is running, with Postman (or any other request system) create a GET request to localhost:5000/stock_scrap . This request must contain a JSON Body as follows.
  ```sh
  {"stock_ticker" : your_desired_stock_ticker}
  ```
  
## Important information: 
> _This system runs as a baseline model for webscraping news about a specific security (only stocks for v.1.0). Since it looks up for all possible websites, erros could be encountered considering DOM, HTML structure, and other system variations along the internet. Please feel free to contact me in order to optimize this program._

<!-- CONTACT -->
## Contact

Daniel Londoño - [@LinkedIn](https://www.linkedin.com/in/daniel-londo%C3%B1o-60189a132/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
