import cmath
import math
from operator import concat

def main():
    print("Welcome to the carpentry calculator ... a work in progress.\n")
    units = selectUnits()
    mainMenu(units)


def mainMenu(units):
    print("    Main Menu")
    print("--------------------")
    print("1 Right Triangle")
    print("2 Right Scalene Triangle")
    print("3 Square\n")

    menuSelection = inputValidation(1,3)
    if menuSelection == 1:
        rightTriangle(units)
    elif menuSelection == 2:
        rightScaleneTriangle(units)

def selectUnits():
    print("    Units")
    print("--------------------")
    print("1 Imperial")
    print("2 Metric\n")
    unitSelection = inputValidation(1,2)
    if unitSelection == 1:
        return "Imperial"
    else:
        return "Metric"

def inputValidation(arg1, arg2):
    while True:
        try:
            validatedInput = int(input("Please enter the number to select the menu item\t"))
        except ValueError:
            print("Invalid Entry")
            continue
        else:
            if validatedInput < arg1 or validatedInput > arg2:
                print("Please enter a number between ", arg1, " and ", arg2, "\t")
                continue
            else:
                return validatedInput

def rightScaleneTriangle(units):
    print("To determine the length of a right scalene triangle's hypotenuse, please enter the base and the base angle:")
        
    if units == "Metric":
        print("Base:\t")
        triangleBase = metricToDecimal() #Side c
        triangleAAngle = int(input("Angle in degrees:\t")) #angle A
        triangleBAngle = 90 
        triangleCAngle = 180 - (triangleAAngle + triangleBAngle)
        sinB = math.sin(math.radians(triangleBAngle))
        sinC = math.sin(math.radians(triangleCAngle))
        hypotenuse = triangleBase * (sinB/sinC) #Side b
        sizeList = decimalToMetric(hypotenuse)
        print("The hypotenuse is: ", int(sizeList[0]), "meters, ", int(sizeList[1]), "centimeters, and ", int(sizeList[2])," millimeters.")
    else:
        print("Base:\t")
        triangleBase = imperialToDecimal() #Side c
        triangleAAngle = int(input("Angle in degrees:\t")) #angle A
        triangleBAngle = 90 
        triangleCAngle = 180 - (triangleAAngle + triangleBAngle)
        hypotenuse = triangleBase * (math.sin(triangleBAngle)/math.sin(triangleCAngle)) #Side b
        sizeList = decimalToImerial(hypotenuse)
        if len(sizeList) == 1:
            print("The hypotenuse is: ", int(sizeList[0]), "feet.")
        elif len(sizeList) == 2:
            print("The hypotenuse is: ", int(sizeList[0]), "feet, ", int(sizeList[1]), "inches.")
        elif len(sizeList) == 3:
            print("The hypotenuse is: ", int(sizeList[0]), "feet, ", int(sizeList[1]), "inches, and ", sizeList[2],".")
        else: print("Program Error")


def rightTriangle(units):
    print("To determine the length of the hypotenuse, please enter the base and altitude:")
    
    if units == "Metric":
        print("Base:\t")
        triangleBase = metricToDecimal()
        print("Altitude:\t")
        triangleAltitude = metricToDecimal()
        hypotenuse = math.sqrt(pow(triangleBase,2) + pow(triangleAltitude,2))
        sizeList = decimalToMetric(hypotenuse)
        print("The hypotenuse is: ", int(sizeList[0]), "meters, ", int(sizeList[1]), "centimeters, and ", int(sizeList[2])," millimeters.")
    else:
        print("Base:\t")
        triangleBase = imperialToDecimal()
        print("Altitude:\t")
        triangleAltitude = imperialToDecimal()
        hypotenuse = math.sqrt(pow(triangleBase,2) + pow(triangleAltitude,2))
        sizeList = decimalToImerial(hypotenuse)
        if len(sizeList) == 1:
            print("The hypotenuse is: ", int(sizeList[0]), "feet.")
        elif len(sizeList) == 2:
            print("The hypotenuse is: ", int(sizeList[0]), "feet, ", int(sizeList[1]), "inches.")
        elif len(sizeList) == 3:
            print("The hypotenuse is: ", int(sizeList[0]), "feet, ", int(sizeList[1]), "inches, and ", sizeList[2],".")
        else: print("Program Error")
def imperialToDecimal():
  while True:
      try:
          feet = int(input("Enter the number of feet:\t"))
          inches = int(input("Enter the number of inches:\t"))
          remainingAmount = input("Enter 1/2 if it is a half inch, 3/4 for three quarters, 3/8 for three eights, 15/16 for sixteenths etc..")
          if remainingAmount == 0:
              break
          else:
              remainingList = remainingAmount.split("/")
              remainingAmount = int(remainingList[0]) / int(remainingList[1])
      except ValueError:
        print("Invalid Entry\n")
        continue
      else:
          decimalMeasurment = float(feet) + float(inches / 12) + (remainingAmount / 12)
          return decimalMeasurment

def metricToDecimal():
    while True:
      try:
          meters = int(input("Enter the number of meters:\t"))
          cm = int(input("Enter the number of centimeters:\t"))
          mm = int(input("Enter the number of millimeters:\t"))
          
      except ValueError:
        print("Invalid Entry\n")
        continue
      else:
          decimalMeasurment = float(meters) + float(cm / 100) + float(mm / 1000)
          return decimalMeasurment

def decimalToImerial(value):   #29.678
    feet = int(value)    #29
    inches, remainder = divmod((value - feet) * 12,1)  #8.136
    sizeList = [feet, inches]
    if remainder == 0.00:
        return sizeList
    else:
        fractionalremainder = int(remainder * 16)
        demoninator = 16
        if fractionalremainder == 0:
            return sizeList
        for index in range(4):
            if fractionalremainder % 2 == 0:
                fractionalremainder /= 2
                demoninator /= 2
                continue
            else:
                sizeList.append(((str(fractionalremainder) + "/" + str(demoninator))))
                break
            
    return sizeList


def decimalToMetric(value):
    sizeList = []
    for i in range(3):
        wholeNumber, fraction = divmod(value,1)
        sizeList.append(wholeNumber)
        value = fraction * 100
    return sizeList

if __name__ == "__main__":
    main()