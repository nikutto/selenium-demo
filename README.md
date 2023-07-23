# Hello selenium

## Preparation

- Docker
- Python
  - `venv` is recommended.a
    - `python3 -m venv venv`
    - `source venv/bin/activate`
- (For WSL env,) imagemagick
  - sudo apt install imagemagick
  - Since there are no viewer.

## Architecture

nginx <--> selenium-chrome <--> selenium (main.py)

## How to run?

1. `docker compose up -d`
2. `python -m pip install -r requirements.txt`
3. `python src/main.py`

## Packet capture

What I learned.
- Selenium webdriver just call Rest API.
- Selenium render html asyncronously.
  - Sometimes, we have to wait for it.
    - For example, wait until some element is rendered.

Package capture report.
1. Establish connection between selenium-chrome and webdriver. (`POST /wd/hub/session`)
  - Send options as JSON
  - Receive session id and configuration properties as JSON
    - For example, browser name (chrome).
2. Send url. (`POST /wd/hub/session/{sessionid}/url`)
  - Send url as JSON (In this case, url: http://fe-server/index.html)
  - Receive 200 and meaningless JSON
3. Take screen shot. (`GET /wd/hub/session/{sessionid}/screenshot`)
  - Receive bytes as JSON
4. And so on