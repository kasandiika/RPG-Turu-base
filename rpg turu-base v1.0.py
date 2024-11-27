import random
import time

#winrates
games = 0
wins = 0
loses = 0

#stat karakter kita
hero = " "
hp = 0
atk = 0
dfn = 0
crt = 0
spd = 0
mode = 0
status = "-"
mages = " "
catpoint = 0
use_item = 0
#item1 = health potion
#item2 = strength potion
#item3 = crit steroid
item_boost = " "


#stat karakter musuh
en_hero = " "
en_hp = 0
en_atk = 0
en_dfn = 0
en_crt = 0
en_spd = 0
en_mode = 0
en_status = "-"
en = 0

username = ' '
def start() :
    global username
    username = input('masukkan namamu: ')
    print(' ')
    time.sleep(1.5)
    print(f'welcome {username}!')
    time.sleep(2.0)
    menu()
#profile
def profile() :
    global wins
    global loses
    global games
    global username
    global catpoint
    print(f'''
==| PROFILE |==   
username : {username}
catpoints : {catpoint} $
games played : {games}
wins  : {wins}
loses : {loses} 
````````````````
[0] back 
          ''')
    input('pilihan: ')
    time.sleep(1.0)
    print('kembali ke menu...')
    time.sleep(2.0)
    menu()


#bag
h_p = 0
s_p = 0
c_s = 0
def bag() :
    global h_p
    global s_p
    global c_s
    
    if h_p >= 1 :
        item1 = 'health potion'
        jml1 = (f'{h_p}x')
    else :
        item1 = " "
        jml1 = " "
    if s_p >= 1 :
        item2 = 'strength potion'
        jml2 = (f'{s_p}x')
    else :
        item2 = " "
        jml2 = " "
    if c_s >= 1 :
        item3 = 'crit steroid'
        jml3 = (f'{c_s}x')
    else :
        item3 = " "
        jml3 = " "
    
    print(f'''
==| BAG |==         
{jml1} {item1}
{jml2} {item2}
{jml3} {item3}
~~~~~~~~~~~
[0] back
          ''')
    input('pilihan: ')
    time.sleep(1.0)
    print('kembali ke menu...')
    time.sleep(2.0)
    menu()


#loading
def load_battle() :
    time.sleep(1.2)
    print("~")
    time.sleep(0.9)
    print("~~")
    time.sleep(0.7)
    print("~~~")
    time.sleep(2.5)

def load_turn1() :
    time.sleep(0.7)
    print(' ')
    print('== First turn ==')
    time.sleep(1.3)
    
def load_turn2() :
    time.sleep(2.5)
    print(' ')
    print('== Second turn ==')
    time.sleep(1.3)


#shop
def shop() :
    global catpoint
    global h_p
    global s_p
    global c_s
    
    time.sleep(0.5)
    print(f'''
==[ SHOP ]== 
[1] health potion <10 CATPOINTS>
    (menambahkan sejumlah hp, +25 HP)
[2] strength potion <20 CATPOINTS>
    (meningkatkan sejumlah atk, +10 atk)
[3] crit steroid <45 CATPOINTS>
    (meningkatkan persentase crit sebanyak 25%)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
catpoint mu = {catpoint}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
[0] back
          ''')
    p_shop = int(input('pilihan: '))
    
    #katalog shop 1
    if p_shop == 1 :
        item = 'health potion'
        jml = int(input('berapa banyak yang ingin anda beli? '))
        hrg = 10*jml
        print(f'harga total barang: {hrg}')
        
        confirm = input(f'apakah anda ingin membeli {jml}x {item}? (y/n): ')
        if confirm == 'n' :
            time.sleep(0.5)
            print('kembali ke shop...')
            time.sleep(1.5)
            shop()
            
        if catpoint >= hrg :
            time.sleep(1.0)
            h_p += jml
            catpoint -= hrg
            print(f'{item} sebanyak {jml} telah masuk ke dalam tasmu')
            time.sleep(3.0)
            print(' ')
            print('kembali ke shop...')
            time.sleep(1.5)
            shop()
        elif catpoint < hrg :
            time.sleep(3.0)
            print('catpoints mu ga cukup')
            time.sleep(0.5)
            print('kembali ke shop...')
            time.sleep(1.5)
            shop()
    #katalog shop 2
    elif p_shop == 2 :
        item = 'strength potion'
        jml = int(input('berapa banyak yang ingin anda beli? '))
        hrg = 20*jml
        print(f'harga total barang: {hrg}')
        
        confirm = input(f'apakah anda ingin membeli {jml}x {item}? (y/n): ')
        if confirm == 'n' :
            time.sleep(0.5)
            print('kembali ke shop...')
            time.sleep(1.5)
            shop()
            
        if catpoint >= hrg :
            time.sleep(1.0)
            s_p += jml
            catpoint -= hrg
            print(f'{item} sebanyak {jml} telah masuk ke dalam tasmu')
            time.sleep(3.0)
            print(' ')
            print('kembali ke shop...')
            time.sleep(1.5)
            shop()
        elif catpoint < hrg :
            time.sleep(3.0)
            print('catpoints mu ga cukup')
            time.sleep(0.5)
            print('kembali ke shop...')
            time.sleep(1.5)
            shop()
    #katalog shop 3        
    elif p_shop == 3 :
        item = 'crit steroid'
        jml = int(input('berapa banyak yang ingin anda beli? '))
        hrg = 45*jml
        print(f'harga total barang: {hrg}')
        
        confirm = input(f'apakah anda ingin membeli {jml}x {item}? (y/n): ')
        if confirm == 'n' :
            time.sleep(0.5)
            print('kembali ke shop...')
            time.sleep(1.5)
            shop()
            
        if catpoint >= hrg :
            time.sleep(1.0)
            c_s += jml
            catpoint -= hrg
            print(f'{item} sebanyak {jml} telah masuk ke dalam tasmu')
            time.sleep(3.0)
            print(' ')
            print('kembali ke shop...')
            time.sleep(1.5)
            shop()
        elif catpoint < hrg :
            time.sleep(3.0)
            print('catpoints mu ga cukup')
            time.sleep(0.5)
            print('kembali ke shop...')
            time.sleep(1.5)
            shop()
    elif p_shop == 0 :
        time.sleep(1.0)
        print('kembali ke menu...')
        time.sleep(2.0)
        menu()

    
#characters
def assasin() :
    global hero
    global hp
    global atk
    global dfn
    global crt
    global cmb
    global spd
    
    #stat assasin
    hero = "ASSASIN"
    atk = 30
    dfn = 8
    crt = 0.3
    cmb = 0.4
    spd = 20
    
def guard() :
    global hero
    global hp
    global atk
    global dfn
    global crt
    global spd
    
    #stat guard
    atk = 15
    dfn = 20
    crt = 0.25
    spd = 10
    
def mage() :
    global hero
    global hp
    global atk
    global dfn
    global crt
    global spd
    global mode
    global mages
    
    mages = "y"
    #mode1 = fire
    #mode2 = electro
    #mode3 = ice
    
    #stat fire mage
    if mode == 1 :
        hero = "FIRE MAGE"
        atk = 22
        dfn = 5
        spd = 16
    #stat fire mage
    elif mode == 2 :
        hero = "ELECTRO MAGE"
        atk = 33
        dfn = 5
        spd = 90
    #stat fire mage
    elif mode == 3 :
        hero = "ICE MAGE"
        atk = 14
        dfn = 22
        spd = 10
    
def wolf() :
    global en_hero
    global en_hp
    global en_atk
    global en_dfn
    global en_crt
    global en_spd
    global en_mode
    
    #stat wolf
    en_hero = "GREAT WOLF"
    en_atk = 18
    en_dfn = 8
    en_crt = 0.2
    en_spd = 17

def dragon() :
    global en_hero
    global en_hp
    global en_atk
    global en_dfn
    global en_crt
    global en_spd
    global en_mode
    
    #stat dragon
    en_hero = "BABY DRAGON"
    en_atk = 20
    en_dfn = 15
    en_crt = 0.25
    en_spd = 12


#menu
def menu() :
    global games
    global wins
    global loses
    
    if games > 0 and wins > 0 :
        winrates = (wins / games)*100
    else :
        winrates = 0
        
    print(f'''  _________________
**| TURU BASE RPG |**
_____________________
  winrates : {winrates}%                
`````````````````````
[1] GAME START!
[2] BAG
[3] SHOP
[4] PROFILE
          ''')
    p_menu = int(input('pilihan: '))
    
    if p_menu == 1 :
        time.sleep(0.5)
        print(' ')
        print('memulai game...')
        time.sleep(2.0)
        choose_character()
    elif p_menu == 2 :
        time.sleep(0.5)
        print(' ')
        print('membuka bag...')
        time.sleep(2.0)
        bag()
    elif p_menu == 3 :
        time.sleep(0.5)
        print(' ')
        print('membuka shop...')
        time.sleep(2.0)
        shop()
    elif p_menu == 4 :
        time.sleep(0.5)
        print(' ')
        print('membuka profile...')
        time.sleep(2.0)
        profile()
    else :
        time.sleep(0.5)
        print(' ')
        print('input tidak valid!')
        time.sleep(1.5)
        print(' ')
        print('membuka kembali menu...')
        time.sleep(2.5)
        menu()


#persiapan battle
choose = 0
def choose_character() :  
    #reset status
    global status
    global en_status
    global use_item
    global item_boost
    status = '-'
    en_status = '-' 
    use_item = 0
    item_boost = ' '
    
    global choose
    choose = int(input('''
[0] back
~~~~~~~~~~~~~~~~~~~
PILIH KARAKTERMU
[1] Assasin
[2] Guard
[3] Mage

pilihan: '''))  
    time.sleep(0.5)
    if choose == 1 :
        print('Serangan kuat dan sangat cepat, namun pertahanannya lemah')
    elif choose == 2 :
        print('Pertahanan tingkat tinggi dan serangannya cukup kuat, namun lambat')
    elif choose == 3 :
        print('Serangan sihir, memiliki 3 mode: FIRE(dmg, status effect) / ELECTRO(burst dmg, speed) / ICE(debuff)')
    elif choose == 0 :
        time.sleep(1.0)
        print('kembali ke menu...')
        time.sleep(2.0)
        menu()
    else :
        print('gada karakternya banh')
        time.sleep(1.3)
        choose_character()
    
    time.sleep(1.0)
    yon = input("apakah kamu yakin memilih ini? (y/n): ")
    if yon == "y" :
        battle()
    else :
        time.sleep(1.0)
        choose_character() 

slot1 = 0
slot2 = 0
slot3 = 0        
def battle() :
    #import stat karakter kita
    global slot1
    global slot2
    global slot3
    global hero
    global hp
    global atk
    global dfn
    global crt
    global spd
    global mode
    global choose
    global en
    time.sleep(1.0)
    if choose == 1 :
        hp = 90
        assasin()
    elif choose == 2 :
        hp = 200
        hero = "GUARD"
        guard()
    elif choose == 3 :
        hp = 110
        mode = int(input('''
<1> FIRE (serangan sihir yang membakar makhluk hidup dan sekitarnya)
<2> ELECTRO (amarah langit yang menghancurkan bumi, bergerak secepat kilat)
<3> ICE (serangan sihir yang membekukan segalanya, namun waktu merapalnya lebih lama)
                
pilih elemen: '''))
        if mode == 1 or mode == 2 or mode == 3 :
            mage()
        else :
            time.sleep(1.0)
            print('element tidak valid!')
            time.sleep(1.5)
            battle()
    
    #persiapan item yang akan dibawa
    global h_p
    global s_p
    global c_s
    global use_item
    
    #slot1
    if h_p >= 1 :
        slot1 = 1
        item1 = 'health potion'
        jml1 = (f'[1] {h_p}x')
    else :
        slot1 = 0
        item1 = " "
        jml1 = " "
    #slot2
    if s_p >= 1 :
        slot2 = 2
        item2 = 'strength potion'
        jml2 = (f'[2] {s_p}x')
    else :
        slot2 = 0
        item2 = " "
        jml2 = " "
    #slot3
    if c_s >= 1 :
        slot3 = 3
        item3 = 'crit steroid'
        jml3 = (f'[3] {c_s}x')
    else :
        slot3 = 0
        item3 = " "
        jml3 = " "
    
    time.sleep(1.0)    
    #bag
    print(f'''
==| BAG |==         
{jml1} {item1}
{jml2} {item2}
{jml3} {item3}
````````````          ''')
    if h_p == 0 and s_p == 0 and c_s == 0 :
        time.sleep(1.0)
        print('sepertinya anda tidak memiliki item apa apa untuk di bawa ke medan pertarungan')
        time.sleep(1.5)
        print('langsung memulai pertarungan...')
        time.sleep(1.5)
    else :
        item = int(input('pilih item yang anda inginkan: '))
        if slot1 == 1 or slot2 == 2 or slot3 == 3 :
            use_item = item
            if slot1 == 1 and slot2 == 2 and slot3 == 3 :
                if item == 1 :
                    used_item = 'health potion'
                elif item == 2 :
                    used_item = 'strength potion'
                elif item == 3 :
                    used_item = 'crit steroid'
            elif slot1 == 1 and slot2 == 2 :
                if item == 1 :
                    used_item = 'health potion'
                elif item == 2 :
                    used_item = 'strength potion'
                else :
                    time.sleep(1.0)
                    print('item tidak ada di tas')
                    time.sleep(2.5)
                    battle()
            elif slot1 == 1 and slot3 == 3 :
                if item == 1 :
                    used_item = 'health potion'
                elif item == 3 :
                    used_item = 'crit steroid'
                else :
                    time.sleep(1.0)
                    print('item tidak ada di tas')
                    time.sleep(2.5)
                    battle()
            elif slot2 == 2 and slot3 == 3 :
                if item == 2 :
                    used_item = 'strength potion'
                elif item == 3 :
                    used_item = 'crit steroid'
                else :
                    time.sleep(1.0)
                    print('item tidak ada di tas')
                    time.sleep(2.5)
                    battle()
            elif slot1 == 1 :
                if item == 1 :
                    used_item = 'health potion'
                else :
                    time.sleep(1.0)
                    print('item tidak ada di tas')
                    time.sleep(2.5)
                    battle()
            elif slot2 == 2 :
                if item == 2 :
                    used_item = 'strength potion'
                else :
                    time.sleep(1.0)
                    print('item tidak ada di tas')
                    time.sleep(2.5)
                    battle()
            elif slot3 == 3 :
                if item == 3 :
                    used_item = 'crit steroid'
                else :
                    time.sleep(1.0)
                    print('item tidak ada di tas')
                    time.sleep(2.5)
                    battle()
            time.sleep(1.0)
            print(f'membawa {used_item} ke dalam pertarungan')
    
    #munculkan stat karakter musuh
    global en_hero
    global en_hp
    global en_atk
    global en_dfn
    global en_crt
    global en_spd
    global en_mode
    en = int(random.randrange(1,3))
    if en == 1 :
        en_hp = 220
        dragon()
    elif en == 2 :
        en_hp = 170
        wolf()
    
    #mulai battle
    load_battle()
    print(f"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
          
{en_hero} TELAH MENYERANGMU!""")
    battle_start()

#battle dimulai (loop)
move_turn = 0
en_move_turn = 0
def battle_start() : 
    global move_turn
    global en_move_turn
    
    #import stat karakter musuh
    global en_hero
    global en_hp
    global en_atk
    global en_dfn
    global en_crt
    global en_spd
    global en_mode
    global en_status
    
    #import stat karakter kita
    global hero
    global hp
    global atk
    global dfn
    global crt
    global spd
    global mode
    global status
    global choose
    global use_item
    global item_boost
        
    #tampilan battle
    time.sleep(0.8)
    print(' ')
    print(f'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    [[{en_hero}]] 
    HP = {round(en_hp)}  <sts = {en_status}>


[[{hero}]] {item_boost}
 HP = {round(hp)}  <sts = {status}>        
          ''')
    
    #pilihan move
    if choose == 1 :
        #assasin
        time.sleep(1.0)
        print('''__________
PILIH MOVE
[1] slash
    (BASE POWER:30, "melancarkan serangan dengan belati")
[2] stealth
    (CRIT BOOST:20%, "memasuki mode menghilang. meningkatkan crit dan combo rate sebanyak 20%. untuk serangan berikutnya")''')
        if use_item >= 1 :
            if use_item == 1:
                item = 'health potion'
            elif use_item == 2 :
                item = 'strength potion'
            elif use_item == 3 :
                item = 'crit steroid'
            print(f'[3] use item {item}')
        
        print(' ')
        move_turn = int(input('pilih move anda: '))
        
        #speed clash
        if spd > en_spd :
            speed_win()
        else :
            speed_lose()
                
    elif choose == 2 :
        #guard
        time.sleep(1.0)
        print('''__________
PILIH MOVE
[1] slam
    (BASE POWER:40, "melancarkan serangan dengan palu gada")
[2] holy shield
    ("BASE POWER:70, "memasuki mode bertahan. jika terserang, akan melakukan counter atk")''')
        if use_item >= 1 :
            if use_item == 1:
                item = 'health potion'
            elif use_item == 2 :
                item = 'strength potion'
            elif use_item == 3 :
                item = 'crit steroid'
            print(f'[3] use item {item}')
        
        print(' ')
        move_turn = int(input('pilih move anda: '))
        
        #speed clash
        if spd > en_spd :
            speed_win()
        else :
            speed_lose()
            
    elif choose == 3 :
        #mage
        if mode == 1 :
            moves = "Fire Ball"
            modes = "FIRE"
            pwr = 25
            cap = "bola api, musuh yang terkenanya akan terbakar"
        elif mode == 2 :
            moves = "Thunderbolt"
            modes = "ELECTRO"
            pwr = 45
            cap = "guntur dari langit"
        elif mode == 3 :
            moves = "Blizzard"
            modes = "ICE"
            pwr = 10
            cap = "badai salju, membekukan musuh dalam proses dan mengurangi defend mereka"
        time.sleep(1.0)
        print(f'''__________
PILIH MOVE ({modes})
[1] {moves}
    (BASE POWER:{pwr}, "melancarkan {cap}")
[2] Elemental Swap
    ("mengganti elemen mage, menghapus debuff")''')
        if use_item >= 1 :
            if use_item == 1:
                item = 'health potion'
            elif use_item == 2 :
                item = 'strength potion'
            elif use_item == 3 :
                item = 'crit steroid'
            print(f'[3] use item {item}')
        
        print(' ')
        move_turn = int(input('pilih move anda: '))
        
        #speed clash
        if spd > en_spd :
            speed_win()
        else :
            speed_lose()


#speed clash win or lose  
def speed_win() :
    global hero
    global hp
    global atk
    global dfn
    global crt
    global spd
    global status
    global choose
    global no
    global move
    global move_turn
    global use_item
    global item_boost
    global h_p
    global s_p
    global c_s
    global en_hero
    global en_hp
    global en_atk
    global en_dfn
    global en_crt
    global en_spd
    global en_status
    global en_no
    global en_move
    global en_move_turn
    global en
    
    #guard ability
    if hero == 'BULKED GUARD' :
        guard_ability()
    
    #first turn
    load_turn1()
    if choose == 1 :
        if move_turn == 1 :
            assasin_move1()
            assasin()
        elif move_turn == 2 :
            assasin_move2()   
    elif choose == 2 :
        if move_turn == 1 :
            guard_move1()
            guard()
        elif move_turn == 2 :
            guard_move2()
    elif choose == 3 :
        if move_turn == 1 :
            mage_move1()
            mage()
        elif move_turn == 2 :
            mage_move2()
            
    if move_turn == 3 :
        if use_item == 1 :
            item_boost = '<hp+>'
            print('menggunakan health potion!')
            time.sleep(1.0)
            print('menambah 25 hp secara permanen')
            hp += 25
            h_p -= 1
        elif use_item == 2 :
            item_boost = '<atk+>'
            print('menggunakan strength potion!')
            time.sleep(1.0)
            print('menambah 10 atk secara permanen')
            s_p -= 1
        elif use_item == 3 :
            item_boost = '<crit+>'
            print('menggunakan crit steroid!')
            time.sleep(1.0)
            print('menambah 25% peluang crit secara permanen')  
            c_s -= 1
        use_item = 0
        
    if hp <= 0 :
        wol()
    elif en_hp <= 0 :
        wol()
                              
    #second turn
    load_turn2()
    if en == 1 :
        if en_status == "frozen" :
            breaks_ice = random.randrange(1,3)
            if breaks_ice == 1 :
                print(f'{en_hero} menghancurkan es, bebas dari efek frozen')
                if en_dfn < 15 :
                    en_dfn = 15
                time.sleep(0.5)
                en_status = "-"
                dragon()
            else :
                print(f'{en_hero} membeku dan tidak dapat bergerak')
        else :
            en_move_turn = int(random.randrange(1,4))
            if en_move_turn == 1 :
                dragon_move1()
            elif en_move_turn == 2 :
                dragon_move2()
            elif en_move_turn == 3 :
                en_no = 3
                print(f'serangan {en_hero} meleset!')
            dragon()
    if en == 2 :
        if en_status == "frozen" :
            breaks_ice = random.randrange(1,3)
            if breaks_ice == 1 :
                print(f'{en_hero} menghancurkan es, bebas dari efek frozen')
                if en_dfn < 5 :
                    en_dfn = 5
                time.sleep(0.5)
                en_status = "-"
                wolf()
            else :
                print(f'{en_hero} membeku dan tidak dapat bergerak')
        else :
            en_move_turn = int(random.randrange(1,3))
            if en_move_turn == 1 :
                wolf_move1()
            elif en_move_turn == 2 :
                wolf_move2()
            wolf()
            
    if choose == 2 :
        guard()
    
    if hp <= 0 :
        wol()
    elif en_hp <= 0 :
        wol()
    
    #trigger ability guard
    if choose == 2 :
        if hero == 'BULKED GUARD' :
            guard_ability()
        elif hp <= 65 :
            print('guard memasuki mode rage')
            hero = 'BULKED GUARD'
            
    #status effect
    if item_boost == '<atk+>' :
        atk += 10
    elif item_boost == '<crit+>' :
        crt += 0.25
    
    if hp > 0 or en_hp > 0 :
        if status == "burn" :
            time.sleep(2.0)
            print(' ')
            print(f'{hero} terkena dmg karena terbakar (-5)')
            hp -= 5
        if en_status == "burn" :
            time.sleep(2.0)
            print(' ')
            print(f'{en_hero} terkena dmg karena terbakar (-5)')
            en_hp -= 5
            
    #akhiri turn
    wol()
        
def speed_lose() :
    global hero
    global hp
    global atk
    global dfn
    global crt
    global spd
    global status
    global choose
    global no
    global move
    global move_turn
    global use_item
    global item_boost
    global h_p
    global s_p
    global c_s
    global en_hero
    global en_hp
    global en_atk
    global en_dfn
    global en_crt
    global en_spd
    global en_status
    global en_no
    global en_move
    global en_move_turn
    
    #guard ability
    if hero == 'BULKED GUARD' :
        guard_ability()
    
    #first turn
    load_turn1()
    if en == 1 :
        if en_status == "frozen" :
            breaks_ice = random.randrange(1,3)
            if breaks_ice == 1 :
                print(f'{en_hero} menghancurkan es, bebas dari efek frozen')
                if en_dfn < 15 :
                    en_dfn = 15
                time.sleep(0.5)
                en_status = "-"
                dragon()
            else :
                print(f'{en_hero} membeku dan tidak dapat bergerak')
        else :
            en_move_turn = int(random.randrange(1,4))
            if en_move_turn == 1 :
                dragon_move1()
            elif en_move_turn == 2 :
                dragon_move2()
            elif en_move_turn == 3 :
                en_no = 3
                print(f'serangan {en_hero} meleset!')
            dragon()
    if en == 2 :
        if en_status == "frozen" :
            breaks_ice = random.randrange(1,3)
            if breaks_ice == 1 :
                print(f'{en_hero} menghancurkan es, bebas dari efek frozen')
                if en_dfn < 5 :
                    en_dfn = 5
                time.sleep(0.5)
                en_status = "-"
                wolf()
            else :
                print(f'{en_hero} membeku dan tidak dapat bergerak')
        else :
            en_move_turn = int(random.randrange(1,3))
            if en_move_turn == 1 :
                wolf_move1()
            elif en_move_turn == 2 :
                wolf_move2()
            wolf()
    
    if choose == 2 :
        guard()
    
    if hp <= 0 :
        wol()
    elif en_hp <= 0 :
        wol()
    
    #second turn
    load_turn2()
    if choose == 1 :
        if move_turn == 1 :
            assasin_move1()
            assasin()
        elif move_turn == 2 :
            assasin_move2()
    elif choose == 2 :
        if move_turn == 1 :
            guard_move1()
            guard()
        elif move_turn == 2 :
            guard()
            guard_move2()
    elif choose == 3 :
        if move_turn == 1 :
            mage_move1()
            mage()
        elif move_turn == 2 :
            mage_move2()
    
    if move_turn == 3 :
        if use_item == 1 :
            item_boost = '<hp+>'
            print('menggunakan health potion!')
            time.sleep(1.0)
            print('menambah 25 hp secara permanen')
            hp += 25
            h_p -= 1
        elif use_item == 2 :
            item_boost = '<atk+>'
            print('menggunakan strength potion!')
            time.sleep(1.0)
            print('menambah 10 atk secara permanen')
            s_p -= 1
        elif use_item == 3 :
            item_boost = '<crit+>'
            print('menggunakan crit steroid!')
            time.sleep(1.0)
            print('menambah 25% peluang crit secara permanen')
            c_s -= 1
        use_item = 0
    
    #trigger ability guard
    if choose == 2 :
        if hero == 'BULKED GUARD' :
            guard_ability()
        elif hp <= 65 :
            print('guard memasuki mode rage')
            hero = 'BULKED GUARD'
        

    if hp <= 0 :
        wol()
    elif en_hp <= 0 :
        wol()
    
    #status effect
    if item_boost == '<atk+>' :
        atk += 10
    elif item_boost == '<crit+>' :
        crt += 0.25
        
    if hp > 0 or en_hp > 0 :
        if status == "burn" :
            time.sleep(1.5)
            print(f'{hero} terkena dmg karena terbakar (-5)')
            hp -= 5
        if en_status == "burn" :
            time.sleep(1.5)
            print(f'{en_hero} terkena dmg karena terbakar (-5)')
            en_hp -= 5
    
    #akhiri turn
    wol()

    
#deklarasi move
move = " "
en_move = " "
no = 0
en_no = 0

#assasin move
def assasin_move1() :
    global hero
    global en_hp
    global en_dfn
    global atk
    global crt
    global cmb
    global no
    global move
    
    no = 1
    move = "slash"
    print(f'{hero} melancarkan serangan {move}')
    
    time.sleep(1.0)
    #perhitungan dmg
    dmg = atk + atk*0.3
    dmg = dmg - dmg*(en_dfn/100)
    crit_chance = random.random()
    if crit_chance < crt :
        dmg = dmg*1.5
        print(f'serangan crit! (-{round(dmg)})')
    else :
        print(f'serangan kena! (-{round(dmg)})')
    en_hp -= dmg
    
    combo_chance = random.random()
    if combo_chance < cmb :
        time.sleep(2.5)
        print(f'{hero} melancarkan combo atk')
        time.sleep(1.0)
        dmg = atk + atk*0.3
        dmg = dmg - dmg*(en_dfn/100)
        crit_chance = random.random()
        if crit_chance < crt :
            dmg = dmg*1.5
            print(f'combo crit! (-{round(dmg)})')
        else :
            print(f'combo kena! (-{round(dmg)})')
        en_hp -= dmg
def assasin_move2() :
    global hero
    global crt
    global cmb
    global no
    global move
    
    no = 2
    move = "stealth"
    print(f'{hero} memasuki mode {move}')
    time.sleep(1.0)
    if crt >= 1 :
        print('crit rate mu sudah melebihi 100%')
    else :
        print('serangan berikutnya memiliki kemungkinan crit dan combo yang lebih tinggi!')
        
    boost = 0.2
    crt += boost
    cmb += boost

#guard move
def guard_move1() :
    global hero
    global en_hp
    global en_dfn
    global atk
    global dfn
    global crt
    global no
    global move
    
    no = 1
    move = "slam"
    print(f'{hero} melancarkan serangan {move}')
    
    time.sleep(1.0)
    #perhitungan dmg
    dmg = atk + atk*0.4
    dmg = dmg - dmg*(en_dfn/100)
    crit_chance = random.random()
    if crit_chance < crt :
        dmg = dmg*1.5
        print(f'serangan crit! (-{round(dmg)})')
    else :
        print(f'serangan kena! (-{round(dmg)})')
    en_hp -= dmg
def guard_move2() :
    global hero
    global en_hp
    global atk
    global dfn
    global crt
    global no
    global move
    global en_move
    
    no = 2
    move = "holy shield"
    print(f'{hero} melancarkan {move}')
    
    time.sleep(1.0)
    #kalau berhasi counter atk
    if en_no == 1 :
        #perhitungan dmg
        dmg = atk + atk*0.7
        dmg = dmg - dmg*(en_dfn/100)
        crit_chance = random.random()
        if crit_chance < crt :
            dmg = dmg*1.5
            print(f'counter atk dilancarkan crit! (-{round(dmg)})')
        else :
            print(f'counter atk dilancarkan! (-{round(dmg)})')
        en_hp -= dmg
    else :
        print('tidak berhasil counter atk!')
        time.sleep(0.7)
        print('mendapat tambahan (+10) defend untuk 1 ronde')
        dfn += 10
def guard_ability() :
    global hero
    global atk
    global dfn
    global crt
    
    hero = 'BULKED GUARD'
    atk += 10
    dfn += 20
    crt += 0.15
    
#mage move
def mage_move1() :
    global hero
    global hp
    global atk
    global dfn
    global crt
    global spd
    global mode
    global no
    global move
    global en_hero
    global en_status
    global en_hp
    global en_dfn
    
    no = 1
    time.sleep(1.0)
    if mode == 1 :
        move = "Fire Ball"
        print(f'{hero} melancarkan serangan {move}')
        #perhitungan dmg
        dmg = atk + atk*0.25
        dmg = dmg - dmg*(en_dfn/100)
        time.sleep(1.0)
        print(f'serangan kena! (-{round(dmg)})')
        en_hp -= dmg
        time.sleep(1.0)
        if en_status == "frozen" :
            print('tercipta uap panas, musuh bebas dari efek frozen')
            time.sleep(0.5)
            en_status = "-"
            print(f'{en_hero} terkena dmg dari uap panas (-20)')
            en_hp -= 20
        elif en_status == "-" :
            print(f'{en_hero} terbakar')
            en_status = "burn"
        
    elif mode == 2 :
        move = "Thunderbolt"
        print(f'{hero} melancarkan serangan {move}')
        dmg = atk + atk*0.45
        dmg = dmg - dmg*(en_dfn/100)
        time.sleep(1.0)
        print(f'serangan kena! (-{round(dmg)})')
        en_hp -= dmg
        
    elif mode == 3 :
        move = "Blizzard"
        print(f'{hero} melancarkan serangan {move}')
        #perhitungan dmg
        dmg = atk + atk*0.1
        dmg = dmg - dmg*(en_dfn/100)
        time.sleep(1.0)
        print(f'serangan kena! (-{round(dmg)})')
        en_hp -= dmg
        time.sleep(1.0)
        if en_status == "frozen" :
            print(f'{en_status} sudah membeku')
            time.sleep(0.5)
            print('defend musuh berkurang karena kedinginan')
        elif en_status == "burn" :
            print(f'tercipta uap panas, status burn {en_hero} dihapus')
            time.sleep(0.5)
            en_status = "-"
            print(f'{en_hero} terkena dmg dari uap panas (-14)')
            en_hp -= 14
        elif en_status == "-" :
            print(f'{en_hero} membeku')
            en_status = "frozen"
            time.sleep(0.5)
            print('defend musuh berkurang karena kedinginan')
            en_dfn -= 5
def mage_move2() :
    global en_hero
    global en_hp
    global en_status
    global hero
    global mode
    
    print('MAGE mengganti elemennya! efek debuff terhapus')
    time.sleep(1.0)
    transform = int(input('''<1> FIRE (serangan sihir yang membakar makhluk hidup dan sekitarnya)
<2> ELECTRO (amarah langit yang menghancurkan bumi, bergerak secepat kilat)
<3> ICE (serangan sihir yang membekukan segalanya, namun waktu merapalnya lebih lama)                   
    
pilih elemen: '''))
    print(' ')
    time.sleep(1.0)
    #mode fire
    if transform == 1 :
        if mode == 1 :
            print('pilih elemen lain!')
            time.sleep(1.0)
            mage_move2()
        else :
            mode = 1
            mage()
            print('api yang panas meledak dari dalam dirimu')
            time.sleep(1.5)
            print(f'{en_hero} terkena apinya! (-5)')
            en_hp -= 5
            time.sleep(1.5)
            if en_status == "frozen" :
                print('tercipta uap panas, musuh bebas dari efek frozen')
                time.sleep(1.0)
                en_status = "-"
                print(f'{en_hero} terkena dmg dari uap panas (-20)')
                en_hp -= 20
            elif en_status == "-" :
                print(f'{en_hero} terbakar')
                en_status = "burn"
    #mode electro
    if transform == 2 :
        if mode == 2 :
            print('pilih elemen lain!')
            time.sleep(1.0)
            mage_move2()
        else :
            mode = 2
            mage()
            print('amarah langit menyertai dirimu')
            time.sleep(1.5)
            print(f'{hero} mendapat tambahan speed!')
    #mode ice
    elif transform == 3 :
        if mode == 3 :
            print('pilih elemen lain!')
            time.sleep(1.0)
            mage_move2()
        else :
            mode = 3
            mage()
            print('armor es menyelimuti dirimu')
            time.sleep(1.5)
            print(f'{hero} mendapat tambahan defend!')
        
#wolf move
def wolf_move1() :
    global en_hero
    global en_no
    global en_move
    global en_atk
    global hp
    global dfn
    
    en_no = 1
    en_move_choose = random.randrange(1,3)
    if en_move_choose == 1 :
        en_move = "bite"
    if en_move_choose == 2 :
        en_move = "claw slash"
    print(f'{en_hero} menyerang dengan {en_move}')
    
    time.sleep(1.0)
    #perhitungan dmg
    en_dmg = en_atk + en_atk*0.2
    en_dmg = en_dmg - en_dmg*(dfn/100)
    crit_chance = random.random()
    if crit_chance < en_crt :
        en_dmg = en_dmg*1.5
        print(f'serangan crit! (-{round(en_dmg)})')
    else :
        print(f'serangan kena! (-{round(en_dmg)})')
    hp -= en_dmg
def wolf_move2() :
    global en_hero
    global en_no
    global en_move
    global hero
    global atk
    global mages
    
    en_no = 2
    en_move = "intimidation"
    print(f'{en_hero} menggunakan {en_move}')
    
    #perhitungan debuff
    en_debuff = atk*0.3
    time.sleep(1.0)    
    print(f'atk {hero} berkurang sebanyak {round(en_debuff)} poin')
    atk -= en_debuff

#dragon move
def dragon_move1() :
    global en_hero
    global en_no
    global en_move
    global en_atk
    global hero
    global hp
    global dfn
    global status
    
    en_no = 1
    en_move_choose = random.randrange(1,3)
    if en_move_choose == 1 :
        en_move = "tackle"
    if en_move_choose == 2 :
        en_move = "ember"
    print(f'{en_hero} menyerang dengan {en_move}')
    
    time.sleep(1.0)
    #perhitungan dmg
    en_dmg = en_atk + en_atk*0.3
    en_dmg = en_dmg - en_dmg*(dfn/100)
    crit_chance = random.random()
    if crit_chance < en_crt :
        en_dmg = en_dmg*1.5
        print(f'serangan crit! (-{round(en_dmg)})')
    else :
        print(f'serangan kena! (-{round(en_dmg)})')
    hp -= en_dmg
    
    if en_move_choose == 2 :
        if status == '-' :
            status = "burn"
            time.sleep(1.0)
            print(f'{hero} terbakar!')   
def dragon_move2() :
    global en_hero
    global en_no
    global en_move
    global en_atk
    global en_hp
    global dfn
    
    en_no = 2
    en_move = "recovery berry"
    print(f'{en_hero} memakan {en_move}')
    
    time.sleep(1.0)
    recover = random.randrange(10,21)
    print(f'hp {en_hero} bertambah! (+{recover})')
    en_hp += recover
    

ded = ' '
en_ded = ' '
def tampilan_battle():
    global en_hero
    global en_hp
    global en_ded
    global hero
    global hp
    global ded
    
    if en_hp < 0 :
        en_hp = 0
        en_ded = '<(defeated)>'
    if hp < 0 :
        hp = 0
        ded = '<(defeated)>'
    
    print(f'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   [[{en_hero}]] {en_ded}
    HP = {round(en_hp)}


[[{hero}]] {ded}
 HP = {round(hp)}         
          ''')

#deklarasi win or lose
def wol():
    global en_hero
    global en_hp
    global hero
    global hp
    
    
    #kalau menang
    if en_hp <= 0 and hp > 0:
        time.sleep(1.5)
        tampilan_battle()
        time.sleep(3.5)
        print(f'''
{hero} telah mengalahkan {en_hero}
...''')
        time.sleep(1.0)
        win()
            
    #kalau kalah  
    elif hp <= 0 and en_hp > 0:
        time.sleep(1.5)
        tampilan_battle()
        time.sleep(3.5)
        print(f'''
{hero} dikalahkan oleh {en_hero}
...''')
        time.sleep(1.0)
        lose()
            
    #kalau seri
    elif hp <= 0 and en_hp <= 0:
        time.sleep(1.5)
        tampilan_battle()
        time.sleep(3.5)
        print(f'''
{hero} seri melawan {en_hero}
...''')
        lose()
            
    else :
        time.sleep(0.5)
        battle_start()   
def win():
    global catpoint
    global games
    global wins
    games += 1 
    wins += 1
    
    plus_cp = random.randrange(15,26)
    
    time.sleep(0.5)
    print(f"kamu mendapat +{plus_cp} catpoints")
    catpoint += plus_cp
    
    if wins == 5 :
        time.sleep(2.5)
        print('''
    |***[ NEW ACHIEVEMENT! ]***|  
    |       "God Of War"       |
    |    games win reach 5x    |
    ````````````````````````````
              ''')
        time.sleep(3.0)
    
    yor = input("mau ngulang ga? (y/n): ")
    if yor == "y":
        time.sleep(1.0)
        choose_character()
        time.sleep(1.5)
    else :
        time.sleep(1.0)
        print('kembali ke menu...')
        time.sleep(2.5)
        menu()
def lose():
    global games
    global loses
    games += 1 
    loses += 1
    
    if loses == 5 :
        time.sleep(2.5)
        print('''
    |***[ NEW ACHIEVEMENT! ]***|  
    |      "Skill Issues"      |
    |   games lose reach 5x    |
    ````````````````````````````
              ''')
        time.sleep(2.5)
        
    time.sleep(0.5)
    yor = input("mau ngulang ga? (y/n): ")
    if yor == "y":
        choose_character()
        time.sleep(1.5)
    else :
        time.sleep(1.0)
        print('kembali ke menu...')
        time.sleep(2.5)
        menu()


#running program
start()
