import csv

def get_file_contents(filename):
    """
    Reads the contents of a file and returns it as a string.
    
    Parameters:
        filename (str): The name of the file to read.
    Returns:
        str: The contents of the file as a string, or None if an error occurs.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            contents = file.read()
        return contents
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
    except IOError:
        print(f"Error: An I/O error occurred while reading '{filename}'.")
        return None


import csv

def create_sentiment_dict(file_path: str) -> dict[str, int]:
    """
    Creates a dictionary of words and their sentiment scores from a CSV file.

    Parameters:
    file_path (str): The path to the CSV file. The CSV file should have
                     two columns: 'Word' and 'Sentiment'.

    Returns:
    dict: A dictionary where keys are words (str) and values are
          sentiment scores (int).
    """
    sentiment = {}
    
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            sentiment[row['Word']] = int(row['Sentiment'])
    
    return sentiment

sentiment = create_sentiment_dict("sentiment.csv")