n=int(input('please enter an integer between 1 and 9999: '))

number_list_one = ["","one","two","three","four","five","six","seven","eight","nine"]
number_list_two = ["ten","eleven","twelve","thirteen","fourteen","fifteen","seventeen","eighteen","nineteen"]
number_list_three = ["","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety"]
number_list_four = ["hundred"]

if n < 10:
    convert_to_word = number_list_one[n]
    print(convert_to_word)
elif n >= 10 and n <20:
    n = n - 10
    convert_to_word = number_list_two[n]
    print(convert_to_word)
elif n >=20 and n <100:
    n1 = n % 10
    n2 = ((n -n1)-1) //10
    convert_to_word1 = number_list_one[n1]
    convert_to_word2 = number_list_three[n2]
    print(convert_to_word2,convert_to_word1, sep=" ")
elif n >=100 and <=999:
    n1 = 0
    n2 = n //100
    n3 = 
    n4 = 
    convert_to_word1 = number_list_one[n2]
    convert_to_word2 = number_list_four[n1]
    print(convert_to_word1, convert_to_word2, sep= " ")
