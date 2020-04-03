import pandas as pd
import wikipedia as wp

def load_correct_table(wiki_page: str, first_col_name: str) -> pd.DataFrame:
    """Go through the tables in a wiki page and dataframify the one that matches
    the first column name.

    Args:
        wiki_page (str): The title of the page of interest. Make sure you use
            the one sitting in the web address. 
        first_col_name (str): The string we're trying to match with

    Returns:
        matched_df (pd.DataFrame): The dataframe with matching the
            first_col_name criteria.

    """
    
    # Get the data
    html = wp.page(wiki_page).html().encode("UTF-8")

    for i in range(len(html)):
        matched_df = pd.read_html(html)[i]        

        if list(matched_df)[0] == first_col_name:
            return matched_df

    # If not found return None
    return None
