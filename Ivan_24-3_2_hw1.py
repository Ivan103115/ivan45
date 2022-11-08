class Hero:
    head=1
    abilyty=True
    def __init__(self,name,nickname,hp,damage):
        self.name=name
        self.nickname=nickname
        self.hp=hp
        self.damage=damage
    def heal(self):
        print(self.hp +100)

    def two_damage(self):
        print(self.damage*2)

    def gritting(self):
        print(f"my name is {self.name}")

    def brand_phrase(self):
        print('good will win')
h1=Hero('optimus','prime',10000,100)
h2=Hero('bakay','bakaevich',1,100)
h3=Hero('org','boss',1000000,57647453)
h4=Hero('optical','suprime',100990,10078)

h1.two_damage()
h2.heal()
h3.gritting()
h4.brand_phrase()























