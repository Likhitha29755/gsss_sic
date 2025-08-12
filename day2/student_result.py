'''
Accept the average score of the student and print  the result as follows:
0 to 59    Fail
60 to 84   Second class
85 to 95   First class
96 to 100  excellent
also check for invalid score.no negative marking
'''

average_score = int(input('Enter your average score to print the result: '))

if average_score <=59:
    print('result is fail')
elif  average_score <=84:
    print('result is Second class') 
elif average_score <=95:
    print('result is First class') 
elif average_score <=100:
     print('result is Excellent') 
else:
    print('Invalid score')