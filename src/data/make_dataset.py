import os
import yaml
import pandas as pd

from src.utils import read_data_csv, read_data_xl


def load_config(config_path: str) -> dict:
    with open(config_path, "r") as f:
        return yaml.safe_load(f)


def load_source(path: str, filename: str, file_type: str) -> pd.DataFrame:
    """
    Load data based on file type.
    """
    if file_type == "csv":
        df1 = pd.DataFrame(read_data_csv(path, filename))
        return df1

    if file_type == "excel":
        df2 = pd.DataFrame(read_data_xl(path, filename))
        return df2

    raise ValueError(f"Unsupported file type: {file_type}")


def ingest_raw_data(config_path: str = "src/config/config.yaml") -> None:
    """
    Ingest all raw data sources (CSV, Excel) defined in config.yaml
    and store them as CSV files in data/raw/.
    """
    config = load_config(config_path)

    sources = config["data"]["sources"]
    raw_path = config["data"]["raw_path"]

    os.makedirs(raw_path, exist_ok=True)

    for source in sources:
        name = source["name"]
        path = source["path"]
        filename = source["filename"]
        file_type = source["file_type"]

        df = load_source(path, filename, file_type)

        output_file = os.path.join(raw_path, f"{name}.csv")
        df.to_csv(output_file, index=False)

        print(f"[INGESTED] {filename} → {output_file}")


if __name__ == "__main__":
    ingest_raw_data()
