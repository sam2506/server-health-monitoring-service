FROM python

COPY . /home/server-health

RUN pip install -r /home/server-health/requirements.txt

CMD ["python3","/home/server-health/monitor.py"]