import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.model_selection import GridSearchCV
np.random.seed(42)
import pickle

# load data
liver_df = pd.read_csv(r"F:\python ml\projects\Liver Disease\indian_liver_patient.csv")

# view sample from the data 
#print(liver_df.head(3)) #by defult = 5

# handle missing data
#print(liver_df.info())
#print(liver_df.isna().sum())

#print(liver_df["Albumin_and_Globulin_Ratio"])
avarage_AGR =liver_df["Albumin_and_Globulin_Ratio"].mean() 
liver_df["Albumin_and_Globulin_Ratio"].fillna(avarage_AGR , inplace=True)
#print(liver_df.isna().sum())


# map labled data to number 
liver_df["Gender"] = liver_df["Gender"].map({"Female": 0 , "Male":1 })
print(liver_df.head())

x = liver_df.drop("Dataset" , axis =1)
y = liver_df["Dataset"]


# split data to train/test
x_train , x_test , y_train , y_test = train_test_split(x ,y , test_size=0.3)     # test by 30%


# choose modle (estimator)
#model = svm.SVC(kernel = 'rbf' , C =1 , gamma = 0.01)
# anthor estimator 
from sklearn.ensemble import RandomForestClassifier
model=RandomForestClassifier(bootstrap=True, ccp_alpha=0.0, class_weight=None,
                       criterion='gini', max_depth=7, max_features='sqrt',
                       max_leaf_nodes=None, max_samples=None,
                       min_impurity_decrease=0.0, min_impurity_split=None,
                       min_samples_leaf=1, min_samples_split=2,
                       min_weight_fraction_leaf=0.0, n_estimators=30, n_jobs=-1,
                       oob_score=False, random_state=None, verbose=0,
                       warm_start=False)



# testing
# train (input , output)
scalled = model.fit(x_train , y_train )

# validate modle 
print(model.score(x_train , y_train))
print(model.score(x_test , y_test))


from sklearn.model_selection import cross_val_score
validator = cross_val_score(model ,x, y ,cv =5)
print(np.mean(validator)) 

'''

from sklearn.model_selection import cross_val_score
validator = cross_val_score(model ,x, y ,cv =5)
print(np.mean(validator)) 


model.fit(x_train , y_train)
print(model.score(x_test , y_test))
'''

'''
# tune modle prams
parameters ={'n_estimators':(10,30,50,70,90,100),
            'criterion':('gini' , 'entropy'),
            'max_depth':(3,5,7,9),
            'max_features':('auto' , 'sqrt'),
            'min_samples_split':(2,4,6)
}
grid = GridSearchCV(RandomForestClassifier(n_jobs=-1,oob_score=False), param_grid=parameters ,cv =3 , verbose=True)

tune_grid = grid.fit(x_train , y_train)
print(tune_grid.best_estimator_)
'''


# save model
#pickle.dump(model , open(r"F:\python ml\projects\Liver Disease\liversavemo.pkl","wb"))


from sklearn.metrics import classification_report
y_predicted = model.predict(x_test)
print(classification_report(y_test , y_predicted))


