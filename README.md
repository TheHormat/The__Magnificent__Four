<h1 align="center" id="title">The Magnificent Four in Django</h1>

<p align="center"><img src="https://cdn-images-1.medium.com/max/1600/1*y85gp8YpXOznN7P7vBhZQQ.jpeg" alt="project-image"></p>

<p id="description" align="center">Celery | Redis | WebSocket in Django with Docker</p>

<h2>🫦 Medium Link</h2>
<p>1. <a href="https://hormat.medium.com/celery-redis-websocket-in-django-with-docker-40d534ba9071">Here is a great blog post for this great repo</a></p>

</br>
<h2>🧐 Features</h2>

Here're some of the project's best features:

*   Dynamically perform surgery using celery and redis
*   Use WebSocket to see changes on your site without refreshing your django server
*   Get rid of many terminals using Docker. Type "docker compuse up --build" to start django celery and redis and finally web socket.
*   Learn the processing logic and how it should be executed using celery redis and websocket with a very simple model object deletion task

</br>
<h2>🛠️ Installation Steps:</h2>
</br>

<p>1. Django</p>

```
pip install django
```
</br>

<p>2. Redis (Install Pc)</p>

```
brew install redis
```
</br>

<p>3. Celery</p>

```
pip install celery
```
</br>

<p>4. WebSocket & Channels</p>

```
pip install channels
```
<p>5. Options (take the contents of my requirements.txt file and ctrl + v into your own file):</p>

```
poetry install
```
</br>


</br>
<h2>🛜 To make it work: </h2>
</br>
<p>1. Create virtualenv</p>

```
python3 -m venv venv
```
</br>

<p>2. Let's active venv</p>

```
source venv/bin/active
```
</br>

<p>3. Migrate Student model</p>

```
python3 manage.py migrate
```
</br>

<p>4. Install packets</p>

```
poetry install
```
</br>

<p>5. We join Docker Hub and run it</p>

<p>6. Finally, it's time to create our docker image. With this, our project will be fully operational.</p>

```
docker compose up --build
```
</br>
  
<h2>💻 Built with</h2>

Technologies used in the project:

*   Python
*   Django Rest Framework
*   HTML5
*   CSS3
*   JavaScript
*   Celery
*   Redis
*   WebSocket
*   Nginx
*   Docker
*   Git
</br>

<h2>😬 Problems</h2>

All the tools used are in their latest versions and suitable for one another. But if you have problems during installation I can recommend the following links:
<p>1. <a href="https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/redis.html">How to download Celery and Redis.</a></p>
<p>2. <a href="https://medium.com/@adabur/introduction-to-django-channels-and-websockets-cb38cd015e29">How to download WebSocket & Channels</a></p>
<p>3. <a href="https://www.docker.com/products/docker-desktop/">How to download Docker & Hub</a></p>

</br>
<h2>🛡️ License:</h2>

This project is licensed under the This project is licensed under the MIT License - see the \[LICENSE\](LICENSE) file for details.
