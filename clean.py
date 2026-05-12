import re
import pandas as pd
from load_data import load_data

def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r'http\S+|www\S+', '', text)   # remove URLs
    text = re.sub(r'\d+', '', text)               # remove numbers
    text = re.sub(r'[^a-z\s]', '', text)          # remove punctuation
    text = re.sub(r'\s+', ' ', text).strip()      # remove extra spaces
    return text

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df['clean_message'] = df['message'].apply(clean_text)
    df['label_num'] = df['label'].map({'ham': 0, 'spam': 1})
    print("Cleaning done!")
    print(df[['message', 'clean_message']].head(3))
    return df

if __name__ == "__main__":
    df = load_data()
    df = clean_data(df)
    print(df.head())