""" Grabs data from a particular source and returns a cleaned version
"""

import pandas as pd
import cleaners
import dataloaders

def australia() -> pd.DataFrame:
    """Prepare a clean dataframe of Australian data.

    Args:
        None

    Returns:
        df_aus (pd.DataFrame): The cleaned australia data
    """
    # Find the correct dataframe
    first_col_name = 'Unnamed: 0'
    df_aus = dataloaders.load_correct_table('2020_coronavirus_pandemic_in_Australia', first_col_name)
    df_aus = df_aus.rename(columns={'Unnamed: 0': 'date'})
    df_aus = df_aus.set_index('date')

    # Clean the data
    df_aus = cleaners.remove_column_names_at_bottom(df_aus)
    df_aus = cleaners.drop_reference_columns(df_aus)
    df_aus = cleaners.clean_references_from_data(df_aus)
    df_aus = cleaners.clean_references_from_column_names(df_aus)

    # Drop newcases and % growth
    df_aus = df_aus.drop(['Newcases', '%growth'], axis=1)

    # Set everything in the dataframe to float64
    df_aus = df_aus.astype('float64')

    return df_aus

def australia_change(df_cleaned: pd.DataFrame) -> pd.DataFrame:
    """Return a dataframe of the daily change in cases.

    Args:
        df_cleaned (pd.DataFrame): A clean dataframe for Australia. Make it by using australia().

    Returns:
        df_change (pd.DataFrame): A dataframe containing the change in number of cases.

    """
    # Make the dataframe to subtract
    # Drop the last row (most recent data) of the df
    df_minus_tail = df_cleaned.drop(df_cleaned.tail(1).index)

    # Drop the first row of the dataframe
    df_minus_head = df_cleaned.drop(df_cleaned.head(1).index)
    index = df_minus_head.index

    # Drop the index from both
    df_minus_head = df_minus_head.reset_index(drop=True)
    df_minus_tail = df_minus_tail.reset_index(drop=True)

    # Subtract the two
    df_change = df_minus_head.subtract(df_minus_tail)

    # Put the index back in
    df_change.index = index

    return df_change
