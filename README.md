[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/eleow/desktop_reminder">
    <img src="_misc/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Desktop reminder for Daily Temperature Monitoring</h3>

  <p align="center">
    A Desktop reminder for Twice Daily temperature monitoring. Enter temperature in the pop-up and it will help you enter it in your company's temperature monitoring website. Alternatively if you have a temperature monitoring wearable, it can be fully automated
    <br />
    <br />
    <br />
    ·
    <a href="https://github.com/eleow/desktop_reminder/issues">Report Bug</a>
    ·
    <a href="https://github.com/eleow/desktop_reminder/issues">Request Feature</a>
  </p>
</p>

## About
With COVID-19, companies world-wide require employees to perform daily temperature monitoring. Often-times, with our busy schedules, we forget about it, and are only notified after the fact. Ideally, there should be an integrated reminder-cum-temperature reporting tool for this (like a chatbot?) but that is out of most of our control.

So this is the next best thing - It will pop-up a reminder at your scheduled time and allow you to enter your current temperature. Then it will automatically enter it in your company's website for you.

Also, there are many wearable temperature sensors in the market today. All you would need is an API to retrieve your temperature, and you could have totally automated body temperature monitoring and recording.

:warning: Use at your own risk. Using this app might violate your company's policies, if they frown upon any form of automation in Temperature Taking.


## Getting Started

### Installation

* clone this repo:

```sh
git clone https://github.com/eleow/desktop_reminder.git
```

* install prerequisites in "\requirements.txt"
* go to https://chromedriver.chromium.org/downloads and download a chromedriver that corresponds to your chrome version, and place it in the same directory

## Usage

There are two main ways to use this

### Man-in-the-loop Reminder and Temperature Recording

* Configure *config.ini* based on config.ini.sample
* Customise the function *input_temperature* in selenium_temperature.py according to your company's website
* Run **reminder_popup.py**. At the scheduled time configued in config.ini, you can record your temperature from the pop-up that appears. It will automatically launch your company's temperature-recording website and submit your temperature

### Fully-automated Temperature Recording

* Customise the function *retrieve_iot_temperature* in selenium_temperature.py, according to your IOT-enabled wearable API

:warning: While you could set a random temperature here, it will totally defeat the purpose of temperature monitoring, and would almost certainly violate your company's policies.

* Set scheduled task in Windows Task Scheduler to run **selenium_temperature.py** at your desired times


## License

Distributed under the [MIT License](LICENSE)

## Acknowledgements

Reminder idea and code originally from [nikhilkumarsingh](https://github.com/nikhilkumarsingh/desktop_reminder)

<div>Temperature icon made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/eleow/roboadvisorSystem
[contributors-url]: https://github.com/eleow/desktop_reminder/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/eleow/roboadvisorSystem
[forks-url]: https://github.com/eleow/desktop_reminder/network/members
[stars-shield]: https://img.shields.io/github/stars/eleow/roboadvisorSystem
[stars-url]: https://github.com/eleow/desktop_reminder/stargazers
[issues-shield]: https://img.shields.io/github/issues/eleow/roboadvisorSystem
[issues-url]: https://github.com/eleow/desktop_reminder/issues
[license-shield]: https://img.shields.io/github/license/eleow/roboadvisorSystem
[license-url]: https://github.com/eleow/desktop_reminder/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/edmundleow
[product-screenshot]: images/screenshot.png

