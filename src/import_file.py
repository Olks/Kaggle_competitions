import pandas as pd


df = pd.read_csv('D:\Kaggle\Santander\\train.csv', sep=',', nrows = 8)
may = df[df['fecha_dato']=='2015-01-28']
print may
#print df['age']
#print df.describe()

#print df.ix[1:3,4:7]
#print df.index
#print df.loc[1:4]

#print df[0:5]

#print df

# df.dtypes
# df.select_dtypes([object])
# header_names = df.select_dtypes([object]).columns.values.tolist()
# dummies_train = get_dummies(df_train[header_names],prefix=header_names)
# dummies_test = get_dummies(df_test[header_names],prefix=header_names)
# df_train_num = df_train.drop(header_names,axis=1)
# df_test_num = df_test.drop(header_names,axis=1)
# df_train = concat([df_train_num,dummies_train] , axis=1)
# df_test = concat([df_test_num,dummies_test] , axis=1)