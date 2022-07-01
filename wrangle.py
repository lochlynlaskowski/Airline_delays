import pandas as pd
import numpy as np
import sklearn.preprocessing

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
    dummy_df = pd.get_dummies(df[['UniqueCarrier']], dummy_na=False, drop_first=[False])
    df = pd.concat([df, dummy_df], axis=1)  
    return df


def scale_data(train,
              validate,
              test,
              columns_to_scale=['DayOfWeek', 'Month', 'UniqueCarrier_DL', 'UniqueCarrier_OO', 
                 'UniqueCarrier_UA', 'UniqueCarrier_WN']):
    '''
    Scales the split data.
    Takes in train, validate and test data and returns the scaled data.
    '''
    train_scaled = train.copy()
    validate_scaled = validate.copy()
    test_scaled = test.copy()
    
    #using MinMaxScaler (best showing distribution once scaled)
    scaler = sklearn.preprocessing.MinMaxScaler()
    scaler.fit(train[columns_to_scale])
    
    #creating a df that puts MinMaxScaler to work on the wanted columns and returns the split datasets and counterparts
    train_scaled[columns_to_scale] = pd.DataFrame(scaler.transform(train[columns_to_scale]),
                                                 columns=train[columns_to_scale].columns.values).set_index([train.index.values])
    
    validate_scaled[columns_to_scale] = pd.DataFrame(scaler.transform(validate[columns_to_scale]),
                                                 columns=validate[columns_to_scale].columns.values).set_index([validate.index.values])
    
    test_scaled[columns_to_scale] = pd.DataFrame(scaler.transform(test[columns_to_scale]),
                                                 columns=test[columns_to_scale].columns.values).set_index([test.index.values])
    
    
    return train_scaled, validate_scaled, test_scaled