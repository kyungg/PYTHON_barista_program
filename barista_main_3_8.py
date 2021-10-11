import sys #sys모듈을 불러옴.
import importlib
import os

if len(sys.argv) >=2: #sys.argv 목록의 항목 개수가 2 이상이면
    _module = importlib. import_module(sys.argv[1], package =None)  
else:
     print("사용법 : python %s _module" %os.path.basename(sys.argv[0]))
     sys.exit(-1)   #sys.exit 함수를 호출하여 프로그램을 종료     
menu = _module.menu
def show_menu() :
    print("\n=<< 메뉴 >>=")
    for item in menu:
        print("%s\t%d" %(item, menu[item]))
    return
def get_order():
    print("무엇을 주문하시겠어요?(q. 종료) ")

    orders = {} #주문 내용을 저장할 빈 사전을 생성하고 orders 변수를 생성하여 가리키도록 함.
    while True:
        order =input(" 어떤 커피를 드시겠습니까? (d. 완료) ")
        if order =="q":
            print("감사합니다 안녕히 가세요~")
            sys.exit(0) #order가 가리키는 값이 q면 프로그램이 종료됨.
        elif order =="d":   #d를 누르면 주문이 완료됨.
            break
        if menu.get(order) == None:
           print("해당 메뉴는 없습니다~")
           continue #continue문을 이용하여 while문의 시작위치로 다시 이동하여 계속해서 주문을 받음.

        howMany =int(input(" 몇 잔을 주문하시겠습니까? "))
        print("%s %d" %(order, howMany))
        orders[order] = howMany
    print("다음과 같이 주문하셨습니다!")
    for order in orders:
       print("%s %d" %(order, orders[order]))   #orders사전의 내용을 출력
       
   # 계산하기
    howMuch =0
    for order in orders:
        howMuch += orders[order]*menu[order]
    print("%d원 입니다~ \n" %howMuch)
    return orders   #orders 사전을 내어주도록 변경

recipe = _module.recipe
def process_order(orders):
    orderToServe = {}
    for order in orders.keys():
        orderCnt = orders[order]
        for curOrder in range(orderCnt):
            func = recipe.get(order)
            orderReady = func() #func 변수가 가리키는 함수를 호출한 후 결과 값을 orderReady 변수로 받음
            if orderToServe.get(orderReady)==None:  #orderReady변수가 가리키는 문자열을 키 값으로 하는 항목이 없다면
                orderToServe[orderReady] =1     #orderReady 1로 초기화. 주문한 커피가 처음orderToServe에 더해질때 수행
            else:
                orderToServe[orderReady]+=1     #주문한 커피가 2번째 이상일때 orderToSave에 더해질 때 수행

    #커피 완성
    print("\n주문하신 커피가 나왔습니다")
    for orderReady in orderToServe.keys():
        print("%s %d잔"%(orderReady, orderToServe[orderReady]))

    return

while True:
    #메뉴보여주기
    show_menu()
    #주문받기
    orders = get_order()
    #주문 처리하기
    process_order(orders)
