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
2. Install virtual environment: ```sudo pip3 install virtualenv```
3. Create and activate virtual environment:
    ```virtualenv venv```
    ```source venv/bin/activate```
4. Install dependencies:   ```pip3 install -r requirements.txt``` 
5. Install server dependencies inside server directory:    ```npm install```
6. Run [server.js](./server/server.js): `node server`
7. Run [monitor.py](monitor.py):  `python3 monitor.py`

    If the following error occurs:  
    **module 'pandas' has no attribute 'tslib'**  
    
    Inside ggplot/utils.py:  
    
    Change this 
    ```    
        date_types = (
            pd.tslib.Timestamp,
            pd.DatetimeIndex,
            pd.Period,
            pd.PeriodIndex,
            datetime.datetime,
            datetime.time
        )
    ```
    to this 
    ```
        date_types = (
            pd._tslib.Timestamp,
            pd.DatetimeIndex,
            pd.Period,
            pd.PeriodIndex,
            datetime.datetime,
            datetime.time
        )
    ```

    Inside ggplot/stats/smoothers.py:  
    
    Change: ```from pandas.lib import Timestamp```  
    To: ```from pandas import Timestamp``` 

    Also change:
    ```    
        date_types = (
            pd.tslib.Timestamp,
            pd.DatetimeIndex,
            pd.Period,
            pd.PeriodIndex,
            datetime.datetime,
            datetime.time
        )
    ```
    To:  
    ```
        date_types = (
            pd.Timestamp,
            pd.DatetimeIndex,
            pd.Period,
            pd.PeriodIndex,
            datetime.datetime,
            datetime.time
        )
    ```
    and then rerun the script.


## Screenshot

![](/screenshot.png)