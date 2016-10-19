import copy;
import random;
import sys;
import math;

world = {}; # Nest keys are "dir" and "attr"
#attr format: 1st bit is if win, 2-5 are place type, 6-8 are adjectives, 9 is if there are enemies, 10 is 1 if already weaponed/limbed

adj = ["is dusty", "is dark", "smells of fish", "groans with every step you take", "seems ready to collapse at any moment", "feels as if caution should be advised", "is quite suspicious in here", "has music blaring from an unknown source"]
places = ["a long hallway", "a doctor\'s office", "a library", "a mine", "a lab", "a classroom", "an armory", "a canteen", "a kitchen", "a generator room", "a factory", "an empty room", "a miniature stadium", "a garden", "a farm", "a forest"];

monster = ["Vogon", "Worm", "Gun"];
attacks = [{25: "reads some poetry", 7: "throws a punch"}, {15: "cast a magic spell", 1: "nibbled a limb off"}, {59: "pew-pews"}];
health = [4, 1, 1];

limbs = 4;
inv = {"PUNCH": 7, "RUN": 5, "PARRY": 0, "DODGE": -10};

potwep = ["SWORD", "BOW", "VOGON POEM", "WAND", "TOPKEK", "CLUB", "DEATH RAY", "MAKESHIFT EL BLANCO ARRAY", "COMIC SANS", "MICROSOFT WORD", "BANE OF HERO", "TUBA"];

def strife(pos):
    global world;
    global limbs;
    global inv;
    typ = random.randrange(0, len(monster));
    ehp = copy.deepcopy(health[typ]);
    
    print("WOULD YOU LIKE TO ENGAGE IN COMBAT‽");
    if not "y" in input("YN> ").lower():
        print("The enemy seems confused, and takes out a cellualar phone.");
        print("You seem hear something, not knowing the sound's source.");
        print("You hear something come out of the room's loudspeakers.");
        print("\"This is Prostetnic Vogon Jeltz of the Galactic Hyperspace Planning Council...\"");
        sys.exit();
    else:
        print("\n" * 100);
        print(monster[typ] + " is here!");
        while(ehp > 0 and limbs > 0):
            print("Your Weapons:");
            for k, v in inv.items():
                print(k.upper() + " - " + str(v) + " CoD.");
            print("Your Limbs: " + str(limbs));
            print("Enemy Limbs: " + str(ehp));
            wep = input("Weapon> ");
            if wep.upper() in inv.keys():
                dodged = False;
                parried = False;
                dc = inv[wep.upper()];
                if(random.randint(1, 20) <= (dc % 20)):
                    if dc is 12379:
                        print("Oh, would you look at the time...");
                    if(wep.upper() == "RUN"):
                        print("Coward.");
                        return;
                    print(str(int(math.ceil(dc / 20))) + " " + monster[typ] + " limb(s) removed!");
                    ehp -= int(math.ceil(dc / 20));
                    if dc is 12379:
                        print("GUN turns against you!");
                        del(inv["BACK2BIZNIZ"]);
                        ehp = 1;
                        typ = 2;
                else:
                    if (wep.upper() == "PARRY"):
                        parried = True;
                    elif(wep.upper() == "DODGE"):
                        dodged = True;
                    else:
                        print("You missed!");
                        
                # ENEMY TURN
                if(ehp > 0):
                    dc = random.sample(list(attacks[typ].keys()), 1)[0];
                    if dodged:
                        dc -= 10;
                        dodged = False;
                    if(random.randint(1, 20) <= (dc % 20)):
                        print(monster[typ] + " " + attacks[typ][dc] + "! You lose " + str(int(math.ceil(dc / 20))) + " limb(s)!");
                        limbs -= int(math.ceil(dc / 20));
                    else:
                        if parried:
                            print("You parried! " + monster[typ] + " looses " + str(int(math.ceil(dc / 20))) + " limbs!");
                            ehp -= int(math.ceil(dc / 20));
                        else:
                            print(monster[typ] + " missed!");
                    parried = False;
        if(limbs > 0):
            print("You win! You gain 1 useless murder point(s)!");
            world[pos]["attr"] |= 256;
            if typ is 2:
                print("You got GUN!");
                inv["BACK2BIZNIZ"] = 12379;
        else:
            print("You are dead.");
            sys.exit();
def begin():
    global world;
    global adj;
    global places;
    global limbs;
    win = False;
    pos = 4545;
    ldir = 0;
    while not win:
        print("\n" * 100);
        if not "attr" in world[pos]:
            print("You seem to have encountered a dead end.");
        else:
            print("You are in " + places[(world[pos]["attr"] >> 1) & 15] + ".");
            if (world[pos]["attr"] >> 1) & 15 is 1 and (limbs < 7):
                print("Your broken limbs were replaced.");
                limbs = 7;
            if (world[pos]["attr"] >> 1) & 15 is 6 and not (world[pos]["attr"] >> 9) & 1 is 1:
                wep = random.randrange(0, len(potwep));
                print("You got " + potwep[wep] + "!");
                inv[potwep[wep]] = random.randint(1, 29);
                world[pos]["attr"] |= 512;
            if (world[pos]["attr"] >> 1) & 15 is 4 and not (world[pos]["attr"] >> 9) & 1 is 1:
                print("You found an extra limb!");
                limbs+=1;
                world[pos]["attr"] |= 512;
            print("It " + adj[(world[pos]["attr"] >> 5) & 7] + ".");
            if world[pos]["attr"] >> 8 is 1:
                strife(pos);
        if not "dir" in world[pos]:
            adir = ldir;
        else:
            adir = world[pos]["dir"];
        s = "";
        if adir & 1 is 1:
            s += "N";
        if adir & 2 is 2:
            s += "E";
        if adir & 4 is 4:
            s += "S";
        if adir & 8 is 8:
            s += "W";
        d = input(s + "> ").lower();
        if d == "n" and adir & 1 is 1:
            ldir = 1;
            pos += 1;
        elif d == "e" and adir & 2 is 2:
            ldir = 2;
            pos += 100;
        elif d == "s" and adir & 4 is 4:
            ldir = 4;
            pos -= 1;
        elif d == "w" and adir & 8 is 8:
            ldir = 8;
            pos -= 100;
        else:
            print("Invalid movement.");
        if "attr" in world[pos]:
            if world[pos]["attr"] & 1 is 1:
                win = True;
    print("You have successfully escaped!");
    sys.exit();

def init():
    global world;
    global adj;
    global places;
    genleft = {0: [4545]}; # First two digits are x, second two are y
    dirtodo = {};
    stuff = 1;
    while stuff > 0:
        stuff = 0;
        temp = copy.deepcopy(genleft);
        for k, va in temp.items():
            if not k + 1 in genleft:
                genleft[k + 1] = [];
            if not va:
                del(genleft[k]);
            for v in va:
                if v not in world:
                    stuff += 1;
                    world[v] = {};
                    conn = random.randint(0, 5 - int(k / 20));
                    if random.randint(0, 1) is 1 and ((k % 4) + 1 > conn):
                        conn = (k % 4) + 1;
                    pgen = [0];
                    for i in range(conn):
                        if(i != 0):
                            direc = 0;
                            while direc in pgen:
                                direc = random.randint(1, 4);
                            pgen.append(direc);
                            adir = 0;
                            if(direc == 1): # North
                                genleft[k + 1].append(v + 1);
                                if v + 1 in dirtodo:
                                    dirtodo[v + 1] |= 4;
                                else:
                                    dirtodo[v + 1] = 4;
                                adir |= 1;
                            elif(direc == 2): # East
                                genleft[k + 1].append(v + 100);
                                if v + 100 in dirtodo:
                                    dirtodo[v + 100] |= 8;
                                else:
                                    dirtodo[v + 100] = 8;
                                adir |= 2;
                            elif(direc == 3): # South
                                genleft[k + 1].append(v - 1);
                                if v - 1 in dirtodo:
                                    dirtodo[v - 1] |= 1;
                                else:
                                    dirtodo[v - 1] = 1;
                                adir |= 4;
                            elif(direc == 4): # West
                                genleft[k + 1].append(v - 100);
                                if v - 100 in dirtodo:
                                    dirtodo[v - 100] |= 2;
                                else:
                                    dirtodo[v - 100] = 2;
                                adir |= 8;
                            if not "dir" in world[v]:
                                world[v]["dir"] = adir;
                            else:
                                world[v]["dir"] |= adir;
                            attr = 0;
                            attr |= (random.randint(0, len(places)) << 1);
                            attr |= (random.randint(0, len(adj)) << 5);
                            attr |= ((random.randint(0, 2) & 1) << 8);
                            if v is 4545:
                                attr &= 4294967039;
                            if "attr" in world[v]:
                                world[v]["attr"] |= attr;
                            else:
                                world[v]["attr"] = attr;
                genleft[k].remove(v);
    wkey = random.sample(list(world.keys()), 1);
    if "attr" in world[wkey[0]]:
        world[wkey[0]]["attr"] |= 1;
    else:
        world[wkey[0]]["attr"] = 1;

    for k, va in world.items():
        if k in dirtodo:
            if not "dir" in va:
                va["dir"] = dirtodo[k];
                del(dirtodo[k]);
            else:
                va["dir"] |= dirtodo[k];
                del(dirtodo[k]);

init();
while not "dir" in world[4545]:
    world = {};
    init();
begin();
