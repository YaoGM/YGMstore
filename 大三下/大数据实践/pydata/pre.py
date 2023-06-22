import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier as DTC
from sklearn.metrics import confusion_matrix

info_user = pd.read_csv('./info_user_clear.csv', encoding='gbk')

info_user = info_user[info_user['type'] != "已流失"]
model_data = info_user.iloc[:, [2, 3, 4, 5, 6]]
print(model_data)
model_data = model_data.drop(labels='ACCOUNT',axis=1).drop(labels='LAST_VISITS',axis=1)
x_tr, x_te, y_tr, y_te = train_test_split(model_data.iloc[:, :-1], model_data['type'], test_size=0.2, random_state=12345)

dtc = DTC()
dtc.fit(x_tr, y_tr)
pre = dtc.predict(x_te)
print('预测结果: \n', pre)

hx = confusion_matrix(y_te, pre, labels=['非流失', '准流失'])
print('混淆矩阵：\n', hx)

P = hx[1, 1] / (hx[0, 1] + hx[1, 1])
print('精确率: \n', round(P, 3))
R = hx[1, 1] / (hx[1, 0] + hx[1, 1])
print('召回率:\n', round(R, 3))

F1 = 2 * P * R / (P + R)
print('F1值: ', round(F1, 3))










