<div id="top"></div>

## mo_technologies

[![Stargazers][stars-shield]][stars-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- ABOUT THE PROJECT -->
## About The Project

A Pokemon is a mystical creature that belongs to a fictional world, designed and managed by the Japanese companies
Nintendo, Game Freak and Creatures. The Pokemon world is available on manga, anime adaptions, games, retail stores 
and many more places.
The idea is to enjoi with this criatures about the software with your kids.

Use the `Django and PostgresSQL` to get started.
<p align="right">(<a href="#top">back to top</a>)</p>

### Installation and Use

_Below is an example of how you can run._

1. Do connection with your server or work in local computer.

2. open a terminal and enter under project folder:
   ```
   
   export COMPOSE_FILE=local.yml
   docker-compose build
   
   ```
3. last command you have images and need to run
   ```
   docker-compose up
   ```
4. check with url http://0.0.0.0:8000/ or http://localhost:8000/
   ```
   Hello Pokemon view.
   ```
5. check with url http://localhost:8000/admin/
   ```
   Django administration
   ```
6. check with url http://localhost:8000/evolution/6
   ```
   this is a endpoint type GET; in this example number 6 is a index and get information about 
   evolution chain.
   the response is a list of dictionary with some keys like "id_evolution", "name", "height" etc.
   ```
7. check with url http://localhost:8000/search/pidgey
   ```
   this is a endpoint type GET; in this example you will get the information about the name=pidgey
   response like example:

   {
        "Evolution": "[{'name': 'pidgey'}, {'name': 'pidgeotto'}, {'name': 'pidgeot'}]",
        "Id": 6,
        "Name": "pidgey"
    }
   ```

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap

- [x] Add Changelog
- [x] Add back to top links
- [x] Add "components" document to easily copy & paste sections of the readme
- [x] Add django app
- [x] Data base implementation
    - [x] Connection ok
    - [x] Save data
- [x] Dev container
    - [x] Docker
    - [x] Docker-compose
- [x] Test functional


See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

william yesid cuesta cardona - [@williamcuestac](https://twitter.com/your_username) - william09y@gmail.com

Project Link: [https://github.com/williamcuesta/mo_technologies](https://github.com/williamcuesta/mo_technologies)


<p align="right">(<a href="#top">back to top</a>)</p>

[stars-shield]: https://img.shields.io/github/stars/williamcuesta
[stars-url]: (https://github.com/williamcuesta/mo_technologies)
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-blue.svg
[linkedin-url]: https://www.linkedin.com/in/william-yesid-cuesta-cardona-9bb09668


![GitHub commit activity](https://img.shields.io/github/commit-activity/w/williamcuesta/mo_technologies?style=plastic)
