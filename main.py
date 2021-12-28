from pytrends.request import TrendReq

if __name__ == '__main__':
    # Only need to run this once, the rest of requests will use the same session.
    pytrend = TrendReq(hl='ja-jp', tz=540)

    # Create payload and capture API tokens. Only needed for interest_over_time(), interest_by_region() & related_queries()
    pytrend.build_payload(kw_list=['カレー', 'ラーメン'], timeframe='2021-1-1 2021-12-31', geo="JP")

    # Interest Over Time
    interest_over_time_df = pytrend.interest_over_time()
    print(interest_over_time_df.head(n=100))

    # Interest by Region
    interest_by_region_df = pytrend.interest_by_region(resolution='COUNTRY', inc_low_vol=True, inc_geo_code=True)
    print(interest_by_region_df.head(n=100))

    # Related Queries, returns a dictionary of dataframes
    related_queries_dict = pytrend.related_queries()
    print(related_queries_dict)

    # Get Google Hot Trends data
    trending_searches_df = pytrend.trending_searches()
    print(trending_searches_df.head())

    # Get Google Hot Trends data
    today_searches_df = pytrend.today_searches()
    print(today_searches_df.head())

    # Get Google Top Charts
    top_charts_df = pytrend.top_charts(2021, hl='ja-jp', tz=540, geo='GLOBAL')
    print(top_charts_df.head())

    # Get Google Keyword Suggestions
    suggestions_dict = pytrend.suggestions(keyword='ラーメン')
    print(suggestions_dict)
