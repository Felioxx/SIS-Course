<div align="center">
  <a href="https://github.com/Felioxx/SIS-Course">
    <img src="https://github.com/Felioxx/SIS-Course/blob/main/App/public/images/flavicon.png?raw=true" alt="Logo" width="20%" height="20%">
  </a>
<h3 align="center">Chat with NRW</h3> 
 Ask NRW about its most important geometries!
  <p align="center">
        <br />
   made <a href="https://www.uni-muenster.de/Geoinformatics/">@ifgi - UNI MUENSTER</a> 🌍
    <br />
    <a href="https://github.com/Laxeros07/Bachelor-thesis-windpark-simulator"><strong>Explore the docs »</strong></a>
  </p>
</div>
<p align="center">
-- ☁️ ✇ - ✇ - ✇ ☁️ --
</p>
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
        <li><a href="https://github.com/Bachelor-thesis-windpark-simulator/windpark-simulator/blob/main/README.md#running-%EF%B8%8F%F0%92%88%B1">Running</a></li>
        <li><a href="#configuaration">Configuration</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="https://github.com/Bachelor-thesis-windpark-simulator/windpark-simulator/blob/main/README.md#server-apis">Server APIs</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project
A collaborative and interactive wind farm simulator. This project was done during the summer semester 2023 at ifgi.

This project is based on the existing [future mobility project from Imaginary ](<[url](https://github.com/IMAGINARY/future-mobility)>) and adapted it towards the aim of this project.
It consists of multiple components, which will be explained in the following.
<br />
<div class="container">
      <div class="image">
        <img align=left width="50%" alt="Bildschirmfoto 2023-08-12 um 19 41 54" src="https://github.com/Bachelor-thesis-windpark-simulator/windpark-simulator/assets/90246149/6c4e63f2-ba9b-41d5-b408-676322ac077f">
      </div>
      <div class="text">
        <p align=justify><a>The website allows users to arrange a 16x16 grid with certain areas. These areas include green spaces as water areas and parks, infrastructure as roads and residentials and windturbines of two different sizes. The initial layout is all parks as you can see in the image.</a>
          <p>
      </div>
    </div>
<br />
<br />
<br />
<br />
<br />
<div class="container">
  <div class="image">
    <img align=left width="30%" src="https://github.com/ifgiscope/wind-turbines/assets/46593824/a94634a1-71ac-4406-a474-74ff8e88c408">
  </div>
  <div class="text">
    <p align=justify><a>With the buttons on the right the user can select an area type and then change tiles by clicking on them. Right to the grid are smileys that display how satisfied certain conditions are, the amount of green spaces, the amount of wind turbines and the distances towards one another.</a>
      <p>
  </div>
</div> 
<div class="container">
  <div class="image">
    <img align=left width="30%" src="https://github.com/ifgiscope/wind-turbines/assets/46593824/6039f364-5388-416a-9d72-7594a5a0a240">
  </div>
  <div class="text">
    <p align=justify><a>Below the smileys are acteurs displayed, that tell, when some conditions are true. They tell the user what is missing in the current layout. On example for this are citizens that say there is not enoug elecrticity. Therefore, there needs to be build more wind turbines.</a>
      <p>
  </div>
</div> 
<br />
<br />
<br />
<br />
Together with all these options, the user has the goal, to build the best possible layout to fulfill all goals and leave averyone involved satisfied.
<p align="right">(<a href="https://github.com/Bachelor-thesis-windpark-simulator/windpark-simulator/blob/main/README.md#windscope">back to top</a>)</p>
<br />

### Questions answered by the application:

#### regarding location
- Where lies <city/district/administrative_district>?

#### regarding federal levels
- Which cities lie in the district of <district>?
- Which cities/districts lie in the administrative district of <administrative_district>?

#### regarding addtibutes
- What is the size of <city/districts/administrative_district>?

#### regarding relations between entities
##### distances
- What is the distance between <city> and <city>?
- What is the distance between <district> and <district>?
- What is the distance between <administrative_district> and <administrative_district>?
##### cardinal directions
- Show me every city that lies western of <city>?
- Show me every district that lies western of <district>?
- Show me every administrative district that lies western of <administrative_district>?
##### neighbors
- Show me all Neighbors of <city/district/administrative_district>?
<br />

### Built With

* [![JavaScript][JavaScript.com]][JavaScript-url]
* [![nodeJS][nodeJS.com]][nodeJS-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![JQuery][JQuery.com]][JQuery-url]
* [![pixi][pixi.com]][pixi-url]
* [![StackOverflow][StackOverflow.com]][StackOverflow-url]

<p align="right">(<a href="https://github.com/Bachelor-thesis-windpark-simulator/windpark-simulator/blob/main/README.md#windscope">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started ✇ミ

### Prerequisites

* npm
  ```sh
  npm install npm@latest -g
  ```
* http-server
  ```sh
  npm install --global http-server
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/Lorano and Laxeros07/windpark-simulator.git
   ```
2. Install NPM packages in **both** the root directory and the
`server` directory.
   ```sh
   npm install
   ```
3. You can use the following commands in the root directory to build the client apps. The
server does not require compilation.
   ```sh
   npm run build
   ```
   or
   ```sh
   npm run watch
   ```

### Running 🏃‍♀️𒈱
1. Start the server by running 
   ```sh
   npm run start
   ```
   in the `server` directory.

2. Start the frontend by running
   ```sh
   http-server -c-1
   ```
   in the root directory.

The clients, in the root directory, are:

- `city.html`: Presents the city map, to be projected over the exhibition table.
- `dashboard.html`: Shows the auxiliary touchscreen dashboard that displays variables and goals,
  and allows selecting Power-Ups.
- `editor.html`: An editor that pushes changes to the server. Note that it doesn't read updates from
  the server, so it's not possible to use multiple editors simulatenously. It's only meant for
  use during development.

- `index.html`: This is a standalone browser version of the software.
<p align="right">(<a href="https://github.com/Bachelor-thesis-windpark-simulator/windpark-simulator/blob/main/README.md#windscope">back to top</a>)</p>

### Configuration

The main configuration file is `config.yml`. The server has to be reloaded after any changes.
Clients get the configuration from the server through the http API and have to be reloaded after
the server to take any changes.

The .env file has other configuration keys that affect the environment.

<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="https://github.com/Bachelor-thesis-windpark-simulator/windpark-simulator/blob/main/README.md#windscope">back to top</a>)</p>

## Server APIs

The server has both an HTTP and a WebSocket API. Their specifications are:

- http: `specs/openapi.yaml`
- ws: `specs/asyncapi.yaml`


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

<p align="right">(<a href="https://github.com/Bachelor-thesis-windpark-simulator/windpark-simulator/blob/main/README.md#windscope">back to top</a>)</p>

<!-- LICENSE -->
## License
Copyright (c) 2021 IMAGINARY gGmbH
Licensed under the MIT license (see LICENSE)
Supported by Futurium gGmbH

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="https://github.com/Bachelor-thesis-windpark-simulator/windpark-simulator/blob/main/README.md#windscope">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Eva Langstein - elangste@uni-muenster.de
Anne Staskiewicz - anne.staskiewicz@uni-muenster.de

Project Link: [https://github.com/Bachelor-thesis-windpark-simulator/windpark-simulator](https://github.com/Bachelor-thesis-windpark-simulator/windpark-simulator)

<p align="right">(<a href="https://github.com/Bachelor-thesis-windpark-simulator/windpark-simulator/blob/main/README.md#windscope">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="https://github.com/Bachelor-thesis-windpark-simulator/windpark-simulator/blob/main/README.md#windscope">back to top</a>)</p>

<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com
[JavaScript.com]: https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E
[JavaScript-url]: https://www.javascript.com/
[StackOverflow-url]: https://stackoverflow.com/
[StackOverflow.com]: https://img.shields.io/badge/-Stackoverflow-FE7A16?style=for-the-badge&logo=stack-overflow&logoColor=white
[pixi-url]: https://pixijs.com/
[pixi.com]: https://img.shields.io/badge/PIXI-FF10F0?style=for-the-badge&logo=pixi&logoColor=white
[nodeJS-url]: [https://pixijs.com/](https://nodejs.org/en)
[nodeJS.com]: https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white

