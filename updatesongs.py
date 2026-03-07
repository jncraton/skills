from urllib.parse import urlencode
from urllib.request import urlopen
from html.parser import HTMLParser
import pandas as pd
import numpy as np
import re
from tqdm import tqdm

tqdm.pandas()

# import csv from Hymnary
base_url = "https://hymnary.org/search"

params = {
    "qu": {
        "textLanguages": "english",
        "hymnalNumber": "CCLI",
        "in": "instances",
    },
    "sort": "displayTitle",
    "export": "csv",
    "limit": 10000
}

params["qu"] = " ".join([f"{k}:{v}" for k, v in params["qu"].items()])
url = f"{base_url}?{urlencode(params)}"

instances = pd.read_csv(url)
instances["ccliPopularity"] = 101 - instances["number"]

ccli_hymns = ( 
    instances.groupby("textAuthNumber")
    .agg(
        {
            "ccliPopularity": "sum",
            "displayTitle": "first",
            "authors": "first",
            "firstLine": "first",
            "refrainFirstLine": "first",
        }
    )
    .sort_values(by=["ccliPopularity"], ascending=False)
    .reset_index()
)

ccli_hymns["ccliPopularity"] = (100 * ccli_hymns["ccliPopularity"] / ccli_hymns["ccliPopularity"].max()).astype(int)

params = {
    "qu": {
        "textLanguages": "english",
        "media": "text",
        "in": "texts",
    },
    "sort": "totalInstances",
    "export": "csv",
    "limit": 250
}

params["qu"] = " ".join([f"{k}:{v}" for k, v in params["qu"].items()])
url = f"{base_url}?{urlencode(params)}"

hymns = pd.read_csv(url)
hymns['hymnalPopularity'] = (100 * hymns['totalInstances'] / hymns['totalInstances'].max()).astype(int)

hymns = pd.concat([hymns, ccli_hymns])

hymns['popularity'] = hymns[['ccliPopularity', 'hymnalPopularity']].max(axis=1).astype(int)

hymns = hymns.groupby('textAuthNumber').agg({
    'popularity': 'max',
    "displayTitle": "first",
    "authors": "first",
    "firstLine": "first",
    "refrainFirstLine": "first",
}).sort_values(by=["popularity"], ascending=False).reset_index()

hymns.drop(columns=['popularity'], inplace=True)

hymns.replace({np.nan: None}, inplace=True)

# export to json
hymns.to_json("skills/hymnary-recommendations/references/songs.jsonl", orient="records", lines=True)

# export to custom line-oriented markdown format
def export_hymns(df, path):
    with open(path, 'w') as f:
        for _, row in df.iterrows():
            refrain = f' and includes the refrain "{row["refrainFirstLine"]}"' if row['firstLine'] else ""
            
            f.write(f"[{row['displayTitle']} by {row['authors']}]"
                    f"(https://hymnary.org/text/{row['textAuthNumber']})"
                    f' (begins with "{row["firstLine"]}"{refrain})\n\n')

export_hymns(hymns, 'skills/hymnary-recommendations/references/songs.md')