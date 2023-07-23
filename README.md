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
