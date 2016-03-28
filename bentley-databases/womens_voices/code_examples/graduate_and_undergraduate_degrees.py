import json
import matplotlib.pyplot as plt

undergraduate = 0
graduate = 0
total = 0

with open("../womens_voices.json", mode="r") as f:
    alumnae = json.load(f)
    
    for id_alumna_dict in alumnae:
        for id, alumna in id_alumna_dict.iteritems():
        
            if alumna.get("degrees", ""):
                for degree in alumna.get("degrees", ""):
                    total += 1
                    if degree.get("type", "") == "graduate":
                        graduate += 1
                    elif degree.get("type", "") == "undergraduate":
                        undergraduate += 1

# Data to plot
labels = "Undergraduate", "Graduate"
counts = undergraduate, graduate
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0)  # explode 1st slice

# Plot
plt.pie(counts, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')
plt.show()
