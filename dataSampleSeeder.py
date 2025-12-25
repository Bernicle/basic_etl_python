import json
import random
from datetime import datetime, timedelta

def generateSampleData(dateTimeStart : datetime | str, dateTimeEnd : datetime | str, intervalSecond : int =5, randomSecondDelay : float=1, outputFolder : str="./sensor_log") -> None:
    """For each Generate basic weather data (Json format) and save it to external folder. 
    Args:
        dateTimeStart (datetime | str) : Generated Data start
        dateTimeEnd (datetime | str): Generated Data End
        intervalSecond (int) : interval second for each data file
        randomSecondDelay (float) : second +/- for each interval second  sampling to create a close to real world scenario.
        outputFolder (str) : path folder where data is save.

    Returns:
        List : List of content based on files.
    """
    _dateTimeStart = dateTimeStart
    _dateTimeEnd = dateTimeEnd
    
    if (type(dateTimeStart) == str):
        _dateTimeStart = datetime.strptime(dateTimeStart, "%y/%d/%m %H:%M:%S")
    if (type(dateTimeEnd) == str):
        _dateTimeEnd = datetime.strptime(dateTimeEnd, "%y/%d/%m %H:%M:%S")

    _current_datetime = _dateTimeStart

    while (_dateTimeEnd > _current_datetime):
        _current_datetime = _current_datetime + timedelta(seconds=intervalSecond)
        if (randomSecondDelay > 0):
            _current_datetime = timedelta(seconds=random.randint(randomSecondDelay * -1, randomSecondDelay))
        
        data = {
            "temp":30,
            "humid":50,
            "dateCreated":_current_datetime
        }
        
        print("Processing : " + _current_datetime.timestamp())
        with open(outputFolder + "/" + _current_datetime.timestamp() + ".json") as f:
            json.dump(data,f)
    
    print("Done")
        
if __name__ == "__main__":
    current_datetime = datetime.now()
    end_datetime = current_datetime + timedelta(days=1)
    generateSampleData(current_datetime, end_datetime, 60, 1,"./data")
    