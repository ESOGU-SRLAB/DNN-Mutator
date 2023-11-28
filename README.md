# IM-FIT

![repo_size](https://img.shields.io/github/repo-size/inomuh/imfit) ![Apache-2.0 License](https://img.shields.io/github/license/inomuh/imfit?color=blue) ![lang](https://img.shields.io/github/languages/top/inomuh/imfit)

IM-FIT applies mutation testing to Python and Python-based ROS file types.

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

![Image of IM-FIT ROS Page](images/imfit-ros-page.png)

<p align="center">
        <b><i>Fig 4. IM-FIT ROS Page</i></b>
</p>

IM-FIT carries out mutation operations on ROS files based on Python, in accordance with the user's requests and the collected data. Once the mutants are generated, IM-FIT executes them on the execution page. Once the execution process is completed, the user can access the monitoring page to obtain detailed information on the V&V process.

### Credits

<a href="http://valu3s.eu">
  <img align=left img src="https://upload.wikimedia.org/wikipedia/tr/d/d0/TUBITAK-Logo.jpg" 
       alt="tübitak_logo" height="100" >
</a>

---

This work is supported by [TÜBİTAK](https://www.tubitak.gov.tr/) Project under grant number 120N803 which conducted by the İnovasyon Mühendislik.

---

<a href="http://valu3s.eu">
  <img align=right img src="https://valu3s.eu/wp-content/uploads/2020/04/VALU3S_green_transparent-1024x576.png" 
       alt="valu3s_logo" height="100" >
</a>

This work is also done by [Inovasyon Muhendislik](https://www.inovasyonmuhendislik.com/) and [ESOGU-ASRLAB](https://srlab.ogu.edu.tr/) under [VALU3S](https://valu3s.eu) project. This project has received funding from the [ECSEL](https://www.ecsel.eu) Joint Undertaking (JU) under grant agreement No 876852. The JU receives support from the European Union’s Horizon 2020 research and innovation programme and Austria, Czech Republic, Germany, Ireland, Italy, Portugal, Spain, Sweden, Turkey.

### License

See the [LICENSE](LICENSE.md) file for license rights and limitations (Apache-2.0 Licence).
