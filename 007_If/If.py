# if문은 ~하면 ~를 수행한다. 라는 조건문이다.
# 만약 if 조건식: 에서 조건식이 True라면 해당하는 내용을  실행한다.

n = 10

if n < 5:
    print("n은 5보다 작다.")
if 5 < n < 10:
    print("n은 5보다 크고 15보다  작다.")

# 실행할 코드가 한줄이라면 콜론(:) 옆에 실행 내용을 이어써도 된다.
if n < 5: print("n은 5보다 작다.\n")
if 5 < n < 15: print("n은 5보다 크고 15보다 작다.\n")

# elif문을 이용해 여러 조건마다 실행되는 내용을 다르게 할 수 있다.
# elif문은 앞에 있는 if문, else if문의 조건식이 true가 아니고 false일 때 실행된다.
# elif문은 여러개를 붙여 사용할 수 있다.
if n < 5: print("n은 5보다 작다.\n")
elif n < 15: print("n은 5와 같거나 더 크고 15보다 작다.\n")

#else문은 앞에 있는 조건문이 false일 때 실행된다.
else: print("n은 15와 같거나 더 크다")
