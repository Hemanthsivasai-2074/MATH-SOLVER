import matplotlib.pyplot as plt
import numpy as np
from sympy import *
import math
from fractions import Fraction


def areas():
    while True:
        print("Enter the name of figure Eg:SQUARE,RECTANGLE ETC...")
        print("Enter STOP to stop the FUNCTION and 11 to stop the PROGRAMME.")
        fig = input().lower()
        if fig == "square":
            print("Enter the side of the square: ")
            side = input().lower()
            while True:
                try:
                    if side.isdigit():
                        s = int(side)
                        area = s**2
                        print("Area of the Square is", area, "sq.units.")
                        break
                    elif side == "stop":
                        print("Ending the program square.")
                    else:
                        print("Oops! Enter an integer.")
                        break
                except ValueError:
                    print("Oops! Enter an integer.")

        elif fig == "rectangle":
            lr = input("Enter the length of the rectangle:").lower()
            br = input("Enter the breadth of the rectangle:").lower()
            while True:
                try:
                    if lr.isdigit() and br.isdigit():
                        l = int(lr)
                        b = int(br)
                        area = l * b
                        print("Area of the rectangle is", area, "sq.units.")
                        break
                    elif lr == "stop" or br == "stop":
                        print("Ending the program rectangle.")
                    else:
                        print("Oops! Enter an integer.")
                        break
                except ValueError:
                    print("Oops! Enter an integer.")

        elif fig == "triangle":
            bt = input("Enter the base of the triangle:").lower()
            ht = input("Enter the height of the triangle:").lower()
            while True:
                try:
                    if bt.isdigit() and ht.isdigit():
                        b = int(bt)
                        h = int(ht)
                        area = (b + h) / 2
                        print("Area of triangle is", area, "sq.units.")
                        break
                    elif bt == "stop" or ht == "stop":
                        print("Ending the program triangle.")
                    else:
                        print("Oops! Enter an integer.")
                        break
                except ValueError:
                    print("Oops! Enter an integer.")
        elif fig == "parallelogram":
            print("ENTER THE BASE:")
            bp = input().lower()
            print("ENTER THE HEIGHT:")
            hp = input().lower()
            while True:
                try:
                    if bp.isdigit() and hp.isdigit():
                        bp = int(bp)
                        hp = int(hp)
                        print("THE AREA OF PARALLALOGRAM IS ", bp * hp,
                              "sq.units")
                        break
                    elif bp == "stop" or hp == "stop":
                        print("Ending the program parallelogram.")
                    else:
                        print("Oops! Enter an integer.")
                        break
                except ValueError:
                    print("Oops! Enter an integer.")
        elif fig == "circle":
            print("ENTER THE RADIUS OF CIRCLE :")
            rc = input().lower()
            while True:
                try:
                    if rc.isdigit():
                        rc = float(rc)
                        print("THE AREA OF CIRCLE IS", 3.1415 * rc * rc,
                              "sq.units")
                        break
                    elif rc == "stop":
                        print("ENTER A NUMBER")
                    else:
                        print("PLEASE ENTER AN INTEGER!!")
                        break
                except ValueError:
                    print("PLEASE ENTER AN INTEGER")

        elif fig == "trapezium":
            print("ENTER THE BASE-1")
            b1t = input().lower()
            print("ENTER THE BASE-2")
            b2t = input().lower()
            print("ENTER THE HEIGHT ")
            htp = input().lower()
            while True:
                try:
                    if (b1t.isdigit() and b2t.isdigit() and htp.isdigit()):
                        b1t = int(b1t)
                        b2t = int(b2t)
                        htp = int(htp)
                        print("THE AREA OF TRAPEZIUM IS",
                              ((b1t + b2t) * htp) / 2, "sq.units")
                        break
                    elif b1t == "stop" or b2t == "stop" or htp == "stop":
                        print("ENTER A NUMBER")
                    else:
                        print("PLEASE ENTER AN INTEGER!!")
                        break
                except ValueError:
                    print("ENTER AN INTEGER!")
        elif fig == "cylinder":
            print("ENTER THE RADIUS")
            rcr = input().lower()
            print("ENTER THE HEIGHT ")
            hcr = input().lower()
            while True:
                try:
                    if rcr.isdigit() and hcr.isdigit():
                        rcr = int(rcr)
                        hcr = int(hcr)
                        print("THE TOTAL SURFACE AREA OF CYLINDER IS ",
                              6.283 * rcr * (rcr + hcr), "sq.units")
                        break
                    elif rcr == "stop" or hcr == "stop":
                        print("ENTER A NUMBER")
                    else:
                        print("PLEASE ENTER AN INTEGER!!")
                        break
                except ValueError:
                    print("PLEASE ENTER AN INTEGER")
        elif fig == "ellipse":
            print("ENTER THE MAJOR AXIS:")
            mje = input().lower()
            print("ENTER THE MINOR AXIS:")
            mne = input().lower()
            while True:
                try:
                    if mje.isdigit() and mne.isdigit():
                        mje = int(mje)
                        mne = int(mne)
                        print("THE AREA OF ELLIPSE IS",
                              3.1415 * (mje / 2) * (mne / 2), "sq.units")
                        break
                    elif mje == "stop" or mne == "stop":
                        print("ENTER A NUMBER")
                    else:
                        print("PLEASE ENTER AN INTEGER!!")
                        break
                except ValueError:
                    print("YOU MUST ENTER AN INTEGER!!")

        elif fig == "cube":
            print("ENTER THE SIDE:")
            sc = input().lower()
            while True:
                try:
                    if sc.isdigit():
                        sc = int(sc)
                        print("THE TOTAL SURFACE AREA OF CUBE IS ",
                              6 * sc * sc, "sq.units")
                        break
                    elif sc == "stop":
                        print("ENTER A NUMBER")
                    else:
                        print("PLEASE ENTER AN INTEGER!!")
                        break
                except ValueError:
                    print("YOU MUST ENTER AN INTEGER!!")

        elif fig == "cone":
            print("ENTER THE RADIUS")
            rc = input().lower()
            print("ENTER THE HEIGHT")
            hc = input().lower()
            while True:
                try:
                    if rc.isdigit() and hc.isdigit():
                        rc = int(rc)
                        hc = int(hc)
                        shc = math.sqrt(hc*2 + rc*2)
                        print("THE AREA OF CONE IS", 3.1415 * rc * (rc + shc),
                              "sq.units")
                        break
                    elif rc == "stop" or hc == "stop":
                        print("ENTER A NUMBER")
                    else:
                        print("PLEASE ENTER AN INTEGER!!")
                        break
                except ValueError:
                    print("YOU MUST ENTER AN INTEGER!!")
        elif fig == "sphere":
            print("ENTER THE RADIUS")
            rsp = input().lower()
            while True:
                try:
                    if rsp.isdigit():
                        rsp = int(rsp)
                        print("THE AREA OF SPHERE IS", 4 * 3.1415 * rsp * rsp,
                              "sq.units")
                        break
                    elif rsp == "stop":
                        print("ENTER A NUMBER")
                    else:
                        print("PLEASE ENTER AN INTEGER!!")
                        break
                except ValueError:
                    print("PLEASE ENTER AN INTEGER")
        elif fig == "hemisphere":
            print("ENTER THE RADIUS:")
            rhs = input().lower()
            while True:
                try:
                    if rhs.isdigit():
                        rhs = int(rhs)
                        print("THE AREA OF HEMISPHERE IS ",
                              3 * 3.1415 * rhs * rhs, "sq.units")
                        break
                    elif rhs == "stop":
                        print("ENTER A NUMBER")
                    else:
                        print("PLEASE ENTER AN INTEGER!!")
                        break
                except ValueError:
                    print("YOU MUST ENTER AN INTEGER!!")
        elif fig == "rectangular prism":
            print("ENTER THE LENGTH:")
            lrt = input().lower()
            print("ENTER THE WIDTH:")
            wrt = input().lower()
            print("ENTER THE HEIGHT:")
            hrt = input().lower()
            while True:
                try:
                    if lrt.isdigit() and wrt.isdigit() and hrt.isdigit():
                        lrt = int(lrt)
                        wrt = int(wrt)
                        hrt = int(hrt)
                        atrp = (wrt * lrt) + (hrt * lrt) + (hrt * wrt)
                        print("THE AREA OF RECTANGULAR TRAPEZIUM IS", 2 * atrp,
                              "sq.units")
                        break
                    elif lrt == "stop" or wrt == "stop" or hrt == "stop":
                        print("ENTER A NUMBER")
                    else:
                        print("PLEASE ENTER AN INTEGER!!")
                        break
                except ValueError:
                    print("PLEASE ENTER AN INTEGER")
        elif fig == "rhombous":
            s1 = input("ENTER THE DIAGONAL 1:").lower()
            s2 = input("ENTER THE DIAGONAL 2:").lower()
            while True:
                try:
                    if s1.isdigit() and s2.isdigit():
                        s1 = int(s1)
                        s2 = int(s2)
                        print("THE AREA OF RHOMBOUS IS:", (1 / 2) * (s1 * s2))
                        break
                    elif s1 == "stop" or s2 == "stop":
                        print("ENTER A NUMBER")
                    else:
                        print("PLEASE ENTER AN INTEGER!!")
                        break
                except ValueError:
                    print("PLEASE ENTER AN INTEGER")
        elif fig == "kite":
            e1 = input("ENTER THE DIAGONAL 1:").lower()
            e2 = input("ENTER THE DIAGONAL 2:").lower()
            while True:
                try:
                    if e1.isdigit() and e2.isdigit():
                        e1 = int(e1)
                        e2 = int(e2)
                        print("THE AREA OF KITE IS:", (1 / 2) * (e1 * e2))
                        break
                    elif e1 == "stop" or e2 == "stop":
                        print("ENTER A NUMBER")
                    else:
                        print("PLEASE ENTER AN INTEGER!!")
                        break
                except ValueError:
                    print("YOU MUST ENTER AN INTEGER!!")
        elif fig == "semi circle" or fig == "semicircle":
            rs = input("ENTER RADIUS OF THE CIRCLE:").lower()
            while True:
                try:
                    if rs.isdigit():
                        rs = int(rs)
                        print("AREA OF SEMI CIRCLE IS",
                              ((1 / 2) * (3.1415 * rs**2)))
                        break
                    elif rs == "stop":
                        print("ENTER A NUMBER")
                    else:
                        print("PLEASE ENTER AN INTEGER!!")
                        break
                except ValueError:
                    print("YOU MUST ENTER AN INTEGER!!")
        elif fig == "sector":
            sa = input("ENTER THE ANGLE OF THE SECTOR(IN DEGREES):").lower()
            while True:
                try:
                    if sa.isdigit():
                        sa = int(sa)
                        print("AREA OF THE SECTOR IS", sa / 360)
                        break
                    elif sa == "stop":
                        print("ENTER A NUMBER")
                    else:
                        print("PLEASE ENTER AN INTEGER!!")
                        break
                except ValueError:
                    print("PLEASE ENTER AN INTEGER")
        elif fig == "stop":
            print("STOPPING THE PROGRAMME")
            break
        else:
            print("SORRY WE DONOT HAVE THAT VALUE")
            print('''
                    s.no -  FIGURES
                      1: square 
                      2:rectangle
                      3:triangle
                      4:parallelogram
                      5:circle
                      6:trapezium
                      7:ellipse
                      8:cube
                      9:rectangular prism
                      10:cylinder
                      11:cone
                      12:sphere
                      13:hemisphere  ''')
            print("PLEASE SELECT THE FIGURE FROM THE ABOVE DATA")


def rootsofquad():
    while True:
        print(
            "NOTE : THE QUADRATIC EQUATION OF FORM ax^2+bx+c CAN ONLY BE FOUND IN THIS PROGRAMME.TYPE OK IF YOU AGREE WITH IT"
        )
        user = input().upper()
        if user =="OK":
            print("WELCOME")
            print("ENTER THE VALUE OF a:")
            va = input().lower()
            print("ENTER THE VALUE OF b:")
            vb = input().lower()
            print("ENTER THE VALUE OF c:")
            vc = input().lower()
            while True:
                if va.isdigit() and vb.isdigit() and vc.isdigit():
                    va = int(va)
                    vb = int(vb)
                    vc = int(vc)
                    eq1 = (vb**2) - (4 * va * vc)
                    eq2 = (eq1)**(1 / 2)
                    eq3 = (-vb + eq2) / 2 * va
                    eq4 = (-vb - eq2) / 2 * va
                    print("THE ROOTS OF THE GIVEN QUADRATIC EQUATION ARE", eq3,
                          eq4)
                    if eq1 >= 0:
                        print("THESE ROOTS ARE REAL ROOTS :)")
                    elif eq1<0:
                        print("OHH LOOKS LIKE THESE ARE  IMAGINARY ROOTS :)")
                        break
                    else:
                      print("Sorry,we did'nt get it.")
                      break
                elif va == "stop" or vb == "stop" or vc == "stop":
                    print("ending the program quadratic equations.")
                    break
                else:
                    print("PLEASE ENTER AN INTEGER!!")
                    break
        elif "stop"==user:
            break
        else:
            print("SORRY ,WE COULD'NT GET THAT!!")


def derivatives():
    while True:
        x, y = symbols('x y')
        print(
            "NOTE: THE X^n NEED TO BE ENTERED AS X*n AND nX NEED TO BE ENTERED AS X*n EXAMPLE:2*X*2+X+3*Y"
        )
        print("TYPE YES TO CONTINUE")
        ag = input().lower()
        if ag == "yes":
            print("ENTER THE FUNCTION")
            expr = input("enter the function:").lower()
            if expr.isdigit():
                expr_diff = Derivative(expr, x)
                print("THE DERIVATIVE IS :", expr_diff.doit())
            elif expr == "stop":
                break
            else:
                print("PLEASE ENTER THE VALUE CORRECTLY")

        elif ag == "stop":
            break
        else:
            print("SORRY,WE COULD'NT GET IT")


def log():
    while True:
        print(
            "IN THIS YOU CAN ONLY GET THE PARTICULAR LOGARITHRM FUNCTION EXAMPLE:LOG2 ,ETC... TYPE YES IF YOU AGREE :)"
        )
        print("TYPE STOP TWO TIMES TO STOP THE PROGRAMME AFTER COMPLETING")
        agree = input().lower()
        if agree=="yes":
          while True:
            val = input("Enter the value :").lower()
            base = input("ENTER THE LOGARITHEMIC BASE:").lower()
            if val == "stop" or base == "stop":
                break
            elif val.isdigit() and base.digit():
              val=int(val)
              base=int(base)
              value = math.log(val, base)
              print("THE VALUE OF LOGARITHEM IS", value)
              break
        elif agree == "stop":
            break
        else:
            print("SORRY,WE COULD'NT GET IT")
            break


def graphs():
    while True:
        print(
            "You are in GRAPH, If you want to continue enter YES or STOP to stop GRAPHS."
        )
        ag = input().lower()
        if "yes" == ag:
            print(
                "Enter the values of X and Y in a single line.Eg:1,2,3,4....")
            try:
                x = list(map(int, input("Enter x-axis values:").split(",")))
                x.sort()
                y = list(map(int, input("Enter y-axis values:").split(",")))
                plt.plot(x, y)
                plt.show(block=False)
                print(
                    "Enter STOP to stop the Operation, else you can continue directly."
                )
            except ValueError:
                print(
                    "Oops! you can enter only numericals or enter same number of x and y values :) "
                )
        elif "stop" == ag:
            break
        else:
            print("SORRY,WE COULD'NT GET IT!")
            break


def pnc():
    while True:
        print(
            "WHAT DO YOU WANT TO FIND PERMUTATION OR COMBINANTION TYPE P FOR PERMUTATION AND C FOR COMBINANTION:"
        )
        print("TYPE STOP TWO TIMES TO STOP THE PROGRAMME AFTER COMPLETING")
        pc = input().lower()
        if pc == "p":
            nob = int(input("Enter the no.of observations:"))
            print("**NOTE** : n MUST BE GREATER THAN r")
            rob = int(input("Enter the choice of observations:"))
            while True:
              try:
                if nob < rob:
                  print(
                        "THE NO.OF OBSERVATIONS MUST BE GREATER THAN THE CHOICE OF OBSERVATIONS!!"
                    )
                  break
                else:
                    nr = math.factorial(nob)
                    dr = math.factorial(nob - rob)
                    print("THE PERMUTATION IS", nr / dr)
                    break
              except ValueError:
                print("please enter a number correctly!!")
        elif pc == "c":
          try:
            nobc = int(input("Enter the no.of observations:"))
            print("**NOTE** : n MUST BE GREATER THAN r")
            robc = int(input("Enter the choice of observations:"))
            ncr = math.factorial(nobc)
            ndr = math.factorial(nobc - robc)
            nrr = math.factorial(robc)
            print("THE COMBINANTION IS", ncr / (ndr * nrr))
            break
          except ValueError:
            print("please enter an integer!!")
        elif "stop" in pc:
            break
        else:
            print("SORRY,WE COULD'NT FIND THE WORD YOU HAVE ENTERED")
            break


def dtof():
    while True:
        print(
            "THIS WILL CONVERT DECIMAL NUMBER INTO A FRACTION.TYPE YES TO CONTINUE AND STOP TO STOP THE PROGRAMME."
        )
        use = input().lower()
        if "yes" in use:
          try:
            dec = input("Enter the decimal:").lower()
            print("THE REQUIRED FRACTION IS ", Fraction(dec))
          except ValueError:
            print("You have to enter an integer!!")

        elif "stop" in use:
            break
        else:
            print("SORRY,WE COULD'NT GET IT")
            break


def dtor():
    while True:
      print(
            "Enter DR to convert degrees to radians and RD to Cconvert radians to degree. "
        )
      try:
        ans = input().lower()
        if "dr" in ans:
            dr = float(input("ENTER DEGREES HERE:"))
            zy = (3.1415 / 180) * dr
            print(dr, "DEGREES =", zy, "RADIANS")
        elif "rd" in ans:
            rd = float(input("ENTER RADIANS HERE:"))
            yz = (180 / 3.1415) * rd
            print(rd, "RADIANS=", yz, "DEGREES")
        elif "stop" in ans:
            break
        else:
            print("SORRY,WE DID'NT GET IT.")
            break
      except ValueError:
        print("Enter the values correctly!!")


def snpr():
    while True:
      sum = 0
      print("Enter P for Parallel circuit and S for series circuit:")
      print("Enter STOP to exit Resistances.")
      res = input().lower()
      if "s"== res:
        try:
          nr = int(input("Enter the number of resistors: "))
          for i in range(nr):
            r = int(input("Enter the resistances:"))
            sum = sum + r
          print("The Equalent Resistance of the series circuit is", sum,".")
        except ValueError:
          print("enter a number!!")
          
      elif "p" == res:
        try:
          ns = int(input("Enter the number of resistors: "))
          for i in range(ns):
            s = int(input("Enter the resistors:"))
            sum = sum + (1 / s)
          print("The Equivalent resistance in parallel circuit is",
                  (1 / sum),".")
        except ValueError:
          print("enter a number!!")
      else:
        print("Ending the programme RESISTANCES.")
        break#done
def colourcode():#if unwanted input given. it need to ask for the value again
    while True:
        v1 = input("Enter the first color(value 1):").lower()
        if v1 in ["black","brown","red","green","blue","violet","gold","silver","none","stop","orange","grey","white"]:
          if v1 == "black":
            d1 = 0
          elif v1 == "brown":
            d1 = 1
          elif v1 == "red":
            d1 = 2
          elif v1 == "orange":
            d1 = 3
          elif v1 == "yellow":
            d1 = 4
          elif v1 == "green":
            d1 = 5
          elif v1 == "blue":
            d1 = 6
          elif v1 == "violet":
            d1 = 7
          elif v1 == "grey":
            d1 = 8
          elif v1 == "white":
            d1 = 9
          else:
            print("Please enter a valid color.")
            break 
        elif v1 == "stop":
            break
        else:
          print("Enter the color correctly.")
          break
        v2 = input("Enter the second color (value 2):").lower()
        if v2 in ["black","brown","red","green","blue","violet","gold","silver","none","stop","orange","grey","white","yellow"]:
          if v2 == "black":
            d2 = 0
          elif v2 == "brown":
            d2 = 1
          elif v2 == "red":
            d2 = 2
          elif v2 == "orange":
            d2 = 3
          elif v2 == "yellow":
            d2 = 4
          elif v2 == "green":
            d2 = 5
          elif v2 == "blue":
            d2 = 6
          elif v2 == "violet":
            d2 = 7
          elif v2 == "grey":
            d2 = 8
          elif v2 == "white":
            d2 = 9
          elif v2 == "stop":
            break
          else:
              print("Please enter a valid colour.")
              break
        elif v2=="stop":
          break
        else:
          print("Enter the color correctly.")
          break
        m = input("Enter the color multiplier:").lower()
        if m in ["black","brown","red","green","blue","violet","gold","silver","none","stop","orange","grey","white","yellow"]:
            if m == "black":
                d3 = 0
            elif m == "brown":
                d3 = 1
            elif m == "red":
                d3 = 2
            elif m == "orange":
                d3 = 3
            elif m == "yellow":
                d3 = 4
            elif m == "green":
                d3 = 5
            elif m == "blue":
                d3 = 6
            elif m == "violet":
                d3 = 7
            elif m == "grey":
                d3 = 8
            elif m == "white":
                d3 = 9
            elif m == "gold":
                d3 = -1
            elif m == "silver":
                d3 = -2
            elif d3 == "stop":
                break
            else:
                print("Enter a valid color.")
                break
        elif m=="stop":
          break
        else:
          print("Enter the color correctly.")
          break
        t = input("Enter the color of TOLERANCE:").lower()
        if t in ["brown","red","green","blue","violet","gold","silver","none","stop"]:
            if t == "brown":
              d4 = 1
            elif t == "red":
              d4 = 2
            elif t == "green":
              d4 = 0.5
            elif t == "blue":
              d4 = 0.25
            elif t == "violet":
              d4 = 0.1
            elif t == "gold":
              d4 = 5
            elif t == "silver":
                d4 = 10
            elif t == "none":
                d4 = 20
            elif t == "stop":
                break
            else:
                print("Please enter a valid color.")
                break
        elif t=="stop":
          break
        else:
          print("Enter the color correctly.")
          break
        print("The required resistance is", d1, d2, "*10^", d3, ". The TOLERANCE is ±", d4,"Ω.")


def exitfunc():
  print("Thank you :)")
  exit()


print("=== WELCOME TO MATHSOLVER!! ===")
print("----------------------------------------")
print("**INSTRUCTIONS**")
print("-------------------")
print("1.you can exit the whole programme by typing 11")
print("2.you can stop the particular operation by typing stop")
print("-----------------------------------------")
print("HERE'S WHAT WE OFFER: ")
print('''
   S.n0 - function
     1 : areas
     2 : roots of quadratic equations
     3 : derivatives
     4 : logarithemic values
     5 : graphs 
     6 : permutations and combinations
     7 : decimal to fraction converter
     8 : degrees to radians converter
     9 : resistances
    10 : colour code for resistors
    11 : exit''')
while True:
  function = int(input("Enter the s.no of the operation you want to perform:"))
  if function in [1,2,3,4,5,6,7,8,9,10,11]:
    funcdict = {
        1: areas,
        2: rootsofquad,
        3: derivatives,
        4: log,
        5: graphs,
        6: pnc,
        7: dtof,
        8: dtor,
        9: snpr,
        10: colourcode,
        11: exitfunc }
    funcdict.get(function)()
  else:
    print("Enter the s.no correctly!!")