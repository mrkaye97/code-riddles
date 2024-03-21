import pandas as pd
import time


def main() -> None:
    data = pd.read_csv(
        "data/measurements.txt",
        delimiter=";",
        header=None,
        names=["station", "temperature"],
    )

    result = data.groupby("station").agg({"temperature": ["mean", "min", "max"]})
    result.columns = list(map("_".join, result.columns.values))

    result = (
        result.reset_index()
        .sort_values(by="station")
        .assign(
            formatted_result=lambda x: x["station"]
            + "="
            + round(x["temperature_min"], 1).astype(str)
            + "/"
            + round(x["temperature_mean"]).astype(str)
            + "/"
            + round(x["temperature_max"]).astype(str)
        )
    )

    print("{" + result.formatted_result.str.cat(sep=", ") + "}")


if __name__ == "__main__":
    start = time.time()
    main()

    print(f"Time: {time.time() - start} seconds")
