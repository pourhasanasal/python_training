def jdvl_zrb(size=10):
    size=(int(input("chand dar chand bashe jadval zarb? fgt yek adad vared konid: ")))
    jdvl=[]

    for i in range(1, size+1):
        radif=[]

        for j in range(1,size+1):
            radif.append( i*j ) 

        jdvl.append(radif)

    for radif in jdvl: 
        for adad in radif:
            print(f"{adad:4}" , end="")
        

jdvl_zrb()


