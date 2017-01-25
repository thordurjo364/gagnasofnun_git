#25.01.2017
#Þórður Jónatansson
#GSÖ gitverkefni

skra=input("skýra skrá : ")
skra=skra+".txt"
minskra=open(skra,'w+')
texti=input("skráðu texta :")
minskra.write(texti)

minskra=exit

minskra=open(skra,'w+')
texti1=input("sláðu inn texta :")
minskra.write(texti1)
texti2=input("sláðu inn texta :")
minskra.write(texti2)
texti3=input("sláðu inn texta :")
minskra.write(texti3)
allirtextar=texti1,texti2,texti3
minskra=exit
print(allirtextar)