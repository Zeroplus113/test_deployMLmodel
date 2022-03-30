import pandas as pd
import numpy as np
import pickle

def md_prediction(temp,humid,light,soil,ec):
    data = [temp,humid,light,soil,ec]

    x_test = np.array(data)
    x_test = x_test.reshape((1,-1))

    filename = "classification.sav"
    loaded_model = pickle.load(open(filename, 'rb'))

    result = loaded_model.predict(x_test)
    advice = ""

    if result ==['cluster_0']:
        advice = "เวลากลางคืนไม่จำเป็นต้องได้รับน้ำ"
        logo = "bi bi-cloud-moon-fill"
    elif result == ['cluster_1']:
        advice = "อากาศร้อนต้องการน้ำเล็กน้อย"
        logo = "bi bi-cloud-moon-fill"
    elif result == ['cluster_2']:
        advice = "ความชื้นเหมาะสมกับเมลอน"
        logo = "bi bi-cloud-moon-fill"
    elif result == ['cluster_3']:
        advice = "ความชื้นเหมาะสมกับเมลอน"
        logo = "bi bi-cloud-moon-fill"
    elif result == ['cluster_4']:
        advice = "ต้องการน้ำเล็กน้อย"
        logo = "bi bi-cloud-moon-fill"
    a= [advice,logo]

    return a

# def md_prediction(temp):
#     x_test = np.array(temp)
#     x_test = x_test.reshape((1,-1))

#     filename = "temp_estimate_humid.sav"
#     loaded_model = pickle.load(open(filename, 'rb'))

#     result = loaded_model.predict(x_test)
 
#     return result


