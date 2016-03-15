print '#####  #   #  #####\n   #   #   #  #     \n  #    #####  #####\n #     #   #      #\n#####  #   #  #####'
z1 = "#####"
z2 ="   # "
z3="  #  "
z4 =" #   "
z5 =z1
h5=h4=h2=h1="#   #"
h3=z1=s1=s3=s5="#####"
s2="#    "
s4="    #"
zh1 = [z1,h1,s1]
zh2 = [z2,h2,s2]
zh3 = [z3,h3,s3]
zh4 = [z4,h4,s4]
zh5 = [z5,h5,s5]
zhs= ["  ".join(zh1),"  ".join(zh2),"  ".join(zh3),"  ".join(zh4)
,"  ".join(zh5)]
for i in range(5):
    print zhs[i]
hz1 = [s1,h1,z1]
hz2 = [s2,h2,z2]
hz3 = [s3,h3,z3]
hz4 = [s4,h4,z4]
hz5 = [s5,h5,z5]
shz= ["  ".join(hz1),"  ".join(hz2),"  ".join(hz3),"  ".join(hz4)
,"  ".join(hz5)]
for i in range(5):
    print shz[i]