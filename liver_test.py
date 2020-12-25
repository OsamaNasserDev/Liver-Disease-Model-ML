import pickle
import numpy as np
clf = pickle.load(open(r"F:\python ml\projects\Liver Disease\liversavemo.pkl","rb"))

age = float(input("Enter your age : "))

Gender = str(input("Enter your Gender : "))
if Gender == "male" :
    Gender = 1
elif Gender == "female"  :
    Gender = 0
else:
    print("The value you entered is wrong. Please try again ")
    exit()

Total_Bilirubin = float(input("Enter Total_Bilirubin : "))
Direct_Bilirubin = float(input("Enter Direct Bilirubin : "))
Alkaline_Phosphotase = float(input("Enter Alkaline Phosphotase : "))
Alamine_Aminotransferase = float(input("Enter Alamine Aminotransferase : "))
Aspartate_Aminotransferase = float(input("Enter Aspartate Aminotransferase : "))
Total_Protiens = float(input("Enter Total_Protiens : "))
Albumin = float(input("Enter Albumin : "))
Albumin_and_Globulin_Ratio = float(input("Enter Albumin and Globulin Ratio : "))



test = np.array([[age,   Gender ,Total_Bilirubin,    Direct_Bilirubin ,   Alkaline_Phosphotase ,   Alamine_Aminotransferase,    Aspartate_Aminotransferase,   Total_Protiens, Albumin,Albumin_and_Globulin_Ratio ]])
predicition = clf.predict(test)
if predicition == 1:
    print("you are diganosed with liver deise")
else:
    print("you are fine")
