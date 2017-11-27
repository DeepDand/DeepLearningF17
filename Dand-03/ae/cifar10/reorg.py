import pandas as pd
import os
df = pd.read_csv('trainLabels.csv')
text_file = open('conversion.csv', 'w')                                               
text_file.write("fname,old,label\n")                                          

cls = 0
for label in df.label.unique():
  cls = cls + 1
  print label
  data = df[df['label']==label]
  batch = 0
  cnt = 0
  for index, row in data.iterrows():
    if (cnt%1000)==0:
      batch = batch + 1
    #print row
    #print batch
    #print cnt
    fname_old = str(row['id']) + '.png' 
    fname_new = 'B' + "{:0>2}".format(batch) + '_C' + "{:0>2}".format(cls) + '_' + "{:0>4}".format(cnt%1000) + '.png'
    print fname_old
    print fname_new
    os.rename(fname_old, fname_new)
    text_file.write(fname_new + "," + fname_old + ',' + label + '\n')

    cnt = cnt + 1
  #break

text_file.close() 


