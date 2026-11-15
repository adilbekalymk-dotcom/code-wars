# write a function that will take the number of petals of each flower and return true if they are in love and false if they not
def lovefunc(flower1 , flower2):
    return (flower1 + flower2) % 2 ==1

print (lovefunc(1, 4)) 
print (lovefunc(2, 2)) 