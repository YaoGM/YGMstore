import pandas as pd
users = pd.read_csv('data2/user_loss.csv', encoding='gbk')
info = pd.read_csv('data2/info_new.csv',encoding='utf-8')
print('历史客户信息表的维数：', users.shape)
print('历史订单表的维数：', info.shape)

info['use_start_time'] = pd.to_datetime(info['use_start_time'])

for i in range(len(users)):
    info1 = info.iloc[info[info['name'] == users.iloc[i, 2]].index.tolist(), :]
    if sum(info['name']==users.iloc[i, 2]) != 0:
        users.iloc[i, 14] = max(info1['use_start_time'])

info = info.loc[info['order_status'] == 1, ['emp_id', 'number_consumers', 'expenditure']]
info = info.rename(columns={'emp_id': 'USER_ID'})
print(info.head())
print(users.head())

user = users.iloc[:, [0, 2, 14, 37]]
print(user.head())
info_user = pd.merge(user, info, left_on='USER_ID', right_on='USER_ID', how='left')
info_user.to_csv('./info_user.csv', index=False, encoding='utf-8')
print(info_user.head())

info_user =pd.read_csv('./info_user.csv', encoding='utf-8')
info_user1 = info_user['USER_ID'].value_counts()
info_user1 = info_user1.reset_index()
info_user1.columns = ['USER_ID', 'frequence']

info_user2 = info_user[['number_consumers', "expenditure"]].groupby(info_user['USER_ID']).sum()
info_user2 = info_user2.reset_index()
info_user2.columns = ['USER_ID', 'numbers', 'amount']

info_user_new = pd.merge(info_user1, info_user2, left_on='USER_ID', right_on='USER_ID', how='left')
info_user = info_user.groupby(['USER_ID']).last()
info_user = info_user.reset_index()
print(info_user.head())
print(info_user_new.head())
info_user_new = pd.merge(info_user_new, info_user, left_on='USER_ID', right_on='USER_ID', how='left')
print(info_user_new.head())
print(info_user_new.shape)

print('合并后表中的空值数目：', info_user_new.isnull().sum())
info_user_new = info_user_new.dropna(axis=0)
print(info_user_new.shape)

info_user_new = info_user_new[info_user_new['numbers'] != 0]
print(info_user_new.shape)

info_user_new['average'] = info_user_new['amount']/info_user_new['numbers']
info_user_new['average'] = info_user_new['average'].apply(lambda x: '%.2f' % x)
print(info_user_new.head())
info_user_new['LAST_VISITS'] = pd.to_datetime(info_user_new['LAST_VISITS'], format='mixed')
datefinally = pd.to_datetime('2016-7-31')
time = datefinally - info_user_new['LAST_VISITS']
info_user_new['recently'] = time.apply(lambda x: x.days)

info_user_new.to_csv('./info_user_clear.csv', index=False, encoding='gbk')
print(info_user_new.head())









