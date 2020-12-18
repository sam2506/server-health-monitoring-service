# Server-Health-Monitor-Service

Service to check the health of a server, which return 1 when it is healthy and 0 when it is down, every X minutes for a total of Y minutes. It plots a graph using ggplot, corresponding to the data returned by the server, and saves it in a png file.

## Configuration options

- **FILENAME:**  
Name of the file to save the plot. By default, "plot.png" is used.

- **TIME_INTERVAL_IN_MINS:** 
Time interval in minutes after which the server is monitored. By default, 5 minutes are used.

- **TOTAL_TIME_IN_MINS:** 
Total time in minutes for which server is monitored. By default, 60 minutes are used

## Run the Script

1. Edit the "monitor.conf" file to fit your preferences (optional)
2. Create and activate virtual environment:
    ```virtualenv venv```
    ```source venv/bin/activate```
3. Install dependencies:   ```pip3 install -r requirements.txt``` 
4. Install server dependencies:    ```npm install```
5. Run [server.js](./server/server.js): `node server`
6. Run [monitor.py](monitor.py):  `python3 monitor.py`

## Screenshot

[!ALT text](./screenshot.png?raw=true)