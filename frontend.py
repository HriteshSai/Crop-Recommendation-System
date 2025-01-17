from joblib import load
# model = load(r"C:\Users\Bruger\OneDrive\Desktop\Python\PROJECT\CRS.joblib")
# cropName = ['rice', 'maize', 'chickpea', 'kidneybeans','pigeonpeas', 'mothbeans',
#  'mungbean', 'blackgram', 'lentil', 'pomegranate', 'banana', 'mango', 'grapes',
#  'watermelon', 'muskmelon', 'apple', 'orange', 'papaya', 'coconut', 'cotton', 'jute', 'coffee']
# while(True):
#    value = []
#    value.append(float(input("Enter Nitrogen Content        :")))
#    value.append(float(input("Enter Phosphorous Content     :")))
#    value.append(float(input("Enter Potassium Content       :")))
#    value.append(float(input("Enter Temparuture             :")))
#    value.append(float(input("Enter Humidity                :")))
#    value.append(float(input("Enter pH                      :")))
#    value.append(float(input("Enter Rainfall                :")))
#    print("RECOMMENDED CROP IS: ", cropName[model.predict([value])[0]])
#    break

def cropSystem(n, p, k, temp, h, ph, rf):
   model = load(r"C:\Users\Bruger\OneDrive\Desktop\Python\PROJECT\CRS.joblib")
   cropName = ['rice', 'maize', 'chickpea', 'kidneybeans','pigeonpeas', 'mothbeans',   
 'mungbean', 'blackgram', 'lentil', 'pomegranate', 'banana', 'mango', 'grapes',
 'watermelon', 'muskmelon', 'apple', 'orange', 'papaya', 'coconut', 'cotton', 'jute', 'coffee']

   value = []
   value.append(float(n))
   value.append(float(p))
   value.append(float(k))
   value.append(float(temp))
   value.append(float(h))
   value.append(float(ph))
   value.append(float(rf))
   return cropName[model.predict([value])[0]]


