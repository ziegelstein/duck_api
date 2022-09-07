<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/ziegelstein/duck_api">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Duck Api</h3>

  <p align="center">
    This is a small fun project to make ducks more accessiable to the world! It exposes duck endpoints to the public and also has a small backend for adding more duck content. It is heavily work in progress. [Watch the demo]("https://duck.ziegel.me") to see it in action!
    <br />
    <a href="https://github.com/ziegelstein/duck_api"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://duck.ziegel.me">View Demo</a>
    ·
    <a href="https://github.com/ziegelstein/duck_api/issues">Report Bug</a>
    ·
    <a href="https://github.com/ziegelstein/duck_api/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]][product-screenshot]

Duck Api should provide a simple rest-api that delivers ducks. It is by no means a professional service, it just is a small attempt to duckify the internet a little bit more

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Marshmallow][marshmallow]][marshmallow-url]
* [![flask][flask]][flask-url]
* [![sqlalchemy][sqlalchemy]][sqlalchemy-url]
* [![python][python]][python-url]
* [![tox][tox]][tox-url]
* [![apispec][apispec]][apispec-url]
* [![Docker][docker]][docker-url]
* [![celery][celery]][celery-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To start developing on the project, please follow these instructions:

### Prerequisites

For Development, Python3, Pip, Venv are requiered, Docker is suggested.
The project can run both on bare-metal or docker, docker is the prefered way.

#### Arch

* pip
  ```sh
    pacman -S python-pip 
  ```

* venv
  ```sh
   python3 -m pip install virtualenv
  ```


#### Ubuntu

* pip
  ```sh
    sudo apt install python3-pip python
  ```

* venv
  ```sh
    sudo pip3 install virtualenv
  ```

### Installation-Dev

0. Clone the repo
   ```sh
   git clone https://github.com/Ziegelstein/duck_api.git
   ```
3. Enter venv
   ```sh
   source bin/activate
   ```
4. Install project requierements
   ```sh
   pip3 install -r requirements.txt
   ```

### Run on Docker

0. Clone the repo
   ```sh
   git clone https://github.com/Ziegelstein/duck_api.git
   ```
3. Run docker compose
   ```sh
   docker-compose up -d
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

The useage will be fully documented in a future update.

_For more examples, please refer to the [Documentation](https://duck.ziegel.me/docs)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Finish the outputs
- [ ] Setup a test library
- [ ] Add Dynamic Duck Facts
- [ ] Add ducks to demo server
    - [ ] Find a solution to duck copyright 
- [ ] Setup a helm-chart

See the [open issues](https://github.com/Ziegelstein/duck_api/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Ziegelstein - [@Ziegelstein 🧱#5926](https://discord.com) - dev@ziegel.me

Project Link: [https://github.com/Ziegelstein/duck_api](https://github.com/Ziegelstein/duck_api)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

None yet, but maybe someone wants to contribute?

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Ziegelstein/duck_api.svg?style=for-the-badge
[contributors-url]: https://github.com/Ziegelstein/duck_api/graphs/contributors
[stars-shield]: https://img.shields.io/github/stars/Ziegelstein/duck_api.svg?style=for-the-badge
[stars-url]: https://github.com/Ziegelstein/duck_api/stargazers
[issues-shield]: https://img.shields.io/github/issues/Ziegelstein/duck_api.svg?style=for-the-badge
[issues-url]: https://github.com/Ziegelstein/duck_api/issues
[license-shield]: https://img.shields.io/github/license/Ziegelstein/duck_api.svg?style=for-the-badge
[license-url]: https://github.com/Ziegelstein/duck_api/blob/main/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/fenja-frings-b100b916b/
[product-screenshot]: images/screenshot.png
[marshmallow]: https://img.shields.io/badge/marshmallow-000000?style=for-the-badge&logo=marshmallow&logoColor=white
[marshmallow-url]: https://marshmallow.readthedocs.io/en/stable/
[flask]: https://img.shields.io/badge/flask-20232A?style=for-the-badge&logo=flask&logoColor=61DAFB
[flask-url]: https://flask.palletsprojects.com/en/2.2.x/
[python]: https://img.shields.io/badge/python-35495E?style=for-the-badge&logo=python&logoColor=4FC08D
[python-url]: https://docs.python.org/3/index.html
[sqlalchemy]: https://img.shields.io/badge/sqlalchemy-DD0031?style=for-the-badge&logo=sqlalchemy&logoColor=white
[sqlalchemy-url]: https://www.sqlalchemy.org/
[tox]: https://img.shields.io/badge/tox-4A4A55?style=for-the-badge&logo=tox&logoColor=FF3E00
[tox-url]: https://tox.wiki/en/latest/
[apispec]: https://img.shields.io/badge/Lapispec?style=for-the-badge&logo=apispec&logoColor=white
[apispec-url]: https://apispec.readthedocs.io/en/latest/index.html
[docker]: https://img.shields.io/badge/Docker-563D7C?style=for-the-badge&logo=docker&logoColor=white
[docker-url]: https://www.docker.com/
[celery]: https://img.shields.io/badge/celery-0769AD?style=for-the-badge&logo=celery&logoColor=white
[celery-url]: https://docs.celeryq.dev/en/stable/
