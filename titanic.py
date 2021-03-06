# 获取原始数据
import d_SVM
import warnings
import drawing_v3
import algorithm2_v3

warnings.filterwarnings("ignore")
# 获取原始数据
data_raw = d_SVM.dataDigitize("data/titanic.csv")

# data, labels, names = funcs.data_clean(data_raw)
adjustment_f = ['parch', 'fare', 'embarked', 'class', 'who', 'embark_town', 'alone']

data1 = data_raw[adjustment_f]
data2 = data_raw.drop(adjustment_f, axis=1)

best_f = ['pclass', 'sex', 'age', 'sibsp', 'alive', 'adult_male']
label = 'survived'

# drawing_v3.run_pic(1, 'titanic', data_raw, adjustment_f, best_f, label, 2)

algorithm2_v3.initial_everything1(data_raw, adjustment_f, label, 2)
algorithm2_v3.mae1(data_raw,1,best_f)
algorithm2_v3.initial_everything2(data_raw, adjustment_f, label, 2)
algorithm2_v3.mae2(data_raw,1,best_f)
