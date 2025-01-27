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
    <a href="https://github.com/Felioxx/SIS-Course/tree/main/App"><strong>Explore the docs »</strong></a>
  </p>
</div>
<p align="center">
-- ⭔ ♞ - ❀ - ♞ ⭔ --
</p>
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="##Questions answered by the application">Example Questions</a></li>
    <li><a href="#built-with">Built With</a></li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project
This project was done during the winter term 2024/25 at ifgi Münster as part of the Spatial Information Search Course of the Master in Geoinformatics.

In this project of a collaborative and interactive Web-Application was implemented. The App includes a Chatbot which is linked to a leaflet map. It is knowledged about the geometries and the federal relations of Northrhine-Westphalia. 

It consists of multiple components, which will be explained in the following:
 
<br />
<div class="container">
      <div class="image">
        <img align=left width="30%"  src="https://github.com/Felioxx/SIS-Course/blob/main/App/public/images/screenshot_apikey.png?raw=true">
      </div>
      <div class="text">
        <p align=justify><a> In order to use the chatbot, one has to enter a purchased </a> <a href="https://openai.com/index/openai-api/">Open AI API Key</a> <a>            The field for entering the  key opens on loading the /chat page.</a>
          <p>
      </div>
    </div>
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<div class="container">
  <div class="image">
    <img align=left width="60%" src="https://github.com/Felioxx/SIS-Course/blob/main/App/public/images/Screenshot_chat.png?raw=true">
  </div>
  <div class="text">
    <p align=justify><a>On the left side of the page is the chat where you can asks questions similar to our listet examples. After asking the question the chatbot takes some time to generate the answer. When the answer is computet, the named entities in question and answer are visualized on the right side on the leaflet map.</a>
      <p>
  </div>
</div> 
<br />
<br />
<br />
<br />
<br />
<br />
<p align="right">(<a href="https://github.com/Bachelor-thesis-windpark-simulator/windpark-simulator/blob/main/README.md#windscope">back to top</a>)</p>
<br />


## Questions answered by the application

#### regarding location
- Where lies (city/district/administrative district)?

#### regarding federal levels
- Which cities lie in the district of (district)?
- Which cities/districts lie in the administrative district of (administrative district)?

#### regarding attributes
- What is the size of (city/districts/administrative district)?

#### regarding relations between entities
##### distances
- What is the distance between (city) and (city)?
- What is the distance between (district) and (district)?
- What is the distance between (administrative district) and (administrative district)?
##### cardinal directions
- Show me every city that lies western of (city)?
- Show me every district that lies western of (district)?
- Show me every administrative district that lies western of (administrative district)?
- In which direction lies (city) from (city)?
- In which direction lies (district) from (district)?
- In which direction lies (administrative district) from (adnministrative district)?
##### neighbors
- Show me all Neighbors of (city/district/administrative district)?
<p align="right">(<a href="https://github.com/Bachelor-thesis-windpark-simulator/windpark-simulator/blob/main/README.md#windscope">back to top</a>)</p>
<br />

### Built With

* [![JavaScript][JavaScript.com]][JavaScript-url]
* [![python][python.com]][python-url]
* [![nodeJS][nodeJS.com]][nodeJS-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![JQuery][JQuery.com]][JQuery-url]
* [![neo4j][neo4j.com]][neo4j-url]
* [![openAi][openAi.com]][openAi-url]
* [![StackOverflow][StackOverflow.com]][StackOverflow-url]

<p align="right">(<a href="https://github.com/Bachelor-thesis-windpark-simulator/windpark-simulator/blob/main/README.md#windscope">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Installation

1. Clone the repo
   ```sh
   https://github.com/Felioxx/SIS-Course
   ```
2. Install NPM packages in the root directory.
   ```sh
   cd App
   npm install
   ```
3. Run the application
   ```sh
   npm start
   ```
<p align="right">(<a href="https://github.com/Bachelor-thesis-windpark-simulator/windpark-simulator/blob/main/README.md#windscope">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage goals
#### Importance of the application
- Works with the “complete” geometries
- Has knowledge about the relations
- Visualization on map
- Easy to use (less complex than Google Maps f.e.)

#### Target users
- Local government workers
- Citizens
- People who struggle with current Map services

#### Benefits for the users
- Easy useage
- Precise visualization
- Correct distances
- Explanation of the federal system


<p align="right">(<a href="https://github.com/Bachelor-thesis-windpark-simulator/windpark-simulator/blob/main/README.md#windscope">back to top</a>)</p>


<!-- LICENSE -->
## License
Copyright (c) 2025 Spacey GmbH

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="https://github.com/Bachelor-thesis-windpark-simulator/windpark-simulator/blob/main/README.md#windscope">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Eva Langstein - elangste@uni-muenster.de

Anne Staskiewicz - anne.staskiewicz@uni-muenster.de

Felix Disselkamp - fdisselk@uni-muenster.de

##### Project Link: [https://github.com/Felioxx/SIS-Course](https://github.com/Felioxx/SIS-Course)

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
[openAi-url]: https://openai.com/
[openAi.com]: https://img.shields.io/badge/-OpenAI%20API-eee?style=for-the-badge&logo=openai&logoColor=412991
[nodeJS-url]: [https://pixijs.com/](https://nodejs.org/en)
[nodeJS.com]: https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white
[neo4j.com]: https://img.shields.io/badge/neo4j-4581C3?style=for-the-badge&logo=neo4j&logoColor=white
[neo4j-url]: https://neo4j.com/
[python.com]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[python-url]: https://www.python.org/
