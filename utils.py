def find_limits(data,col):
    print(data[col].quantile([0.25, 0.75]))
    q1,q3 = data[col].quantile([0.25, 0.75])
    iqr = q3-q1
    lower_limit = q1 - (1.5 * iqr)
    upper_limit = q3 + (1.5 * iqr)
    return lower_limit,upper_limit

def treat_outliers(data,col):
    lower_limit,upper_limit = find_limits(data,col)
    data.loc[(data[col]<lower_limit),col] = lower_limit
    data.loc[(data[col]>upper_limit),col] = upper_limit
    return data

