<h1 align=center>scrapy_homework</h1>
<h3 align=center>First step</h3>
<b>Download project:</b>
<p>git clone https://github.com/HabibiDev/scrapy_homework.git</p>
<b>Create and activation virtualenv:</b>
<p>cd scrapy_homework</p>
<p>python3 -m venv env</p>
<p>. env/bin/active</p>
<b>Install requirements:</b>
<p>pip install -r requirements.txt</p>
<h3 align=center>Second Step</h3>
<b>Install postgres and create database</b>
<p>sudo apt-get update</p>
<p>sudo apt install postgresql postgresql-contrib</p>
<p>sudo -u postgres psql</p>
<p>CREATE USER fendi_admin WITH PASSWORD '123';</p>
<p>CREATE DATABASE fendi_db OWNER fendi_admin;</p>
<h3 align=center>Third step</h3>
<b>Create migrate and run webapp</b>
<p>cd fendi_shop</p>
<p>python manage.py migrate</p>
<p>python manage.py runserver</p>
<b>Open another terminal and run celery</b>
<p>celery -A fendi_shop worker -l info</p>
<b>Open another terminal and run spider</b>
<p>scrapy crawl fendi</p>
<h3 align=center>Last step</h3>
<p>Open browser and run http://127.0.0.1:8000/</p>

