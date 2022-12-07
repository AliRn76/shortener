**Usage:**  

`docker run --publish 8000:8000 --env BASE_URL=https://example.com --env TITLE="URL Shortener" --env DESCRIPTION="Create Your Short URL Here" --name shortener --detach alirn76/url-shortener:v1.1`

*   It starts at **port 8000**, so you can publish it in any port you want.
*   **BASE\_URL:** It is used to show the shortened URL to the user **( default:** [_http://127.0.0.1:8000_](http://127.0.0.1:8000) **)**
*   **TITLE:** For customizing the title **( default:** _URL Shortener_ **)**
*   **DESCRIPTION:** For customizing the description **( default:** _Create Short & Memorable URL In a Seconds._ **)**

**Persistent Storage:**

1.  Create docker volume → `docker volume create shortener-volume`
2.  Add this to the run command → `--volume shortener-volume:/shortener/database`

**Technology Used:**

*   Python
*   Django
*   SQLite
*   Gunicorn

**Source Code** → [https://github.com/AliRn76/shortener](https://github.com/AliRn76/shortener)

**Docker Image** → [https://hub.docker.com/r/alirn76/url-shortener](https://hub.docker.com/r/alirn76/url-shortener)

Tanks to MohammadReza Shahbazi