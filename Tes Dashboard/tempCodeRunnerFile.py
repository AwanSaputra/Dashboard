df_with_good_dates[df_with_good_dates.tier1 == 'planning'].groupby(
    [df_with_good_dates.TGL.dt.year, df_with_good_dates.TGL.dt.month]).count().values.tolist()