import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'
file = pd.read_csv(big_mac_file)


def get_big_mac_price_by_year(year,country_code):
    country = country_code.upper()
    query = f"( date >= '{year}-01-01'and date <= '{year}-12-31' and iso_a3 == '{country}')"
    country_df= file.query(query)
    return round(country_df['dollar_price'].mean(),2)


def get_big_mac_price_by_country(country_code):
    country = country_code.upper()
    query = f"(iso_a3 == '{country}')"
    country_df= file.query(query)
    return round(country_df['dollar_price'].mean(),2)


def get_the_cheapest_big_mac_price_by_year(year):
    query_date = f"date >= '{year}-01-01' and date <= '{year}-12-31'"
    price = file.query(query_date)
    idx_min_price = price['dollar_price'].idxmin()
    min_price = file.loc[idx_min_price]
    return f"{min_price['name']}({min_price['iso_a3']}): ${round(min_price['dollar_price'],2)}"


def get_the_most_expensive_big_mac_price_by_year(year):
    query_date = f"date >= '{year}-01-01' and date <= '{year}-12-31'"
    price = file.query(query_date)
    idx_max_price = price['dollar_price'].idxmax()
    max_price = file.loc[idx_max_price]
    return f"{max_price['name']}({max_price['iso_a3']}): ${round(max_price['dollar_price'],2)}"

if __name__ == "__main__":
    answer1 = get_big_mac_price_by_year(2010,"arg")
    print(answer1)
    answer2 = get_big_mac_price_by_country("mex")
    print(answer2)
    answer3 = get_the_cheapest_big_mac_price_by_year("2008")
    print(answer3)
    answer4 = get_the_most_expensive_big_mac_price_by_year("2014")
    print(answer4)