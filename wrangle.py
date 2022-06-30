import pandas as pd
import numpy as np

def get_flight_data():
    df = pd.read_csv('DelayedFlights.csv')
    return df


def integers(df):
    """This function converts datatypes to integers for the given columns."""
    df['CRSElapsedTime'] = df['CRSElapsedTime'].astype('int64')
    df['ArrDelay'] = df['ArrDelay'].astype('int64')
    df['AirTime'] = df['AirTime'].astype('int64')
    df['DepDelay'] = df['DepDelay'].astype('int64')
    df['CarrierDelay'] = df['CarrierDelay'].astype('int64')
    df['WeatherDelay'] = df['WeatherDelay'].astype('int64')
    df['NASDelay'] = df['NASDelay'].astype('int64')
    df['SecurityDelay'] = df['SecurityDelay'].astype('int64')
    df['LateAircraftDelay'] = df['LateAircraftDelay'].astype('int64')
    df['Delayed_Status'] = df['Delayed_Status'].astype('int64')
    return df


cols_to_remove = ['Unnamed: 0','DepTime','ArrTime', 'FlightNum','ActualElapsedTime', 'TaxiIn', 'TaxiOut',
       'Cancelled', 'CancellationCode', 'Diverted']
def remove_columns(df, cols_to_remove):
    '''This function removes columns(cols_to_remove) from the dataframe due to duplicates or
    erroneous data.'''
    df = df.drop(columns=cols_to_remove)
    return df

def prepare_flight_data(df):
    '''This function prepares the dataframe by dropping nulls, unwanted columns, creates a
    column Delayed_Status depending on the time of the delay, converts floats to ints, limits
    data to specified airlines and departure arrival airports.'''
    df = df.dropna()
    df = remove_columns(df,cols_to_remove)
    for data in df:
        df.loc[df['ArrDelay'] <= 15, 'Delayed_Status'] = 0
        df.loc[df['ArrDelay'] > 15, 'Delayed_Status'] = 1
        df.loc[df['ArrDelay'] >= 60, 'Delayed_Status'] = 2
        df.loc[df['ArrDelay'] >= 120, 'Delayed_Status'] = 3
        df.loc[df['ArrDelay'] >= 180, 'Delayed_Status'] = 4
    df['Delayed'] = np.where(df['Delayed_Status']== 0, 0, 1)    
    df = integers(df)
    df = df[df.UniqueCarrier.str.contains('WN|AA|MQ|UA|OO|DL')]
    df = df[df.Origin.str.contains('ATL|ORL|DFW|DEN|LAX') & df.Dest.str.contains('ATL|ORL|DFW|DEN|LAX')]
    return df