#!/usr/bin/env python
# coding: utf-8

# In[2]:
import sys
if len(sys.argv) > 1:
    x = sys.argv[1]
    print(x)

dr = {'Gastroesophageal reflux disease': {'symptoms': ['reflux', 'food moves back into my mouth', 'acid moves back into my mouth', 'bile moves back into my mouth'], 'treatment': 'Motilium 3 times per day and Omebrazol 1 time per day'},
      'Gastritis disease': {'symptoms': ['hiccups', 'nausea', 'vomiting', 'indigestion', 'bloating', 'appetite loss', 'black stool'], 'treatment': 'gavscon 3 time per day and omebrazol 1 time per day '},
      'Peptic ulcer disease': {'symptoms': ['abdominal pain', 'nausea', 'vomiting', 'inability to drink fluids', 'feeling hungry after eating', 'fatigue', 'weight loss', 'black tarry stool', 'chest pain'], 'treatment': 'Please consult a doctor for taking Antibiotics and Proton pump inhibitors'},
      'Viral gastroenteritis disease': {'symptoms': ['vomiting', 'diarrhea'], 'treatment': 'Antinal 3 times per day and Flagil 3 times per day if need be '},
      'Hiatal hernia': {'symptoms': ['bloating', 'belching pain', 'bitter taste in your throat'], 'treatment': 'Antacids and H-2 receptor blockers'},
      'Gastroparesis': {'symptoms': ['nausea', 'vomiting', 'weight loss', 'bloating', 'heartburn'], 'treatment': 'Gut motility stimulator and Antiemetic'},
      'Stomach cancer': {'symptoms': ['fatigue', 'stomach pain', 'loss of appetite', 'severe heartburn', 'heartburn', 'fullness', 'stomach fullness', 'indigestion', 'severe indigestion', 'weight loss'], 'treatment': 'Urgent medical attention is usually recommended!!'},
      'Helicobacter pylori ': {'symptoms': ['burning pain', 'frequent burping', 'burping', 'nausea'], 'treatment': 'Antibiotic 2 times per day\n Omibrazol 1 time per day\n Flagil 3 times per day'},
      'chronic constipation': {'symptoms': ['hard stools', ' lumpy stool', 'not pooping enough', 'lumpy poop', 'not pooping all'], 'treatment': 'Include plenty of high-fiber foods in your diet, Eat fewer processed foods, and dairy and meat products, Drink a lot of fluids'},
      'Liver fibrosis disease': {'symptoms': ['jaundice', 'yellowing of the skin', 'yellowing of the eyes'], 'treatment': 'Urgent medical attention is usually recommended!!'}}


# In[3]:


# x = input("Enter your symptoms \n")
symptom = x.split(",")
count = 0
flag = -1
disease = dict()

for item in dr:
    for symp in symptom:
        if symp in dr[item]['symptoms']:
            if item in disease:
                disease[item] = disease[item] + 1
            else:
                disease[item] = 1
            continue


for item in disease:
    if disease[item] == len(symptom):
        flag = 1
        count += 1
        perc = int((len(symptom)/len(dr[item]['symptoms']))*100)
        print("We are", perc, "% sure that you may have", item,
              "\n", "You should take", dr[item]['treatment'], "\n")

if flag == -1:
    print('Sorry your disease is not found, please consult a doctor or enter other symptoms')

if count > 1:
    print("THE RESULT MAY NOT BE ACCURATE BUE TO UNSPECIFIC SYMPTOMS PLEASE ENTER MORE SYMPTOMS OR CONSULT A DOCTOR")


# In[19]:
