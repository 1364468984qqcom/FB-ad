import tushare as ts

data = ts.get_hist_data('600536')
# print(data.head().T)
print(data.head(10))
# data_all = ts.get_today_all()
# print(data_all)

