# Type your code here
n=int(input('please enter an integer between 1 and 9999: '))

# Main program
# Defintion of the dictionary

single_digit = { 0: "zero", 1 : "one", 2 : "two", 3 : "three", 4 : "four", 5 : "five",
 6 : "six", 7 : "seven", 8 : "eight", 9 : "nine"}

double_digit = { 10 : "ten", 11 : "eleven", 12 : "twelve", 13 : "thirteen",
 14 : "fourteen", 15 : "fifteen", 16 : "sixteen"}

tens_digit = { 20 : "twenty", 30 : "thirty", 40 : "forty" , 50 : "fifty" , 60 : "sixty"
70 : "seventy", 80 : "eighty", 90 : "ninety"}

hundreds_digit = { 100 : "hundred", 1000 : "thousand"}


def single_digit_word (number):
    if number >=0 and number <10:
        return single_digit[number]

def double_digit_word (number_1):
    if number_1 >= 10 and number_1 < 20:
        return double_digit[number_1]

    if number_1 >= 20 and number_1 < 100:
        index = number_1 % 10
        index_1 = number_1 // 10
        if index != 0 :
            return tens_digit[index_1] + single_digit[index]
        else :
            return tens_digit[number_1]

def tens_digit_word(number_1):
    if number_1 >=100 and number_1 < 1000:
         index = number_1 % 100
         index_1 = number_1 // 100
         if index != 0 :
            if index < 10:
                return single_digit_word(index_1) + hundreds_digit(0) + single_digit_word(index)
            elif index < 100:
                return single_digit_word(index_1) + hundreds_digit(0) + double_digit_word(index)
            else :
                return single_digit_word(index_1)



# Test the code
