import os, glob
import pandas as pd
from pathlib import Path
import sqlalchemy as alch
import json

dir_path = os.path.join(os.path.dirname(__file__), "json_files")
res = glob.glob(os.path.join(dir_path, "*.json"))
print(dir_path)
end = "\n" + 10 * "-" + "\n"
engine = alch.create_engine("sqlite:///db.sqlite3")
print(res, end=end)
for i in res:
    try:
        if (
            Path(i).stem != "weekly_box_office"
            and Path(i).stem != "StarwarsBudgetAndProfit"
            and Path(i).stem != "SWCScreentime"
        ):
            print(i, end=end)
            print(Path(i).stem)
            DNRTable = ["created", "edited"]
            [
                "films",
            ]
            y = pd.read_json(i)
            x = y.transpose()
            if Path(i).stem != "character_data":
                x = x.reset_index(drop=True)
            arr = [
                "films",
                "species",
                "residents",
                "people",
                "pilots",
                "characters",
                "planets",
                "starships",
                "vehicles",
            ]
            for ar in arr:
                if ar in x:
                    x[ar] = x[ar].apply(
                        lambda x: ",".join(map(str, x)) if isinstance(x, list) else x
                    )
            if set(DNRTable).issubset(x.columns):
                for el in DNRTable:
                    x = x.drop(el, axis=1)
            x.to_sql(Path(i).stem, con=engine)
            print(x.head(15))
        else:
            print(Path(i).stem)
            print(Path(i))
            with open(Path(i), encoding="utf-8-sig") as file:
                data = json.load(file)
            print(data)
            y = pd.DataFrame(data)
            y.to_sql(Path(i).stem, con=engine)
            print(y.head(15))
    except: next