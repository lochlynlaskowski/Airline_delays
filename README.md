### Project Planning
- Audience: potential consumers planning airline travel.
- Utilize classification modeling to determine how long a flight will be delayed by categories.
- Find key features that drive flight delays.

### Project Goal:
- Use classification modeling to predict the likliehood of a flight falling within a specific delayed status category.
- With this knowledge, consumers can identify the best flights for their travel, and allow for any predicted delays.

### Initial Hypotheses:
- Ariline carriers will impact the amount of time delayed.
- Departure and arrival airports will impact the amount of time delayed.
- Day of the week will impact the amount of time delayed.
- The time of the year(month) will impact the amount of time delayed.
- The time of the scheduled flight will impact the amount of time delayed.

### Conclusions:
- Via the exploration process, it was found that airline, the day of the week, the month, day of the month, and the scheduled departure time have a relationship with delayed status.
- During random forest modeling, feature importance was utilized to update the features modeled on.
    - Key features found: Month, DayOfWeek, DayofMonth, CRSElapsedTime, AirTime, departure_hour
- Overall accuracy did not outperform baseline, but increased precision occurred within categories.
- For 2008 flight data, a consumer can expect to be delayed 65% of the time up to 59 minutes past their scheduled arrival time. 
    - This information can allow for additional planning in terms of being on time for important life events, making connecting flights, or ensuring flights home are scheduled with an alloted hour of additional time to return to work on time.
    
- Things to do differently:
    - I significantly reduced the dataset to limit flights that were flown by specific airlines and only departed or arrived at 5 different airports. In retrospect, I would maintain the majority of the data and look into clustering by specific departure times or airports and then attempt to model on the discovered clusters.
    
- With additional time:
    - Explore hyperparameters for modeling to potentially increase model performance.



### Acquire:
- Data was acquired from [kaggle](https://www.kaggle.com/datasets/giovamata/airlinedelaycauses?select=DelayedFlights.csv), with the original datset coming from the U.S. Department of Transportation - Bureau of Transportation Satistics.

### Prepare:
- Original data comprised of 1,936,758 rows and 30 columns.
- Data preparation included:
    - Dropping nulls.
    - Dropping duplicate columns(example:CRSArrTime vs ArrTime).
    - Converts floats to integers.
    - Created Delayed, Delayed_Status, and departure_hour.
    - One-hot encoded UniqueCarrier.
    - Converted CRSDepTime to 24 hour datetime.time.
    - Limited airlines to: WN|AA|MQ|UA|OO|DL
    - Limited airports to: ATL|DFW|DEN|LAX
    
- Dataframe now consists of 12,846 rows and 27 columns.

### Data dictionary:
- **Delayed_Status:**(Target Variable) categorical groups depedning on length of delay. 
    - 0: No delay
    - 1: Delay from 16-59 minutes
    - 2: Delay from 60-119 minuutes
    - 3: Delay from 120- 179 minutes
    - 4: Delay greater than 180 minutes
- **Year:** 2008
- **Month:** 1-12
- **DayofMonth:** 1-31
- **DayOfWeek:** 1 (Monday) - 7 (Sunday)
- **CRSDepTime:** scheduled departure time (local, hhmm)
- **CRSArrTime:** scheduled arrival time (local, hhmm)
- **UniqueCarrier:** unique carrier code
- **TailNum:** plane tail number: aircraft registration, unique aircraft identifier
- **CRSElapsedTime:** in minutes
- **AirTime:** in minutes
- **ArrDelay:** arrival delay, in minutes: A flight is counted as "on time" if it arrived less than 15 minutes before the carriers' scheduled Computerized Reservations Systems (CRS) time.
- **Origin:** origin IATA airport code
- **Dest:** destination IATA airport code
- **Distance** in miles
- **CarrierDelay in minutes:** The cause of the cancellation or delay was due to circumstances within the airline's control (e.g. maintenance or crew problems, aircraft cleaning, baggage loading, fueling, etc.).
- **WeatherDelay in minutes:** Significant meteorological conditions (actual or forecasted) that, in the judgment of the carrier, delays or prevents the operation of a flight such as tornado, blizzard or hurricane.
- **NASDelay in minutes:** Delays and cancellations attributable to the national aviation system that refer to a broad set of conditions, such as non-extreme weather conditions, airport operations, heavy traffic volume, and air traffic control.
- **LateAircraftDelay in minutes:** A previous flight with same aircraft arrived late, causing the present flight to depart late.
- **SecurityDelay in minutes:** Delays or cancellations caused by evacuation of a terminal or concourse, re-boarding of aircraft because of security breach, inoperative screening equipment and/or long lines in excess of 29 minutes at screening areas.
- **Delayed:** If a flight has been delayed or not.
- **departure_hour:** The 24 hour that the flight was scheduled to depart.


### Explore:
- Explore the interactions of features and target variable to determine drivers of flight delays by category.
- Utilize univarate and bivariate exploration, incorporporate hypothesis testing to confirm or deny initial hypotheses.

### Model:
- Utilize classification models to predict flight delays by category.
- Show the three best models.
- Test the best performing model (determined by results of train and validate datasets).
- Best performing model was Gradient Boosting and was in-line with, but did not outperform the baseline model.


### Steps to Reproduce:
- You will need an env.py file with credentials to the Codeup database. 
- Clone this repo (including wrangle.py) 
- Import python libraries: pandas, matplotlib, seaborn, numpy, and sklearn 
- Run final_report (Airline delays- FINAL)