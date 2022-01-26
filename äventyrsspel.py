"""importerar modulen random för att kunna slumpa tal"""
import random

"""deklarerar de variabler som innehåller info angående spelaren"""
hp = 175
spelar_str = 10
lvl = 0
vapen_str = 0

"""öppnar listan inventory för att kunna hantera de olika vapen som kan hittas i kistor"""
inventory = []

"""definerar klassen vapen som lagrar datan namn och vapen_str"""
class Vapen:
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength

"""deklarerar de olika vapen som finns"""  
vapen1 = Vapen("Dolk",(random.randint(2,6)))
vapen2 = Vapen("Bila",(random.randint(4,8)))
vapen3 = Vapen("Värja",(random.randint(6,11)))
vapen4 = Vapen("Katana",(random.randint(7,13)))
vapen5 = Vapen("Pistol m/07",(random.randint(6,17)))
vapen6 = Vapen("Gevär m/96",(random.randint(9,19)))
vapen7 = Vapen("Automatkarbin 5",(random.randint(12,22)))
vapen8 = Vapen("Raketgevär",(random.randint(-7,32)))
vapen9 = Vapen("Hagelgevär 686",(random.randint(2,28)))
vapen10 = Vapen("Colt Python",(random.randint(18,21)))
vapen11 = Vapen("Katiusja",(random.randint(4,40)))
"""definerar bossfunktionen som hanterar bossfighter"""
def bossfunktion():
    #deklarerar dessa variabler som globala så att de kan hämta data ifrån andra funktioner och variabler utanför denna
    global hp
    global lvl
    global spelar_st
    global vapen_str

    #slumpar bossens styrka som ett tal mellan 5 och 40
    boss_str = random.randint(1,35)
    print("Du möter en boss")

    #programmet kollar om spelarens styrka kombinerat med vapnets styrka är större än, lika med eller mindre än bossens styrka och agerar utifrån de alternativen
    #du vinner om du har högre styrka, det blir lika om era styrkor är lika och du förlorar om bossens styrka är större än din
    if spelar_str + vapen_str > boss_str:
        print("Du besegrar bossen")
        lvl += 1
        print("Du går upp en level")
        meny()

    elif spelar_str + vapen_str == boss_str:
        print("Du och bossen är lika starka och båda går till reträtt")
        meny()

    elif spelar_str + vapen_str < boss_str:
        print("Bossen besegrar dig")
        hp -= boss_str
        print("Du förlorar",boss_str,"hp")
        meny()

"""deklarerar funktionen fälla, där spelaren hamnar i en fälla och tar en slumpad mängd skada"""
def fällafunktion():
    #gör variabeln hp global så att variabeln konstant är uppdaterad då den kan ändras i andra funktioner också
    global hp
    print("Du hamnar i en fälla")
    skada_fälla = random.randint(1,10)

    hp -= skada_fälla
    print("Du förlorar",skada_fälla,"hp")
    meny()

"""funktionen sköter kistorna som spelaren hittar där spelaren får ett vapen som slumpas fram från alla existerande"""
def kistafunktion():

    print("Du hittar en kista")

    #deklarerar en lista med alla vapen i spelet
    vapenlista = [vapen1,vapen2,vapen3,vapen4,vapen5,vapen6,vapen7,vapen8,vapen9,vapen10,vapen11]

    #tilldelar variabeln x ett värde mellan 0 och 6, vilket motsvarar indexet på listan vapenlista
    x = random.randint(0,8)

    #priset spelaren finner i kistan defineras som en slumpvald indexposition i vapenlista 
    pris = vapenlista[x]

    print("I kistan finns vapnet:",pris.name)

    #vapnet som spelaren finner i kistan läggs till i dennes inventory
    inventory.append(pris)

    #vapnet som spelaren funnit tas bort ur vapenlista för att förhindra att spelaren för flera kopior av samma vapen
    vapenlista.remove(pris)

    #tillkalar menyn för att fortsätta spelet
    meny()

"""funktionen hanterar spelarens inventory och låter denne välja vilket vapen de vill använda, varav endast ett kan användas samtidigt"""
def inventoryfunktion():
    #definerar spelar_str och vapen_str som globala så att variablerna konstant är uppdaterade då dom kan ändras i andra funktioner
    global spelar_str
    global vapen_str
    #programmet kollar om listan är tom och i så fall meddelar spelaren innan den tillkallar menyn så att spelet kan fortsätta
    if len(inventory) <= 0:
        print("Ditt inventory är tomt")
        meny()
    #om listans längd är större än 0, vilket indikerar att det finns föremål i spelarens inventory, printar programmet dessa samt vilken plats de har i index så att spelaren kan välja vilket vapen denne vill använda
    elif len(inventory) > 0:
        print("I ditt inventory finns: ")
        for i in range(len(inventory)):
            vapen = "{i}: {name} | {strength}".format(i = i, name = inventory[i].name, strength = inventory[i].strength)
            print(vapen)

    #definerar variabeln vapen_val som spelarens input och sätter därefter vapen_str som respektive vapens strength bonus
    vapen_val = int(input("Välj vapen med siffror: "))
    if vapen_val < len(inventory):
        vapen_str = inventory[vapen_val].strength
    #om en indexplats som valts är tom informeras spelaren och ombeddes välja igen
    else:
        print("Denna plats i ditt inventory är tom, välj en annan")
        inventoryfunktion()

    meny() 

"""funktionen låter spelaren välja dörr"""
def dörrvalfunktion():
    accepterade_inputs = [1,2,3]
    slump = random.randint(-2,3)
    #definerar variabeln dörrval som spelarens input, detta görs dock bara för att ge illusionen av ett val
    dörrval = int(input("Välj dörr, 1-3: "))
    if dörrval not in accepterade_inputs:
      print("Du har gjort ett ogiltigt val, försök igen!")
      dörrvalfunktion()
    else:
      if dörrval - slump > 0:
        bossfunktion()
      elif dörrval - slump < 0:
        fällafunktion()
      elif dörrval - slump == 0:
        kistafunktion()
    #om ett val annat än 1-3 väljs anropas funktionen igen så att spelaren kan skriva in ett giltigt dörrval
  
      
    
      
      

"""funktionen visar spelaren dennes hp, styrka, totala styrka (spelar_str + vapen_str) samt dennes level"""
def spelarinfofunktion():
    #definerar vapen_str som global så att variabeln konstant är uppdaterad då den kan ändras i andra funktioner
    global vapen_str
    print("HP: ",hp,"/ 100")
    print("STR: ",spelar_str)
    print("TOTAL STR: ",spelar_str + vapen_str)
    print("LVL: ",lvl,"/ 10")
    #spelaren måste välja att gå tillbaka med e så att de ska kunna titta på spelarinformationen så länge de vill
    spelarval = input("[e] Gå tillbaka: ").lower()
    if spelarval == "e":
        meny()
    else:
        spelarinfofunktion()

"""funktionen agerar som meny och låter spelaren navigera genom de olika funktionerna"""
def meny():
    #definerar hp som global så att variabeln konstant är uppdaterad då den kan ändras i andra funktioner
    global hp
    #hp kontrolleras hela tiden i menyn då alla funktioner anropar menyn efter de är klara, om hp understiger eller är lika med 0 avslutas programmet
    if hp < 0:
        print("Du dör, programmet avslutas")
    #level kontrolleras hela tiden i menyn då alla funktioner anropar menyn efter de är klara, om level överstiger eller är lika med 0 avslutas programmet
    elif lvl >= 10:
        print("Gattis, du når level 10 och har således vunnit över") 
        print("Samtliga bossar, och överlevde mot alla odds")
    else:
        #spelaren ges 3 olika val där de kan se spelarinfo som t.ex hp, se vad som finns i deras inventory samt ändra vilket vapen som används. Spelaren kan också välja att gå till dörrvalsfunktion för att faktiskt spela
        print("[v] Välj dörr")
        print("[i] Visa inventory")
        print("[s] Visa spelarinfo")
        #menyval är .lower() för att bokstavsstorlek inte ska spela någon roll
        menyval = input("Tryck för att visa: ").lower()
        if menyval == "v":
            dörrvalfunktion()

        elif menyval == "i":
            inventoryfunktion()

        elif menyval == "s":
            spelarinfofunktion()

        else:
            print("Ogiltigt alternativ, försök igen!")
            meny()

print("𝓚𝓐𝓜𝓟𝓔𝓝 𝓞𝓜  𝓓𝓘𝓣𝓣 𝓛𝓘𝓥 ┌( ͝° ͜ʖ͡°)=ε/̵͇̿̿/’̿’̿ ̿")
print("Detta spel går ut på att du har tre enkla val.")
print("När du väljer en av de tre dörrarna så kan en av tre saker inträffa, alla lika sannolika.")
print("I första utfallet kan du träffa en boss i varierande styrka, här gäller det att dö eller döda.")
print("I det andra utfallet kan du finna ett vapen, som gör dig starkare gentemot de bossar som onekligen kommer komma i din väg")
print("I det tredje utfallet kan du råka ut för en fälla, ingen lämnar en fälla oskadd.... någonsin!")
print("Du börjar som smuts, vid ynka level 0. Varje gång du dräper en boss så ökar du till nästa level. Spelet avslutas antingen med din död eller efter att du har nått level 10 och således vunnit spelet. Lycka till.")
meny()
#dörrvalfunktion()
