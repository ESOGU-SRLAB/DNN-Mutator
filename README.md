# IM-FIT

![repo_size](https://img.shields.io/github/repo-size/inomuh/imfit) ![Apache-2.0 License](https://img.shields.io/github/license/inomuh/imfit?color=blue) ![lang](https://img.shields.io/github/languages/top/inomuh/imfit)

IM-FIT applies mutation testing to Python.

## Installations

- Install python3 and some requirements:

        sudo apt-get update && sudo apt-get install python3 python3-venv python3-pip

- Install requirements:

        pip install -r requirements.txt

## Usage

Terminal command to open interface

    python3 main.py

PS: Before first run IM-FIT, the command

    chmod +x *

must enter the terminal opened from IM-FIT folder.

![Image of IM-FIT Home Page](images/imfit-home-page.png)

<p align="center">
        <b><i>Fig 1. IM-FIT Home Page</i></b>
</p>

The goal of IM-FIT is to offer the user a comprehensive and effective guide to its usage by providing a user manual upon opening.

![Image of IM-FIT Start Page](images/imfit-start-page.png)

<p align="center">
        <b><i>Fig 2. IM-FIT Start Page</i></b>
</p>

IM-FIT's scans can be tailored to specific workloads and chosen code snippets. Once the scanning process is complete, it generates fault plans that can be used in testing procedures. These fault plans contain information on which file to mutate the code.

![Image of IM-FIT Scan Page](images/imfit-scan-page.png)

<p align="center">
        <b><i>Fig 3. IM-FIT Scan Page</i></b>
</p>

During the test run, mutants are categorized as either killed or survived when compared to the original code. The primary aim of the testing process is to kill all mutants. If any mutants survive, it indicates that the software works correctly despite the fault.

![Image of IM-FIT Dnn Mutation Module Page](images/imfit-dnn-page.png)

<p align="center">
        <b><i>Fig 4. IM-FIT ROS Page</i></b>
</p>

IM-FIT carries out mutation operations on ROS files based on Python, in accordance with the user's requests and the collected data. Once the mutants are generated, IM-FIT executes them on the execution page. Once the execution process is completed, the user can access the monitoring page to obtain detailed information on the V&V process.

### Credits

<a href="https://1004.tubitak.gov.tr/tr/node/95">
  <img align=left img src="https://upload.wikimedia.org/wikipedia/tr/d/d0/TUBITAK-Logo.jpg" 
       alt="tübitak_logo" height="100" >
</a>

---

This study has been supported by the Scientific and Technological Research Council of Turkey (TÜBİTAK) under the project number 22AG040, titled "Advanced Technologies Platform for Sustainable Cities (SÜİT)".

---


### License

See the [LICENSE](LICENSE.md) file for license rights and limitations (Apache-2.0 Licence).
