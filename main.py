from colored import fg
from requests import get
from os import system

def Menu():   
    system("cls") 
    Api = get('https://bypass.bot.nu/').status_code
    ApiBackup = get('https://vacant-curtly-composure.herokuapp.com/').status_code
    
    print("\n")
    print(f'     {fg(240)}╔═╗ {fg(238)} ╦ ╦ {fg(236)} ╔═╗ {fg(238)} ╔═╗ {fg(240)}╔╦╗   {fg(24)}●{fg(240)} Status :')
    print(f'     {fg(240)}║ ╦ {fg(238)} ╠═╣ {fg(236)} ║ ║ {fg(238)} ╚═╗ {fg(240)} ║    {fg(82 if Api == 200 else 160)}●{fg(240)} Api ~ {Api}')
    print(f'     {fg(240)}╚═╝ {fg(238)} ╩ ╩ {fg(236)} ╚═╝ {fg(238)} ╚═╝ {fg(240)} ╩    {fg(82 if ApiBackup == 200 else 160)}●{fg(240)} Api ~ {ApiBackup} ( Backup )')
    

def Main(URI):
    BypassRequet = get('https://bypass.bot.nu/bypass2?url='+URI)
    if BypassRequet.status_code == 200:
        pass
    else:
        BypassRequet = get('https://vacant-curtly-composure.herokuapp.com/bypass2?url='+URI)
        if BypassRequet.status_code == 200:
            pass
        else:
            print("Sorry, i cant bypass this url")
            exit()

    print(fg(7)+"\n{\n")
    print(fg(7)+"\tTarget : " + BypassRequet.json()["query"])
    print(fg(7)+"\tResponse : " + fg(28) + BypassRequet.json()["destination"])
    print(fg(7)+"\n}\n")

    system('pause')

if __name__ == '__main__':
    while True:
        Menu()
        URI = input(f"\n\n Link To Bypass :"+fg(49))
        Main(URI)