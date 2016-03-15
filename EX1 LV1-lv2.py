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
zhs1 = [z1,h1,s1]
zhs2 = [z2,h2,s2]
zhs3 = [z3,h3,s3]
zhs4 = [z4,h4,s4]
zhs5 = [z5,h5,s5]
zhs= ["  ".join(zhs1),"  ".join(zhs2),"  ".join(zhs3),"  ".join(zhs4)
,"  ".join(zhs5)]

zsh1 = [z1,s1,h1]
zsh2 = [z2,s2,h2]
zsh3 = [z3,s3,h3]
zsh4 = [z4,s4,h4]
zsh5 = [z5,s5,h5]
zsh= ["  ".join(zsh1),"  ".join(zsh2),"  ".join(zsh3),"  ".join(zsh4)
,"  ".join(zsh5)]

szh1 = [s1,z1,h1]
szh2 = [s2,z2,h2]
szh3 = [s3,z3,h3]
szh4 = [s4,z4,h4]
szh5 = [s5,z5,h5]
szh= ["  ".join(szh1),"  ".join(szh2),"  ".join(szh3),"  ".join(szh4)
,"  ".join(szh5)]

shz1 = [s1,h1,z1]
shz2 = [s2,h2,z2]
shz3 = [s3,h3,z3]
shz4 = [s4,h4,z4]
shz5 = [s5,h5,z5]
shz= ["  ".join(shz1),"  ".join(shz2),"  ".join(shz3),"  ".join(shz4)
,"  ".join(shz5)]

hsz1 = [h1,s1,z1]
hsz2 = [h2,s2,z2]
hsz3 = [h3,s3,z3]
hsz4 = [h4,s4,z4]
hsz5 = [h5,s5,z5]
hsz= ["  ".join(hsz1),"  ".join(hsz2),"  ".join(hsz3),"  ".join(hsz4)
,"  ".join(hsz5)]

hzs1 = [h1,z1,s1]
hzs2 = [h2,z2,s2]
hzs3 = [h3,z3,s3]
hzs4 = [h4,z4,s4]
hzs5 = [h5,z5,s5]
hzs= ["  ".join(hzs1),"  ".join(hzs2),"  ".join(hzs3),"  ".join(hzs4)
,"  ".join(hzs5)]
for i in range(5):
    print zhs[i]
