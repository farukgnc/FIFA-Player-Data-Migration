import pandas as pd
import numpy as np

first_file_path = '2022.txt'
second_file_path = '2024.txt'

output_path = 'out.txt'

chunksize = 2000  # Define your chunk size here

# Define the columns to update
columns_to_update = ['acceleration', 'aggression', 'agility', 'curve', 'attackingworkrate', 'balance', 'ballcontrol', 'composure', 'crossing', 'defensiveworkrate', 'defspe', 'dribbling', 'driref', 'emotion', 'finishing', 'freekickaccuracy', 'gkdiving', 'gkhandling', 'gkkicking', 'gkpositioning', 'gkreflexes', 'headingaccuracy', 'interceptions', 'jumping', 'longpassing', 'longshots', 'overallrating', 'pacdiv', 'paskic', 'penalties', 'personality', 'phypos', 'positioning', 'potential', 'reactions', 'shohan', 'shortpassing', 'shotpower', 'slidingtackle', 'sprintspeed', 'stamina', 'standingtackle', 'strength', 'vision', 'volleys', 'weakfootabilitytypecode']

def run():
    chunk_counter = 1  # Counter for chunks

    # Read the first text file
    df1_chunks = pd.read_csv(first_file_path, encoding='utf-16-le', delimiter='\t', chunksize=chunksize)

    # Initialize an empty DataFrame as the result
    result = pd.DataFrame()

    # Iterate over chunks from the first text file
    for df1 in df1_chunks:
        print(f"Processing chunk {chunk_counter}...")  # Print the current chunk number
        
        # Read the corresponding chunk from the second text file
        df2_chunks = pd.read_csv(second_file_path, encoding='utf-16-le', delimiter='\t', chunksize=chunksize)

        # Initialize an empty DataFrame to accumulate changes
        chunk_results = pd.DataFrame()

        for chunk_df2 in df2_chunks:
            common_columns = set(df1.columns) & set(chunk_df2.columns)
            dtype_dict = {col: dtype for col, dtype in df1.dtypes.items() if col in common_columns}

            for column in chunk_df2.columns:
                chunk_df2[column] = chunk_df2[column].replace([np.inf, -np.inf, np.nan], 0)

            # Then convert the data types
            chunk_df2 = chunk_df2.astype('Int32')

            # Drop extra columns from chunk_df2
            extra_columns = set(chunk_df2.columns) - common_columns
            chunk_df2.drop(columns=list(extra_columns), inplace=True)

            # Append the updated chunk_df2 to chunk_results
            chunk_results = pd.concat([chunk_results, chunk_df2])

        # Drop duplicate 'playerid' rows in df1 and chunk_results
        df1.drop_duplicates(subset=['playerid'], inplace=True)
        chunk_results.drop_duplicates(subset=['playerid'], inplace=True)

        # Set 'playerid' as index for both dataframes
        df1.set_index(['playerid'], inplace=True)
        chunk_results.set_index(['playerid'], inplace=True)

        # Get the common indices between df1 and chunk_results
        common_indices = df1.index.intersection(chunk_results.index)

        # Update df1 with chunk_results
        for column in columns_to_update:
            df1.loc[common_indices, column] = chunk_results.loc[common_indices, column]

        # Reset index
        df1.reset_index(inplace=True)

        # Append the updated df1 to the result
        result = pd.concat([result, df1])

        chunk_counter += 1  # Increment the counter after processing each chunk

    # Get a list of column names
    cols = list(result.columns)

    # Remove 'playerid' from the list
    cols.remove('playerid')

    # Find the index of the 'stamina' column
    stamina_index = cols.index('stamina')

    # Insert 'playerid' into the right position
    cols.insert(stamina_index + 1, 'playerid')

    # Reindex the DataFrame
    result = result[cols]

    # Save the result to a text file
    result.to_csv(output_path + '/out.txt', index=False, sep='\t', encoding='utf-16-le')
