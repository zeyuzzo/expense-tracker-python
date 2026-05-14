print ("welcone to expence tracker ")
dict = {
    "food" : {},
    "trvel" : {},
    "shopping":{},
    "study": {}
}
print("0 - to add expence")
print("9 - to calcutate total")
print("8 - to exit")

first = input("selcect one of the above : ")
while True:
   if first == "0":
    while True :
      print("1 - food ")
      print("2 - travel ")
      print("3 - shopping ")
      print("4 - study ")
      
      
      name = input("enter expence name : ")
      price = int(input("enter the price of expence: "))

      sel = int(input("select one of the above : "))
      
      if sel == 1:
         dict["food"][name] = price
         print(dict["food"])
         new = open("food.txt", "a")
         new.write(str({name:price}) + "\n")
         new.close()       
      elif sel == 2:
         dict["trvel"][name] = price
         print(dict["trvel"])
         new = open("travelr.txt"  ,"a")
         new.write(str({name : price}) +"\n")
         new.close()
      elif sel == 3:
         dict["shopping"][name] = price
         print(str(dict["shopping"]))
         new = open("shopping.txt","a")
         new.write(str({name :price})+"\n")
         new.close()
      elif sel == 4:
         dict["study"][name] = price
         print(dict["study"])
         new = open("study.txt" , "a")        
         new.write(str({name:price}) + "\n")
         new.close()
      
      else:
         print("invalid input")
      
   elif first == "9":
      print("1 - food")
      print("2 - travel ")
      print("3 - shopping")
      print("4 - study ")
      print("5 - all of the above")
      second = input("select one of the above :  ")


      if second == "1":
         filefood = open("food.txt","r")
         total = 0
         for line in filefood:
            ftotal = eval(line)
            for value in ftotal.values():
               total +=value
               print(total)
         filefood.close()
      elif second == "2" :
         filetravel = open("travelr.txt","r")
         total = 0
         for line in filetravel:
            ttotal = eval(line)
            for value in ttotal.values():
               total += value
               print(total)
         
         filetravel.close()
      elif second == "3":
         fileshopping = open("shopping.txt","r")
         total = 0
         for line in fileshopping:
            stotal = eval(line)
            for value in stotal.values():
               total += value
               print(total)
         fileshopping.close()
      elif second == "4":
         filestudy = open("study.txt", "r")
         total = 0
         for line in filestudy:
            sstotal = eval(line)
            for value in sstotal.values():
               total += value
            print(total)
            filestudy.close()    
      elif second == "5":
         ffulltotal = open("food.txt","r")
         tfultotal = open("travelr.txt","r")
         sfultravel = open("shopping.txt","r")
         ssfultravel = open("study.txt","r")
          
         total = 0
         for line in ffulltotal:
            
            x = eval(line)
            for value in x.values():
               total += value
               xx = print(total)

         tftotal = 0   
         for line in tfultotal:
            y = eval(line)
            for value in y.values():
               tftotal += value
               yy =  print(tftotal)
            
         sftotal = 0
         for line in sfultravel:
            z = eval(line)
            for value in z.values():
               sftotal += value
               zz = print(sftotal)

         ssftotal = 0  
         for line in ssfultravel:
            c = eval(line)
            for value in c.values():
               ssftotal += value
               cc = print(ssftotal)
            
         b = total +tftotal + sftotal + ssftotal
         print("total = ",b)
         ffulltotal.close()
         tfultotal.close()
         sfultravel.close()
         ssfultravel.close()
      else:
         print("invalid input")
   
   elif first == "8":
      break
   else:
      print("invlid input")

     



