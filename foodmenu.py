print(">>>>..WELCOME TO FOOD CORNER<<<<..")
print("1=Monday\n2=Tuesday\n3=Wednesday\n4=Thursday\n5=Friday\n6=Saturday\n7=Sunday")
day=int(input("enter the day of weak>>>>........"))
if day==1:
    print("1=breakfast\n2=lunch\n3=dinner")
    choice=int(input("enter what do you want>>>.."))
    if choice==1:
        print("1=burger $200\n2=chai   $60\n3=pigga  $600")
        type=int(input("What do you want>>>.."))
        if type==1:
            print("1=veg burger $100\n2=non burger $200")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=veg burger\nPrice=$100")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=100))*bill-100
                if bill>=100:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=non burger\nprice=$200")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=200))*bill-200
                if bill>=200:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
        elif type==2:
            print("1=Chai         $30\n2=Special Chai $60")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=Chai\nPrice=$30")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=30)*bill)-30
                if bill>=30:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Special Chai\nprice=$60")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=60))*bill-60
                if bill>=60:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
        elif type==3:
            print("1=Pigga     $300\n2=Non Pigga $600")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=Pigga\nPrice=$300")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=300)*bill)-300
                if bill>=300:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Non Pigga\nprice=$600")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=600))*bill-600
                if bill>=600:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")

    elif choice==2:
        print("1=Dal Roti      $150\n2=Roti Sabji    $225\n3=Chhole Chawal $300")
        type=int(input("What do you want>>>.."))
        if type==1:
            print("1=Half $75\n2=Full $150")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=Half\nPrice=$75")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=75))*bill-75
                if bill>=75:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Full\nprice=$150")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=150))*bill-150
                if bill>=150:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
        elif type==2:
            print("1=Half $125\n2=Full $100")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=Half\nPrice=$125")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=125)*bill)-125
                if bill>=125:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Full\nprice=$225")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=225))*bill-225
                if bill>=225:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
        elif type==3:
            print("1=Half $150\n2=Full $300")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=Half\nPrice=$150")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=150)*bill)-150
                if bill>=150:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Full\nprice=$300")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=300))*bill-300
                if bill>=300:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
    elif choice==3:
        print("Mater paneer   $1000\n2=Sahi Paneer  $1200\n3=Masroom      $1400")                
        type=int(input("What do you want>>>.."))
        if type==1:
            print("1=Half $500\n2=Full $1000")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=Half\nPrice=$500")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=500))*bill-500
                if bill>=500:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Full\nprice=$1000")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=1000))*bill-1000
                if bill>=1000:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
        elif type==2:
            print("1=Half $600\n2=Full $1200")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=Half\nPrice=$600")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=600)*bill)-600
                if bill>=600:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Full\nprice=$1200")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=1200))*bill-1200
                if bill>=1200:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
        elif type==3:
            print("1=Half $700\n2=Full $1400")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=Half\nPrice=$700")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=700)*bill)-700
                if bill>=700:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Full\nprice=$1400")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=1400))*bill-1400
                if bill>=1400:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")

elif day==2:
    print("1=breakfast\n2=lunch\n3=dinner")
    choice=int(input("enter what do you want>>>.."))
    if choice==1:
        print("1=Channe $125\n2=chai   $40\n3=Samose $100")
        type=int(input("What do you want>>>.."))
        if type==1:
            print("1=Half $50\n2=Full $125")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=veg burger\nPrice=$100")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=50))*bill-50
                if bill>=50:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Full\nprice=$125")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=125))*bill-125
                if bill>=125:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
        elif type==2:
            print("1=Chai         $20\n2=Special Chai $40")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=Chai\nPrice=$20")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=20)*bill)-20
                if bill>=20:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Special Chai\nprice=$40")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=40))*bill-40
                if bill>=40:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
        elif type==3:
            print("1=Half $100\n2=Full $200")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=Half\nPrice=$100")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=100)*bill)-100
                if bill>=100:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Full\nprice=$200")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=200))*bill-200
                if bill>=200:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")

    elif choice==2:
        print("1=Dahi ParaRoti $120\n2=Puri Sabji    $225\n3=Rajma Chawal  $200")
        type=int(input("What do you want>>>.."))
        if type==1:
            print("1=Half $60\n2=Full $120")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=Half\nPrice=$60")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=60))*bill-60
                if bill>=60:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Full\nprice=$120")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=120))*bill-120
                if bill>=120:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
        elif type==2:
            print("1=Half $125\n2=Full $100")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=Half\nPrice=$125")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=125)*bill)-125
                if bill>=125:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Full\nprice=$225")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=225))*bill-225
                if bill>=225:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
        elif type==3:
            print("1=Half $100\n2=Full $200")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=Half\nPrice=$100")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=100)*bill)-100
                if bill>=100:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Full\nprice=$200")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=200))*bill-200
                if bill>=200:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
    elif choice==3:
        print("Chicken       $1500\n2=Sahi Paneer $1000\n3=Maton       $2000")                
        type=int(input("What do you want>>>.."))
        if type==1:
            print("1=Half $7500\n2=Full $7500")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=Half\nPrice=$7500")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=7500))*bill-7500
                if bill>=7500:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Full\nprice=$1500")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=1500))*bill-1500
                if bill>=1500:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
        elif type==2:
            print("1=Half $500\n2=Full $1000")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=Half\nPrice=$500")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=500)*bill)-500
                if bill>=500:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Full\nprice=$1000")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=1000))*bill-1000
                if bill>=1000:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")


elif type==3:
            print("1=Half $1000\n2=Full $2000")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=Half\nPrice=$1000")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=1000)*bill)-1000
                if bill>=1000:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Full\nprice=$2000")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=2000))*bill-2000
                if bill>=2000:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")


elif day==3:
    print("1=breakfast\n2=lunch\n3=dinner")
    choice=int(input("enter what do you want>>>.."))
    if choice==1:
        print("1=Kulfi $40\n2=chai  $40\n3=Milk  $35")
        type=int(input("What do you want>>>.."))
        if type==1:
            print("1=Veg Kulfi      $20\n2=Non Veg Kulfi  $40")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=veg Kulfi\nPrice=$20")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=20))*bill-20
                if bill>=20:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Non Veg KULFI\nprice=$400")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=40))*bill-40
                if bill>=40:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
        elif type==2:
            print("1=Chai         $20\n2=Special Chai $40")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=Chai\nPrice=$20")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=20)*bill)-20
                if bill>=20:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Special Chai\nprice=$40")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=40))*bill-40
                if bill>=40:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
        elif type==3:
            print("1=Half $15\n2=Full $35")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=Half\nPrice=$15")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=15)*bill)-15
                if bill>=15:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Full\nprice=$35")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=35))*bill-35
                if bill>=35:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")

    elif choice==2:
        print("1=Aalu Parata $75\n2=Puri Sabji  $80\n3=Dal Chawal  $90")
        type=int(input("What do you want>>>.."))
        if type==1:
            print("1=Half $30\n2=Full $75")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=Half\nPrice=$30")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=30))*bill-30
                if bill>=30:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Full\nprice=$75")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=75))*bill-75
                if bill>=75:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
        elif type==2:
            print("1=Half $40\n2=Full $80")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=Half\nPrice=$40")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=40)*bill)-40
                if bill>=40:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Full\nprice=$80")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=80))*bill-80
                if bill>=80:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
        elif type==3:
            print("1=Half $45\n2=Full $90")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=Half\nPrice=$45")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=45)*bill)-45
                if bill>=45:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Full\nprice=$90")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=90))*bill-90
                if bill>=90:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
    elif choice==3:
        print("Dal Makhani $400\n2=Lamon Rice  $600\n3=Jeera Rice  $800")                
        type=int(input("What do you want>>>.."))
        if type==1:
            print("1=Half $200\n2=Full $400")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=Half\nPrice=$200")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=200))*bill-200
                if bill>=200:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Full\nprice=$400")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=400))*bill-400
                if bill>=400:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
        elif type==2:
            print("1=Half $300\n2=Full $600")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=Half\nPrice=$300")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=300)*bill)-300
                if bill>=300:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Full\nprice=$600")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=600))*bill-600
                if bill>=600:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
        elif type==3:
            print("1=Half $400\n2=Full $800")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=Half\nPrice=$400")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=400)*bill)-400
                if bill>=400:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Full\nprice=$800")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=800))*bill-800
                if bill>=800:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")


elif day==4:
    print("1=breakfast\n2=lunch\n3=dinner")
    choice=int(input("enter what do you want>>>.."))
    if choice==1:
        print("1=Maggi $180\n2=chai  $40\n3=Lasse $60")
        type=int(input("What do you want>>>.."))
        if type==1:
            print("1=Veg Maggi      $90\n2=Non Veg Maggi  $180")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=veg Maggi\nPrice=$90")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=90))*bill-90
                if bill>=90:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Non Veg Maggi\nprice=$180")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=180))*bill-180
                if bill>=180:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
        elif type==2:
            print("1=Chai         $20\n2=Special Chai $40")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=Chai\nPrice=$20")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=20)*bill)-20
                if bill>=20:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Special Chai\nprice=$40")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=40))*bill-40
                if bill>=40:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
        elif type==3:
            print("1=Half $30\n2=Full $60")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=Half\nPrice=$30")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=30)*bill)-30
                if bill>=30:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Full\nprice=$60")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=60))*bill-60
                if bill>=60:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")

    elif choice==2:
        print("1=Aalu Parata $75\n2=Puri Sabji  $80\n3=Dal Chawal  $90")
        type=int(input("What do you want>>>.."))
        if type==1:
            print("1=Half $30\n2=Full $75")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=Half\nPrice=$30")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=30))*bill-30
                if bill>=30:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Full\nprice=$75")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=75))*bill-75
                if bill>=75:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
        elif type==2:
            print("1=Half $40\n2=Full $80")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=Half\nPrice=$40")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=40)*bill)-40
                if bill>=40:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Full\nprice=$80")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=80))*bill-80
                if bill>=80:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
        elif type==3:
            print("1=Half $45\n2=Full $90")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=Half\nPrice=$45")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=45)*bill)-45
                if bill>=45:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Full\nprice=$90")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=90))*bill-90
                if bill>=90:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
    elif choice==3:
        print("Chicken       $1500\n2=Sahi Paneer $1000\n3=Maton       $2000")                
        type=int(input("What do you want>>>.."))
        if type==1:
            print("1=Half $7500\n2=Full $7500")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=Half\nPrice=$7500")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=7500))*bill-7500
                if bill>=7500:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Full\nprice=$1500")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=1500))*bill-1500
                if bill>=1500:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
        elif type==2:
            print("1=Half $500\n2=Full $1000")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=Half\nPrice=$500")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=500)*bill)-500
                if bill>=500:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Full\nprice=$1000")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=1000))*bill-1000
                if bill>=1000:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
        elif type==3:
            print("1=Half $1000\n2=Full $2000")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=Half\nPrice=$1000")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=1000)*bill)-1000
                if bill>=1000:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Full\nprice=$2000")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=2000))*bill-2000
                if bill>=2000:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")


if day==5:
    print("1=breakfast\n2=lunch\n3=dinner")
    choice=int(input("enter what do you want>>>.."))
    if choice==1:
        print("1=burger $200\n2=chai   $60\n3=pigga  $600")
        type=int(input("What do you want>>>.."))
        if type==1:
            print("1=veg burger $100\n2=non burger $200")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=veg burger\nPrice=$100")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=100))*bill-100
                if bill>=100:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=non burger\nprice=$200")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=200))*bill-200
                if bill>=200:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
        elif type==2:
            print("1=Chai         $30\n2=Special Chai $60")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=Chai\nPrice=$30")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=30)*bill)-30
                if bill>=30:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Special Chai\nprice=$60")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=60))*bill-60
                if bill>=60:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
        elif type==3:
            print("1=Pigga     $300\n2=Non Pigga $600")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=Pigga\nPrice=$300")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=300)*bill)-300
                if bill>=300:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Non Pigga\nprice=$600")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=600))*bill-600
                if bill>=600:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")

    elif choice==2:
        print("1=Dal Roti      $150\n2=Roti Sabji    $225\n3=Chhole Chawal $300")
        type=int(input("What do you want>>>.."))
        if type==1:
            print("1=Half $75\n2=Full $150")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=Half\nPrice=$75")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=75))*bill-75
                if bill>=75:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Full\nprice=$150")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=150))*bill-150
                if bill>=150:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
        elif type==2:
            print("1=Half $125\n2=Full $100")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=Half\nPrice=$125")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=125)*bill)-125
                if bill>=125:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Full\nprice=$225")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=225))*bill-225
                if bill>=225:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
        elif type==3:
            print("1=Half $150\n2=Full $300")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=Half\nPrice=$150")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=150)*bill)-150
                if bill>=150:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Full\nprice=$300")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=300))*bill-300
                if bill>=300:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
    elif choice==3:
        print("Mater paneer   $1000\n2=Sahi Paneer  $1200\n3=Masroom      $1400")                
        type=int(input("What do you want>>>.."))
        if type==1:
            print("1=Half $500\n2=Full $1000")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=Half\nPrice=$500")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=500))*bill-500
                if bill>=500:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Full\nprice=$1000")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=1000))*bill-1000
                if bill>=1000:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
        elif type==2:
            print("1=Half $600\n2=Full $1200")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=Half\nPrice=$600")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=600)*bill)-600
                if bill>=600:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Full\nprice=$1200")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=1200))*bill-1200
                if bill>=1200:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
        elif type==3:
            print("1=Half $700\n2=Full $1400")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=Half\nPrice=$700")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=700)*bill)-700
                if bill>=700:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Full\nprice=$1400")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=1400))*bill-1400
                if bill>=1400:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")


elif day==6:
    print("1=breakfast\n2=lunch\n3=dinner")
    choice=int(input("enter what do you want>>>.."))
    if choice==1:
        print("1=Channe $125\n2=chai   $40\n3=Samose $100")
        type=int(input("What do you want>>>.."))
        if type==1:
            print("1=Half $50\n2=Full $125")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=veg burger\nPrice=$100")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=50))*bill-50
                if bill>=50:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Full\nprice=$125")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=125))*bill-125
                if bill>=125:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
        elif type==2:
            print("1=Chai         $20\n2=Special Chai $40")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=Chai\nPrice=$20")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=20)*bill)-20
                if bill>=20:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Special Chai\nprice=$40")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=40))*bill-40
                if bill>=40:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
        elif type==3:
            print("1=Half $100\n2=Full $200")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=Half\nPrice=$100")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=100)*bill)-100
                if bill>=100:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Full\nprice=$200")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=200))*bill-200
                if bill>=200:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")

    elif choice==2:
        print("1=Dahi ParaRoti $120\n2=Puri Sabji    $225\n3=Rajma Chawal  $200")
        type=int(input("What do you want>>>.."))
        if type==1:
            print("1=Half $60\n2=Full $120")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=Half\nPrice=$60")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=60))*bill-60
                if bill>=60:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Full\nprice=$120")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=120))*bill-120
                if bill>=120:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
        elif type==2:
            print("1=Half $125\n2=Full $100")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=Half\nPrice=$125")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=125)*bill)-125
                if bill>=125:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Full\nprice=$225")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=225))*bill-225
                if bill>=225:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
        elif type==3:
            print("1=Half $100\n2=Full $200")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=Half\nPrice=$100")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=100)*bill)-100
                if bill>=100:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Full\nprice=$200")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=200))*bill-200
                if bill>=200:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
    elif choice==3:
        print("Chicken       $1500\n2=Sahi Paneer $1000\n3=Maton       $2000")                
        type=int(input("What do you want>>>.."))
        if type==1:
            print("1=Half $7500\n2=Full $7500")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=Half\nPrice=$7500")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=7500))*bill-7500
                if bill>=7500:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Full\nprice=$1500")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=1500))*bill-1500
                if bill>=1500:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
        elif type==2:
            print("1=Half $500\n2=Full $1000")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=Half\nPrice=$500")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=500)*bill)-500
                if bill>=500:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Full\nprice=$1000")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=1000))*bill-1000
                if bill>=1000:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
        elif type==3:
            print("1=Half $1000\n2=Full $2000")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=Half\nPrice=$1000")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=1000)*bill)-1000
                if bill>=1000:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Full\nprice=$2000")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=2000))*bill-2000
                if bill>=2000:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")

elif day==7:
    print("1=breakfast\n2=lunch\n3=dinner")
    choice=int(input("enter what do you want>>>.."))
    if choice==1:
        print("1=Kulfi $40\n2=chai  $40\n3=Milk  $35")
        type=int(input("What do you want>>>.."))
        if type==1:
            print("1=Veg Kulfi      $20\n2=Non Veg Kulfi  $40")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=veg Kulfi\nPrice=$20")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=20))*bill-20
                if bill>=20:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Non Veg KULFI\nprice=$400")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=40))*bill-40
                if bill>=40:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
        elif type==2:
            print("1=Chai         $20\n2=Special Chai $40")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=Chai\nPrice=$20")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=20)*bill)-20
                if bill>=20:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Special Chai\nprice=$40")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=40))*bill-40
                if bill>=40:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
        elif type==3:
            print("1=Half $15\n2=Full $35")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=Half\nPrice=$15")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=15)*bill)-15
                if bill>=15:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Full\nprice=$35")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=35))*bill-35
                if bill>=35:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")

    elif choice==2:
        print("1=Aalu Parata $75\n2=Puri Sabji  $80\n3=Dal Chawal  $90")
        type=int(input("What do you want>>>.."))
        if type==1:
            print("1=Half $30\n2=Full $75")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=Half\nPrice=$30")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=30))*bill-30
                if bill>=30:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Full\nprice=$75")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=75))*bill-75
                if bill>=75:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
        elif type==2:
            print("1=Half $40\n2=Full $80")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=Half\nPrice=$40")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=40)*bill)-40
                if bill>=40:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Full\nprice=$80")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=80))*bill-80
                if bill>=80:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
        elif type==3:
            print("1=Half $45\n2=Full $90")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=Half\nPrice=$45")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=45)*bill)-45
                if bill>=45:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Full\nprice=$90")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=90))*bill-90
                if bill>=90:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
    elif choice==3:
        print("Dal Makhani $400\n2=Lamon Rice  $600\n3=Jeera Rice  $800")                
        type=int(input("What do you want>>>.."))
        if type==1:
            print("1=Half $200\n2=Full $400")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=Half\nPrice=$200")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=200))*bill-200
                if bill>=200:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Full\nprice=$400")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=400))*bill-400
                if bill>=400:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
        elif type==2:
            print("1=Half $300\n2=Full $600")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=Half\nPrice=$300")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=300)*bill)-300
                if bill>=300:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Full\nprice=$600")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=600))*bill-600
                if bill>=600:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
        elif type==3:
            print("1=Half $400\n2=Full $800")
            choose=int(input("what do you choose>>>.."))
            if choose==1:
                print("1=Half\nPrice=$400")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=400)*bill)-400
                if bill>=400:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)   
                else:
                    print("Stop")
            elif choose==2:
                print("2=Full\nprice=$800")
                bill=int(input("enter the bill paying price now>>>.."))
                e=(int(bill>=800))*bill-800
                if bill>=800:
                    print("Thankyou you can go now") 
                    print("Please take your payment receipt>>>..",e)
                else:
                    print("STOP")  