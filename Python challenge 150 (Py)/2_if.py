#%% 12. 두개의 숫자를 입력받아 큰수부터 출력하시오
num1 = int(input('첫번째 숫자를 입력하세요 : '))
num2 = int(input('두번째 숫자를 입력하세요 : '))
if num1 > num2:
    print('%s %s' % (num1, num2))
else:
    print('%s %s' % (num2, num1))

#%% 13. 20보다 작은값을 입력시키고 만약 그렇지 않은경우 경고하기
num1 = int(input('20보다 작은수 하나를 입력하세요 : '))
if num1 < 20:
    print('감사합니다.')
else:
    print('20보다 작은수를 입력해야 되었습니다.')

#%% 14. 10과 20사이의 숫자를 입력, 범위 안일경우 감사, 아니라면 경고하기
num1 = int(input('10~20 사이의 수를 입력하세요 : '))
if num1 >= 10 and num1 <= 20:
    print('Thank you.')
else:
    print('Um...')

# %% 15. 좋아하는 색 입력받기
ans_color = str(input('좋아하는 색을 입력하세요 : '))
if ans_color == 'red' or ans_color == 'RED':
    print('I like red too.')
else:
    print("I don't like that colour, I prefer red.")


#%% 16. 날씨에 대하여 묻고 대답하기
ans_wea = str(input('지금 밖에 비가 오고 있나요? : YES/NO '))
if ans_wea == 'YES':
    ans_win = str(input('밖에 바람이 불고 있나요? : YES/NO'))
    if ans_win == 'YES':
        print("It is too windy for an umbrella.")
    else:
        print("ake an umbrella.")
else:
    print("Engoy your day.")

# %% 17. 사용자의 나이 묻기
ans_age = int(input('How old are you? : '))
if ans_age >= 18:
    print("You can vote.")
elif ans_age == 17:
    print("You can learn to drive.")
else:
    print("You can go Trick-or-Treating.")

# %% 18. 숫자 입력받기
num1 = int(input("Number : "))
if num1 < 10:
    print('Too low.')
elif num1 > 20:
    print("Too high.")
else:
    print("Correct.")

# %% 19. 1 or 2 or 3
num1 = int(input("Enter 1 or 2 or 3 : "))
if num1 == 1:
    print("Thank you.")
elif num1 == 2:
    print("Well done.")
elif num1 == 3:
    print("Correct.")
else:
    print("Error message.")