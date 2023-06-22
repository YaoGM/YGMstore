import pandas as pd
import matplotlib.pyplot as plt

info_august = pd.read_csv('data1/meal_order_info.csv',encoding='utf-8')
user_august = pd.read_csv('data1/users.csv',encoding='gbk')
info_august_new = info_august[info_august['order_status'].isin([1])]
info_august_new = info_august_new.reset_index(drop=True)
print('提交的订单数据维数：', info_august_new.shape)
info_august_new.to_csv('info_august_new.csv', index=False, encoding='utf-8')

for i in range(1, len(info_august_new)):
    num = user_august[user_august['USER_ID'] ==
                      info_august_new.iloc[i-1, 1]].index.tolist()
    user_august.iloc[num[0], 14] = info_august_new.iloc[i-1,9]
user = user_august
user['LAST_VISITS'] = user['LAST_VISITS'].fillna(999)
user = user.drop(user[user['LAST_VISITS'] == 999].index.tolist())
user = user.iloc[:, [0, 2, 12, 14]]
print(user.head())
user.to_csv('users_august.csv', index=False, encoding='utf-8')






























