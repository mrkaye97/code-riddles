import pandas as pd
import time


def main() -> None:
    data = pd.read_csv(
        "data/measurements.txt",
        delimiter=";",
        header=None,
        names=["station", "temperature"],
    )

    aggregate_statistics = data.groupby("station").agg({"temperature": ["mean", "min", "max"]})
    aggregate_statistics.columns = list(map("_".join, aggregate_statistics.columns.values))

    ordered_by_station = aggregate_statistics.reset_index().sort_values(by="station")

    result = ordered_by_station["station"] + \
        "=" + round(ordered_by_station["temperature_min"], 1).astype(str) + \
        "/" + round(ordered_by_station["temperature_mean"]).astype(str) + \
        "/" + round(ordered_by_station["temperature_max"]).astype(str)


    print("{" + result.str.cat(sep=", ") + "}")


if __name__ == "__main__":
    start = time.time()
    main()

    print(f"Time: {time.time() - start} seconds")
