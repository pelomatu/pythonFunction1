def input_accNo():
    accNo = input("Faka inombolo ye akhawunti  yakho  : ")
    return accNo

def input_password():
    password = input("faka inombolo yokuvula: ")
    return password

def input_inBalance():
    inBalance = float(input("Faka ibhalansi yokuqala : "))
    return inBalance

def validation(password,pw):
     while (password != pw):
         password = input("Akuyiyo inombolo yokuvula echanekileyo le,phinda ufake echanekileyo")
     print("Yinombolo echanekileyo le")

def Deposit(inibal,p_word,acc_n):
   ans = input("Uyafuna na ukufaka imali kwi akhawunti yakho?")
   if ans == "ewe"or ans == "Ewe"or ans == "EWE":
      answr = input("Yiyo na le akhawunti ufuna ukuyithumelela le: "+ acc_n)
      if answr == "ewe" or answr == "Ewe" or answr == "EWE":
           amount= float(input(" Bhala lemali ufuna ukuyifaka kwi akhawunti yakho"))
           password = input_password()
           validation(password,p_word)
           print("Ingenile imali ekuyi R ", amount, " kwi akhawunti engu ", acc_n)
           current = inibal + amount
           return current
      else:
          acc_n = input("Faka inombolo ye akhawunti yakho elungileyo")
          amount = float(input(" Bala lemali ufuna ukuyifaka kwi akhawunti yakho"))
          password = input_password()
          validation(password, p_word)
          print("Ingenile imali ekuyi R ", amount, " kwi akhawunti engu ", acc_n)
          current = inibal + amount
          return current
   else:
       current = inibal
       return current

def Withdraw(current_B,p):
    answ= input("Uyafuna ukukhupha imali?")
    if answ == "ewe"or answ == "Ewe" or answ == "EWE":
       Amount= float(input(" Faka imali ofuna ukuyikhupha"))
       password = input_password()
       validation(password,p)
       print("Ukhuphe imali engange R ", Amount, "kwi akhawunti yakho")
       C_bal =  current_B - Amount
       return C_bal
    else:
        C_bal = current_B
        return C_bal

def Display(C_balance,pas):
    answer = input("Uyafuna na ukubona imali eshiyekileyo kwi akhawunti yakho")
    if answer == "ewe" or answer == "Ewe" or answer == "EWE":
        psw = input("Faka inombolo yokuvula echanekileyo")
        validation(psw,pas)
        print(" Imali eshiyekileyo kwi akhawunti yakho yebhanki yi : R" , C_balance )

    print("Usagqibile ebhankini okwangoku siyabulela siyibhanki ubenohambo oluhle")

if __name__ == '__main__':
    acc= input_accNo()
    passw= input_password()
    Bal =input_inBalance()
    cur = Deposit(Bal,passw,acc)
    Curr = Withdraw(cur,passw)
    Display(Curr,passw)