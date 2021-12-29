from pytrends.request import TrendReq

if __name__ == '__main__':
    # トレンド情報を取得する。
    pytrend = TrendReq(hl='ja-jp', tz=540)
    kw_list = ['ブロックチェーン', 'ビットコイン']
    pytrend.build_payload(kw_list=kw_list, timeframe='2021-1-1 2021-12-31', geo="JP")
    interest_over_time_df = pytrend.interest_over_time()
    print("*" * 80)
    print("* 結果表示 *")
    print("*" * 80)
    print(interest_over_time_df.head(n=10))

    # 地域別に結果を取得する。
    pytrend = TrendReq(hl='ja-jp', tz=540)
    kw_list = ['ブロックチェーン', 'ビットコイン']
    pytrend.build_payload(kw_list=kw_list, timeframe='2021-1-1 2021-12-31', geo="JP")
    interest_by_region_df = pytrend.interest_by_region(resolution='COUNTRY', inc_low_vol=True, inc_geo_code=True)
    print("*" * 80)
    print("* 結果表示（地域別） *")
    print("*" * 80)
    print(interest_by_region_df.head(n=10))

    # 関連キーワードの取得
    pytrend = TrendReq(hl='ja-jp', tz=540)
    kw_list = ['ブロックチェーン']
    pytrend.build_payload(kw_list=kw_list, timeframe='2021-1-1 2021-12-31', geo="JP")
    topics = pytrend.related_queries()
    print("*" * 80)
    print("* 結果表示（関連キーワード:rising） *")
    print("*" * 80)
    print(topics[kw_list[0]]['rising'])
    print("*" * 80)
    print("* 結果表示（関連キーワード:top） *")
    print("*" * 80)
    print(topics[kw_list[0]]['top'])

    # 検索サジェストの取得
    pytrend = TrendReq(hl='ja-jp', tz=540)
    suggestions_dict = pytrend.suggestions(keyword='ブロックチェーン')
    print("*" * 80)
    print("* 結果表示（関連キーワード:検索サジェスト） *")
    print("*" * 80)
    print(suggestions_dict)

    # 最近の急上昇
    pytrend = TrendReq(hl='ja-jp', tz=540)
    trending_searches_df = pytrend.trending_searches(pn='japan')
    print("*" * 80)
    print("* 結果表示（最近の急上昇） *")
    print("*" * 80)
    print(trending_searches_df.head(n=10))

    # 本日の急上昇
    pytrend = TrendReq(hl='ja-jp', tz=540)
    today_searches_df = pytrend.today_searches(pn='JP')
    print("*" * 80)
    print("* 結果表示（本日の急上昇） *")
    print("*" * 80)
    print(today_searches_df.head(n=10))

    # 年度別のトップチャート取得
    pytrend = TrendReq(hl='ja-jp', tz=540)
    top_charts_df = pytrend.top_charts('2021', hl='ja-jp', tz=540, geo='JP')
    print("*" * 80)
    print("* 結果表示（年度別のTOPチャート） *")
    print("*" * 80)
    print(top_charts_df.head(n=10))

    # カテゴリ内容の表示
    pytrend = TrendReq(hl='ja-jp', tz=540)
    categories_df = pytrend.categories()
    print("*" * 80)
    print("* 結果表示（カテゴリ内容） *")
    print("*" * 80)
    print(categories_df)
