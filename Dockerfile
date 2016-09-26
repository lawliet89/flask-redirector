FROM python:3.5
MAINTAINER Yong Wen Chua <me@yongwen.xyz>

WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

VOLUME '/usr/src/app/config'
COPY . /usr/src/app/

EXPOSE 5000
ENTRYPOINT ["/usr/src/app/manager.py"]
CMD ["-c", "/usr/src/app/config/config.ini", "gunicorn", "-b", "0.0.0.0:5000"]
