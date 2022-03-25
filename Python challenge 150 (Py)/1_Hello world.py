# 1.
name = input('사용자의 이름을 입력해 주세요 : ')
print('Hello %s' % name)

# 2.
name_last = input('Last name 을 알려주세요 :')
print('Hello %s %s' % (name, name_last))

# 3.
print(' what do you call a bear with no teeth?' + '\n' + 'A gummy bear!')

# 4.
num_1 = int(input('첫번째 숫자 입력하세요 : '))
num_2 = int(input('두번째 숫자 입력하세요 : '))
num_3 = int(num_1) + int(num_2)
print('The total is %s' % num_3)

# 5.
num_1 = int(input('첫번째 숫자 입력하세요 : '))
num_2 = int(input('두번째 숫자 입력하세요 : '))
num_3 = int(input('두번째 숫자 입력하세요 : '))
print('The answer is %s' % ((num_1+num_2)*num_3))

# 6.
piz_1 = int(input('처음에 가지고 있었던 피자 조각이 몇 조각 인가요? : '))
piz_2 = int(input('몇 조각을 먹었나요? : '))
print('피자가 %s 조각 남아있네요' % (piz_1-piz_2))

# 7.
age = int(input('나이가 몇 살인가요? : '))
print('%s next birthday you will be %s' % (name, age+1))

# %% 8.
peo = int(input('몇명이서 식사를 했나요? : '))
bil = int(input('금액이 얼마나 나왔나요? : '))
print('한사람당 %s 원씩 내면 됩니다.' % (bil/peo))

# %% 9. 날짜수를 입력받아 그 일까지 몇시간 몇분 몇초가 남았는가
days = int(input('날짜를 시간, 분, 초로 바꿔드릴게요 : '))
print('%s 일은 %s 시간이에요.' % (days, days*24))
print('%s 일은 %s 분이에요.' % (days, days*24*60))
print('%s 일은 %s 초에요.' % (days, days*24*60*60))

# %% 10. 킬로그램은 2.204파운드 이다. 몸무게를 킬로그램 단위로 입력받아 파운드로 변환해 출력해라
weight = int(input('몸무게가 몇 키로 인가요? : '))
print('%s 파운드 이군요!' % (weight/2.204))

# %% 11. 100보다 큰수와 10보다 작은수를 하나씩 받아서, 큰수에 작은수가 몇번 들어가는가를 보여줘라.
big_n = int(input('100보다 큰수 하나를 입력하세요 : '))
sma_n = int(input('10 보다 작은수 하나를 입력하세요 : '))
print('%s는 %s안에 %s 번 들어가네요.' % (sma_n, big_n, big_n//sma_n))
# %%
