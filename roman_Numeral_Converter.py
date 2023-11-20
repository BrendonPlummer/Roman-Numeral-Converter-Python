#Roman Numeral Converter

romanNum = {
    'C': 100, 
    'L': 50, 
    'X': 10, 
    'V': 5, 
    'I': 1
    }



def convertToRomanNum(toConvert):
    originalValue = toConvert
    convertedValue = ''
    
    
    for value in romanNum.values():
        
        for key, value in romanNum.items():
            while originalValue >= value:
                # if originalValue == 4:
                #     originalValue -= value
                #     convertedValue += 'IV'
                # elif originalValue == 9:
                #     originalValue -= value
                #     convertedValue += 'IX'
                # else:
                originalValue -= value
                convertedValue += key
    print(convertedValue)
    
print("Running converter")
toConvert = input("Please input a number to convert: ")

convertToRomanNum(int(toConvert))