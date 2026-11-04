def main():
    print("This app will count vowel sounds in your entered text") 
    
    matn=(input("lotfan matn khod ra vared konid:")).lower()
    
    h_seddar = {"a":0 ,"e":0 , "i":0 , "o":0 , "u":0 }
    
    for i in matn:
        if i in h_seddar:
            h_seddar[i]+=1
    
    return h_seddar

if __name__ == "__main__":
    print(main())