''' Build a dataframe in pandas'''

import os
import pandas as pd

def symbol_to_path(symbol, base_dir="data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol))

def get_data(symbols, dates):
    """Read stock date (adjusted close) for given symbols from CSV files."""
    df = df.DataFrame(index=dates)
    if 'SPY' not in symbols: # add SPY for reference, if absent
        symbols.insert(0, 'SPY')
    for symbol in symbols:

    return df

def test_run():
    # Define date range
    start_date='2010-01-22'
    end_date='2010-01-26'
    dates=pd.date_range(start_date,end_date)

    df1=pd.DataFrame(index=dates)

    # Read SPY data into temporary dataframe
    dfSPY=pd.read_csv("data/SPY.csv", index_col="Date", parse_dates=True,
            usecols=['Date','Adj Close'], na_values=['nan'])

    # Rename 'Adj Close' column to 'SPY' to prevent clash
    dfSPY = dfSPY.rename(columns={'Adj Close':'SPY'})

    # Join the two dataframes using DataFrame.join()
    df1 = df1.join(dfSPY,how='inner')

    # Read in more stocks
    symbols = ['GOOG', 'IBM', 'GLD']
    for symbol in symbols:
        df_temp=pd.read_csv("data/{}.csv".format(symbol), index_col='Date',
                parse_dates=True, usecols=['Date','Adj Close'], na_values=['nan'])
        # rename to prevent clash
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df1 = df1.join(df_temp) # use default how='left'

    # Drop NaN values
    df = df1.dropna()
    print df1

if __main__ == "__main__":
    test_run()
