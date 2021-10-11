menu={
    "Americano":1500,
    "Cafe Latte":2100,
    "Espresso":1600,
}

def make_americano():
    print("아메리카노를 만들고 있습니다")
    return "Americano"
class _Object:  #_Object클래스를 정의.
    def __init__(self,state):
        self.state=state
    def getState(self):
        return self.state
class Coffee(_Object):
    pass
class Milk(_Object):
    pass
class Sugar(_Object):
    pass
class Mug(_Object):
    def setState(self,state):
        self.state=state
class FrothMaker(_Object):
    def setState(self,state):
        self.state=state

def brew(coffee, mug):
    print(" %s를 %s에 넣어 우립니다"
          %(coffee.getState(),mug.getState()))
    mug.setState("우린 커피")
    print(" %s가 준비되었습니다"%mug.getState())
    return
def froth(milk, froth_maker):
    print(" %s를 %s로 거품을 냅니다"
          %(milk.getState(),froth_maker.getState()))
    froth_maker.setState("거품 우유")
    print(" %s가 준비되었습니다"%froth_maker.getState())
    return
def add(mug, froth_maker):
    print(" %s를 %s에 더해줍니다"
          %(froth_maker.getState(),mug.getState()))
    mug.setState("우유 커피")
    print(" %s가 준비되었습니다"%mug.getState())
    return
def stir(mug,sugar):
    print(" %s를 %s으로 저어줍니다"
          %(mug.getState(),sugar.getState()))
    mug.setState("카페라떼")
    print(" %s가 준비되었습니다"%mug.getState())
    return
def make_cafelatte():
    print("카페라떼를 만들고 있습니다")
    coffee=Coffee("커피가루")
    milk=Milk("우유")
    sugar=Sugar("설탕")
    mug=Mug("뜨거운 물이 담긴 머그잔")
    froth_maker=FrothMaker("거품기")
    brew(coffee,mug)
    froth(milk, froth_maker)
    add(mug,froth_maker)
    stir(mug, sugar)
    return "Cafe Latte"
def make_espresso():
    print("에스프레소를 만들고 있습니다~")
    return "Espresso"
recipe={
    "Americano":make_americano,
    "Cafe Latte":make_cafelatte,
    "Espresso":make_espresso
}
    
