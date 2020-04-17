import re
import numpy as np
import pandas as pd


def remove_column_names_at_bottom(df_to_clean: pd.DataFrame) -> pd.DataFrame:
    """Sometimes a table has the column names are at the bottom of the table, in addition to at the
    top. Remove these. They suck donkey balls.

    This is done by removing rows with NaNs as indices.

    Args:
        df_to_clean (pd.DataFrame): The dataframe to remove col names from the bottom

    Returns:
        df_to_clean (pd.DataFrame): The dataframe to remove col names from the bottom

    """

    df_to_clean = df_to_clean.drop([np.nan])
    return df_to_clean


def drop_reference_columns(df_to_clean: pd.DataFrame) -> pd.DataFrame:
    """Remove a column that contains only references from a table.
    
    Sometimes there's a stupid column in the table for each state containing the references. Lets
    get rid of that. Functionally this works by removing the second of duplicate column titles. 
    
    Args:
        df_to_clean (pd.DataFrame): The dataframe we want to remove the reference columns from. 
        
    Returns:
        df_to_clean (pd.DataFrame): The dataframe with refence columns removed.

    """

    # Drop reference columns
    for state in list(df_to_clean):
        if state[-2:] == '.1':
            df_to_clean = df_to_clean.drop([state], axis=1)

    return df_to_clean

def clean_references_from_data(df_to_clean: pd.DataFrame) -> pd.DataFrame:
    """Remove references that attached to data in a column.

    Sometimes data in a column will have a reference right next to the data values in a column: eg.
    2134 [1]. Remove the [1]. Matches and removes anything in square brackets.

    Args:
        df_to_clean (pd.DataFrame): The dataframe to remove references from.

    Returns:
        df_to_clean (pd.DataFrame): The dataframe with references removed.

    """

    for state in list(df_to_clean):
        try:
            df_to_clean[state] = df_to_clean[state].str.replace(r"\[.*\]","")
        except AttributeError:
            pass

    return df_to_clean

def clean_references_from_column_names(df_to_clean: pd.DataFrame) -> pd.DataFrame:
    """Clean the refs from column titles.

    Sometimes there's annoying ass references in the column titles which looks a bit shit. Let's
    ditch these.

    Args:
        df_to_clean (pd.DataFrame): The dataframe to remove references from.

    Returns:
        df_to_clean (pd.DataFrame): The dataframe with references removed.

    """

    for state in list(df_to_clean):
        try:
            new_state = re.sub("[\(\[].*?[\)\]]", "", state)
            df_to_clean = df_to_clean.rename(columns={state: new_state})
        except AttributeError:
            pass

    return df_to_clean


def clean_references_from_index(df_to_clean: pd.DataFrame) -> pd.DataFrame:
    """Remove references that attached to data in an index.

    Sometimes data in a indexn will have a reference right next to the data values in a column: eg.
    2134 [1]. Remove the [1]. Matches and removes anything in square brackets.

    Args:
        df_to_clean (pd.DataFrame): The dataframe to remove references from.

    Returns:
        df_to_clean (pd.DataFrame): The dataframe with references removed.

    """

    try:
        df_to_clean.index = df_to_clean.index.str.replace(r"\[.*\]","")
    except AttributeError:
        pass

    return df_to_clean


def remove_string_from_data(df_to_clean: pd.DataFrame, string) -> pd.DataFrame:
    """Remove references that attached to data in an index.

    Sometimes data in a indexn will have a reference right next to the data values in a column: eg.
    2134 [1]. Remove the [1]. Matches and removes anything in square brackets.

    Args:
        df_to_clean (pd.DataFrame): The dataframe to remove references from.
        string (str): String to be removed.

    Returns:
        df_to_clean (pd.DataFrame): The dataframe with references removed.

    """
    for state in list(df_to_clean):
        try:
            df_to_clean[state] = df_to_clean[state].str.replace(string, '')               
        except AttributeError:
            pass

    return df_to_clean
