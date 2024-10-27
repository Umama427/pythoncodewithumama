# this is a function definition to perform the conversion
def temp_converter(temp,convert_to):
    #function body
    if  convert_to == 'F'or'f':
        output_temp = (temp*9/5)+32
    elif convert_to in ['C','c','celcius']:
        output_temp = (temp-32)*5/9
    return output_temp
print("Welcome to my Temperature Converter","\n")
#error handling use try and except
try:
    input_temp = int(input("Enter temperature:"))
    convert_to_main = input("Enter 'F' or 'C' :")
    output_temp_main = temp_converter(input_temp,convert_to_main)
    print(f'{input_temp} in {convert_to_main} is {output_temp_main}')
    print("\n","Thanks for using my temperature converter.")
except:
    print("The application encountered an error, please run again")

###############################


    


        

















# this farenheit to celcius converter
 # this is value of farenheit
#f = 30
# perform the conversion
#c = (f - 32)/1.8 
# print the converted value
#print(f"{f}°F will be {c:.2f}°C in Celcius")

# this farenheit to celcius converter
 # this is value of farenheit
#f = 40
# perform the conversion
#c = (f - 32)/1.8 
# print the converted value
# after point 2 value allowed :.2f
#print(f"{f_main}°F will be {c_main:.2f}°C in Celcius: ")
#function call
#celciusToFarenheit(f_main)

