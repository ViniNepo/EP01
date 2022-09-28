import pandas as pd


def Convert_to_final_csv():
    pd.read_json('../scrapy/pokemons.json').to_csv(path_or_buf='pokemons.csv')


if __name__ == '__main__': Convert_to_final_csv()
