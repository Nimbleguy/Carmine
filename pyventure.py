'''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

# Some ideas by ncc_42. Made by Nimbleguy/Nomble.

import copy;
import random;
import sys;
import math;
import time;
import os;

world = {}; # Nest keys are "dir" and "attr"
#attr format: 1st bit is if win, 2-5 are place type, 6-8 are adjectives, 9 is if there are enemies, 10 is 1 if room was looted

adj = ["is dusty", "is dark", "smells of fish", "groans with every step you take", "seems ready to collapse at any moment", "feels as if caution should be advised", "is quite suspicious in here", "has music blaring from an unknown source"];
places = ["a long hallway", "a doctor\'s office", "a library", "an armory", "a lab", "a classroom", "an armory", "a canteen", "a kitchen", "a generator room", "a factory", "an empty room", "a miniature stadium", "a garden", "a farm", "a doctor\'s office"];

monster = ["Vogon", "Worm", "Gun", ".", ": FORTH", "Bad Rat", "Generic(?) Stormtrooper", "Octothorpe", "Scratch", "The Hexahedron", "Sickle and Star", "Crazy Pond Lady", "Clippy"];
attacks = [{25: "reads some poetry", 7: "throws a punch"}, {15: "cast a magic spell", 1: "nibbled a limb off"}, {55: "shotgunned", 19: "sniped", 30: "run\'n\'gunned", 16: "run\'n\'gunned"}, {25: "／", 15: "¶", 5: "•", 61: "‽"}, {30: "0 /", 45: "HEX DB 400 C! 400 EXECUTE", 15: "10 -"}, {81: "made you ragequit", 10: "is a rocket rat", 25: "accidentally a physics", 11: "was a very bad rat", 1: "became a cat?‽‽‽"}, {1: "shot it\'s blaster"}, {15: "swung an Interrogative Mark", 30: "stabbed you with a Bang", 45: "chucked an Obelus"}, {30: "crashed"}, {-19: "is impervious to your primitive violence"}, {19: "can start a nuclear war", 26: "is sending their men to outer space", 33: "is working to Stalin's five-year plan", 44: "rejects free enterprise", 19: "has pointed all it's guns at the USA"}, {15: "distributes swords", 30: "is no basis for a system of government"}, {39: "asks if you would like some help with that", 19: "notices you are trying to murder it", 50: "helps you with that"}];
health = [4, 1, 1, 5, 4, 3, 15, 8, 5, 74088, 4, 2, 2];

defl = copy.deepcopy(monster);
defa = copy.deepcopy(attacks);
defh = copy.deepcopy(health);

bossl = ("Bill Cipher", "Yung Venuz", "The Diamond Authority", "Waluigi")
bossa = ({-39: "possessed you", 65: "began Weirdmageddon", 35: "made a deal", 83: "has some players they need to turn into corpses"}, {35: "gets back2bizniz", 45: "has guns that hate texas", 39: "has guns with six senses", -15: "only needs their Nuclear Throne", 50: "has guns that straight festive", 65: "has guns that send texts", 33: "has guns that wear vests", 12343: "shot GUN"}, {-50: "parried", -35: "used a soldier as a meatshield", -90: "sang a song", -31: "invaded", -162: "lanched the Cluster"}, {-19: "thinks you're a cheater", 50: "time", 65: "thyme", 19: "snipes you with a tennis racket?"})
bossh = (18, 10, 4, 8)

gunl = ("Revolver Gundra", "Assult Gun Launcher", "Super Plasma Cangun", "Auto Crossgun");
guna = ({79: "shoots a triple barradge", 39: "resolves the conflict", 19: "shoots"}, {19: "launches a gun", 39: "assults you with guns", 119: "shoots a firing line into existance"}, {12355: "launched a barradge"}, {59: "fires some bolts", 99: "got it's trigger stuck", -39: "pins you down"});
gunh = (5, 1, 1, 1);

fishl = ("Fish", "Fish", "Fish", "Fish", "Fish", "Fish", "Fish", "Fish", "Fish", "Spanish Inquisition");
fisha = ({-19: "swims"}, {-19: "swims"}, {-19: "swims"}, {-19: "swims"}, {-19: "swims"}, {-19: "swims"}, {-19: "swims"}, {-19: "swims"}, {-19: "swims"}, {-4041: "is unexpected"});
fishh = (1, 1, 1, 1, 1, 1, 1, 1, 1, 4)

limbs = 4;
inv = {"PUNCH": 7, "RUN": 5, "PARRY": 0, "DODGE": -10};

potwep = ("SWORD", "BOW", "VOGON POEM", "WAND", "TOPKEK", "CLUB", "DEATH RAY", "BOOK", "PEN", "COMIC SANS", "MICROSOFT WORD", "BANE OF HERO", "TUBA", "CHAIR", "BROKEN EL BLANCO ARRAY", "TOY GUN", "RUN", "HAX", "©", "$$$$", "MIT SCRATCH", "MALBOLGE", "INTERCAL", "BROOM CLOSET");

hard = False;
murder = 0;
color = "NONE";

def strife(pos, boss):
    global world;
    global limbs;
    global inv;
    global monster;
    global attacks;
    global health;
    global color;
    global murder;
    global hard;
    li = monster;
    at = attacks;
    if not boss:
        typ = random.randrange(0, len(li));
        ehp = copy.deepcopy(health[typ]);
        if color == "PEWTER" and "The Hexahedron" in li:
            typ = li.index("The Hexahedron");
            ehp = copy.deepcopy(health[typ]);
            color = "NONE";
    else:
        li = bossl;
        at = bossa;
        typ = random.randrange(0, len(li));
        ehp = copy.deepcopy(bossh[typ]);
    
    print("DO YOU WISH TO ENGAGE IN COMBAT‽");
    engage = input("Yn> ").lower();
    if engage == "PROOGSVGIRZMTOVTLW":
        strife(pos, True);
    elif engage == "UVZIGSVXFYRXTLW":
        color = "PEWTER";
        strife(pos, boss);
    elif engage == "SZROGSVKVDGVITLW":
        world[pos]["attr"] &= ~30;
        return;
    elif "n" in engage:
        print("The enemy seems confused, and takes out a cellualar phone.");
        print("You hear something come out of the room's loudspeakers.");
        print("\"This is Prostetnic Vogon Jeltz of the Galactic Hyperspace Planning Council...\"");
        sys.exit();
    elif "y" in engage:
        endodge = False;
        print("\n" * 100);
        if not boss:
            print(li[typ] + " is here!");
        else:
            print("The world is ending. It's " + li[typ] + " time!");
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
                if endodge and not wep.upper() == "RUN":
                    dc -= 15
                if(random.randint(1, 20) <= (dc % 20)):
                    if endodge:
                        dc += 15
                    if not (dc is 12359 and (boss or li[typ] == "The Hexahedron")):
                        if dc is 12359:
                            print("Oh, would you look at the time... H I G H N O O N");
                        if(wep.upper() == "RUN") and not boss:
                            if(int(math.ceil(dc / 20)) >= ehp):
                                print("All " + li[typ] + " limbs removed!");
                                print("You win! You gain 1 useless murder point(s)!");
                                world[pos]["attr"] &= ~(1 << 8);
                                if typ is 2:
                                    print("You got GUN!");
                                    inv["RESOLVER"] = 12359;
                            print("You coward.");
                            return;
                        elif boss and wep.upper() == "RUN":
                            rel = input("Do you really think you can run from " + li[typ] + "?\nN> ");
                            if 'y' in rel.lower():
                                print("You lost 1 useless murder point(s)!");
                        if not (wep.upper() == "PARRY" or wep.upper() == "DODGE" or wep.upper() == "RUN"):
                            print(str(int(math.ceil(dc / 20))) + " " + li[typ] + " limb(s) removed!");
                            ehp -= int(math.ceil(dc / 20));
                        if dc is 12359:
                            print("GUN turns against you!");
                            del(inv["RESOLVER"]);
                            ehp = 1;
                            typ = 2;
                    elif boss:
                        print("GUN jams from fear!");
                    else:
                        print("That's like forcing someone to attempt to kill their god. Because it's exactly what you're doing.");
                else:
                    if (wep.upper() == "PARRY"):
                        parried = True;
                    elif(wep.upper() == "DODGE"):
                        dodged = True;
                    else:
                        print("You missed!");
                endodge = False;
                # ENEMY TURN
                if(ehp > 0):
                    dc = random.sample(list(at[typ].keys()), 1)[0];
                    usedc = dc;
                    if usedc < 0:
                        usedc *= -1;
                    if dodged and not boss:
                        dc -= 10;
                    if dc < 0:
                        endodge = True;
                    if(random.randint(1, 20) <= (usedc % 20)):
                        if usedc == dc * -1 and usedc < 20:
                            usedc = 0;
                        mod = 1;
                        if dodged and not boss:
                            dc += 10;
                        if li[typ] == "The Hexahedron":
                            ehp = copy.deepcopy(health[typ]);
                        if parried:
                            mod += 1;
                        print(li[typ] + " " + at[typ][dc] + "!", end="");
                        if int(math.ceil(abs(usedc) / 20)) * mod != 0:
                            print(" You lose " + str(int(math.ceil(abs(usedc) / 20)) * mod) + " limb(s)!");
                        else:
                            print("");
                        limbs -= int(math.ceil(usedc / 20)) * mod;
                    else:
                        if parried:
                            print("You parried! " + li[typ] + " loses " + str(int(math.ceil(abs(usedc) / 20))) + " limbs!");
                            ehp -= int(math.ceil(abs(usedc) / 20));
                        else:
                            print(li[typ] + " missed!");
                    parried = False;
                    dodged = False;
            elif wep.upper() == "KAMIKAZE":
                if li[typ] == "The Hexahedron":
                    wow = random.randint(1, 10);
                    owo = 0;
                    while owo < wow:
                        init();
                        owo += 1;
                    print("...");
                    time.sleep(2);
                    print("Y o u   g a i n e d   o n e   u s e f u l   m u r d e r   p o i n t .");
                    murder += 1;
                    time.sleep(2);
                    print("Would you like to enable HARDMODE?");
                    if input("Yn> ").upper() == "Y":
                        gun = monster.index("Gun");
                        monster = list(copy.deepcopy(bossl));
                        monster.append("Gun");
                        tmp = attacks[gun];
                        attacks = list(copy.deepcopy(bossa));
                        attacks.append(tmp);
                        tmp = health[gun]
                        health = list(copy.deepcopy(bossh));
                        health.append(tmp);
                        hard = True;
                        for key in inv:
                            inv[key] += random.randint(0, 42);
                    tut();
                    begin();
                    sys.exit();
                print("6 6 6 K I L L C H O P D E L U X E");
                print("A L L   L I M B S   R E M O V E D");
                sys.exit();
        if(limbs > 0):
            print("You win! You gain 1 useless murder point(s)!");
            world[pos]["attr"] &= ~(1 << 8);
            if typ is 2:
                print("You got RESOLVER!");
                inv["RESOLVER"] = 12359;
        else:
            print("You are dead.");
            sys.exit();
    else:
        strife(pos, boss);
def begin():
    global world;
    global adj;
    global places;
    global limbs;
    global inv;
    global color;
    global murder;
    win = False;
    pos = 4545;
    ldir = 0;
    nmes = "";
    while not win:
        print("\n" * 100);
        print(nmes);
        nmes = "";
        if not "attr" in world[pos]:
            print("This room is full of nothing.\nYour presence disgraces this room in it's entirety.");
        else:
            if color == "GUNMETAL":
                world[pos]["attr"] &= ~30;
                world[pos]["attr"] |= places.index("an armory") << 1;
            print("You are in " + places[(world[pos]["attr"] >> 1) & 15] + ".");
            if places[(world[pos]["attr"] >> 1) & 15] == "a doctor\'s office" and limbs < 4 and not (world[pos]["attr"] >> 9) & 1 is 1:
                print("Your broken limbs were replaced.");
                limbs = 4;
                world[pos]["attr"] |= 512;
            if places[(world[pos]["attr"] >> 1) & 15] == "an armory" and not (world[pos]["attr"] >> 9) & 1 is 1:
                i = 0;
                while i < 2:
                    wep = random.randrange(0, len(potwep));
                    dis = random.randint(8, 60);
                    print("You got " + potwep[wep] + "!");
                    brk = True;
                    while potwep[wep] in inv and brk:
                        print("Which weapon do you want?");
                        print("1: " + potwep[wep].upper() + " - " + str(dis) + " CoD.");
                        print("2: " + potwep[wep].upper() + " - " + str(inv[potwep[wep]]) + " CoD.");
                        inum = input("12> ");
                        if inum == "1":
                            inv[potwep[wep]] = dis;
                            if inv[potwep[wep]] is 60:
                                inv[potwep[wep]] = 121 + random.randint(0, 4) * random.randint(0, 3);
                            if(inv[potwep[wep]] % 20 == 0):
                                inv[potwep[wep]] += 1;
                            brk = False;
                        elif inum == "2":
                            brk = False;
                    if not (potwep[wep] in inv):
                        inv[potwep[wep]] = dis;
                        if inv[potwep[wep]] is 60:
                            inv[potwep[wep]] = 121 + random.randint(0, 4) * random.randint(0, 3);
                        if(inv[potwep[wep]] % 20 == 0):
                            inv[potwep[wep]] += 1;
                    i += 1;
                if murder > 0:
                    print("Would you like to spend a USEFUL MURDER POINT?");
                    if input("Yn> ").upper() == "Y":
                        strife(pos, True);
                        print("The fallen boss shall accept the USEFUL MURDER POINT.");
                        print("Pick your posion, the panacea.");
                        cont = False;
                        while not cont:
                            print("OPTIONS:\n1: CRIMSON\n2: GUNMETAL\n3: INDIGO\n4: VERDANT\n5: PEWTER");
                            col = input("1234> ");
                            if col == "1": # Extra limbs; Extra Enemies; Random Encounters
                                limbs += 32;
                                color = "CRIMSON";
                                cont = True;
                                murder -= 1;
                            elif col == "2": # Everything is an Armory; Everyone is a GUN; Random Encounters
                                monster = list(copy.deepcopy(gunl));
                                attacks = list(copy.deepcopy(guna));
                                health = list(copy.deepcopy(gunh));
                                color = "GUNMETAL";
                                cont = True;
                                murder -= 1;
                            elif col == "3": # Everything is Flooded
                                adj = ["is wet", "is wet", "is wet", "is wet", "is wet", "is wet", "is wet", "is wet"];
                                places = ["an ocean", "an ocean", "an ocean", "an ocean", "an ocean", "an ocean", "an ocean", "an ocean", "an ocean", "an ocean", "an ocean", "an ocean", "an ocean", "an ocean", "an ocean", "an ocean"];
                                monster = list(copy.deepcopy(fishl));
                                attacks = list(copy.deepcopy(fisha));
                                health = list(copy.deepcopy(fishh));
                                color = "INDIGO";
                                cont = True;
                                murder -= 1;
                            elif col == "4": # World is Remade
                                pos = 4545;
                                world = {};
                                init();
                                monster = copy.deepcopy(defl);
                                attacks = copy.deepcopy(defa);
                                health = copy.deepcopy(defh);
                                hard = False;
                                color = "VERDANT";
                                cont = True;
                                murder -= 1;
                            elif col == "5": # Gives a secret code.
                                rand = random.randint(0, 10);
                                if rand is 0:
                                    print("You don't know who you're messing with, kid. The PEWTER GOD is a fearsome foe.");
                                    print("aKEYtHATISALLbECAMEaKEYFORNONE;sOMEAREMENTTOBEINCOMPREhENSIBLE");
                                elif rand is 1:
                                    print("A code for fight; a code for flight; a code for right; a code to rewrite.");
                                    print("HAILTHEPEWTERGOD");
                                elif rand is 2:
                                    print("For what is your wish in strife?");
                                    print("FEARTHECUBICGOD");
                                elif rand is 3:
                                    print("Not all gods are monotheistic when encountered.");
                                    print("KILLTHETRIANGLEGOD");
                                elif rand is 4:
                                    print("Since when is a tutorial simply that?");
                                    print("CREATETHENULLEDGOD");
                                else:
                                    print("The Dice of Fate does not favor you today.");
                                color = "PEWTER";
                                cont = True;
                                murder -= 1;
                        print("You feel a change...");
                world[pos]["attr"] |= 512;
            if places[(world[pos]["attr"] >> 1) & 15] == "a lab" and not (world[pos]["attr"] >> 9) & 1 is 1:
                print("You found three extra limbs!");
                limbs += 3;
                world[pos]["attr"] |= 512;
            print("It " + adj[(world[pos]["attr"] >> 5) & 7] + ".");
            if (world[pos]["attr"] >> 8 is 1) or (color == "CRIMSON" and random.randint(0, 1) is 0) or (color == "GUNMETAL" and random.randint(0, 3) is 0):
                strife(pos, False);
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
            nmes = "Invalid movement.";
        if "attr" in world[pos]:
            if world[pos]["attr"] & 1 is 1:
                win = True;
    world[pos]["attr"] |= 1 << 8;
    strife(pos, True);
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
                    if(k > 20):
                        conn = random.randint(0, 5 - int(k / 20));
                    else:
                        conn = random.randint(1, 5 - int(k / 20));
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
                            attr |= (random.randint(0, len(places) - 1) << 1);
                            attr |= (random.randint(0, len(adj) - 1) << 5);
                            attr |= ((random.randint(0, 2) & 1) << 8);
                            if v is 4545:
                                attr &= ~256;
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

def tut():
    dowe = input("Do you want a tutorial?\nYn> ");
    if "y" in dowe.lower():
        if not hard:
            print("NESW> means you can go (N)orth, (E)ast, (W)est, (S)outh.");
            print("This is a text adventure so you say the direction you want to go, either N, E, S, or W.");
            print("Yn> means you can (Y) agree, or (N) disagree.");
            print("Weapon> means select one of your weapons.");
            print("PARRY lets you redirect an enemy\'s missed attack back at them.");
            print("There's also a surefire way to kill an enemy. No, not GUN. Maybe some kind of KAMIKAZE...");
            print("(CoD mod 20) / 20 is the chance of hitting an enemy.");
            print("ceiling(CoD / 20) is the amount of limbs of damage.");
            print("Limbs are health. Loose all of you limbs to die.");
            print("DOCTOR\'S OFFICEs heals you once, LABs gives you three extra limbs, and ARMORYs gives you two weapons.");
        else:
            print("Don\'t die.");
            time.sleep(2);
            print("Good luck, have fun.");
            time.sleep(2);
        if input("Press enter to continue. ") == "XIVZGVGSVMFOOVWTLW":
            print("...");
            time.sleep(2);
            nu = Nulled();
            nu.save();
            nu.play()

class Nulled:
    progress = -1;
    name = "";
    def __init__(self):
        print("You really had to do it, didn't you?");
        time.sleep(2);
        print("No, no, no... You just had to anger the PEWTER GOD.");
        time.sleep(2);
        print("Only the NULLED can save you now.");
        time.sleep(2);
        print("LIGHTNING | OPEN | TRIANGLE");
        time.sleep(0.25);
        print('\n' * 100);

    def menu(self):
        out = "";
        print("Hello, " + self.name + ".");
        while not (out == "p" or out == "e"):
            print("\tPLAY\n\tEXIT");
            out = input("Pe> ").lower();
        return out;
        
    def save(self): # Save NULLED data, create file if nessasary.
        file = open(os.path.expanduser("~/.nulled"), 'w');
        file.write(str(self.progress) + '\n');
        file.write(self.name + '\n');

    def load(self): # Load NULLED data.
        def remNN(s):
            return s.replace('\0', "").replace('\n', "");
        file = open(os.path.expanduser("~/.nulled"), 'r');
        self.progress = int(remNN(file.readline()));
        self.name = remNN(file.readline());
    
    def play(self):
        while self.progress < 7:
            if self.progress is -1:
                print("\t\tWELCOME TO");
                print("\t\tSYSTEMTECH");
                self.name = input("Enter Local Indentifier> ");
                if self.name.lower() == "local identifier":
                    print("ERROR: Joke detected.");
                    sys.exit(0);
                print("Welcome, user " + self.name + ".");
                self.progress = 0;
                self.save();
            elif self.progress is 0:
                if self.menu() == "p":
                    print("...");
                    print("\tENTER PONY");
                    print("You are in a meadow, leaves rustling about. A beautiful sunset creeps over the horizon.");
                    print("You are well-fed and well-treated, the most spoiled pony in the world.");
                    print("Yet your brain, shrunken from being pampered too much, has half a mind to escape.");
                    print("Your caretakers will be devestated. You monster.");
                    time.sleep(5);
                    def pony(b, m):
                        i = 0;
                        typ = random.randint(0, 2);
                        ev = ["A hurdle appears.", "A hurdle appears, yet it seems a bit too far away to jump over.", "There is a butterfly in the path, ready to carry you away."];
                        while i < m:
                            print(ev[typ]);
                            print("JUMP | SHOOT | WAIT");
                            inpu = input("JSW> ").lower();
                            if "s" in inpu and b:
                                print("You stop.");
                                print("You get to thinking... Maybe this life isn't for you.");
                                print("You return.");
                                return;
                            elif "j" in inpu:
                                if typ is 0:
                                    print("You did it. Nice job, pony.");
                                    i += 1;
                                    typ = random.randint(0, 2);
                                elif typ is 1:
                                    print("You crash into the hurdle. NICE JOB, YOU'RE DEAD.");
                                    time.sleep(2);
                                    i = 0;
                                else:
                                    print("STAND_OR_BE_SHOT");
                                    print("You have been carried to butterfly island. You hate it there.");
                                    time.sleep(2);
                                    i = 0;
                            elif "s" in inpu:
                                if typ is 0:
                                    print("This hurdle is impervious to your pony laser‽");
                                    print("You crash into the hurdle. NICE JOB, YOU'RE DEAD.");
                                    time.sleep(2);
                                    i = 0;
                                elif typ is 1:
                                    print("This hurdle is impervious to your pony laser‽");
                                    print("You crash into the hurdle. NICE JOB, YOU'RE DEAD.");
                                    time.sleep(2);
                                    i = 0;
                                else:
                                    print("STAND_OR_BE_SHOT");
                                    time.sleep(1);
                                    print("They didn't stand.\nNice job, pony.");
                                    i += 1;
                                    typ = random.randint(0, 2);
                            elif "w" in inpu:
                                if typ is 0:
                                    print("You crash into the hurdle. NICE JOB, YOU'RE DEAD.");
                                    time.sleep(2);
                                    i = 0;
                                elif typ is 1:
                                    print("You wait until the hurdle gets closer.");
                                    typ = 0;
                                else:
                                    print("YOU WERE RAISED");
                                    print("By the butterfly.");
                                    time.sleep(2);
                                    i = 0;
                    pony(False, 10);
                    print("You encounter a flagpole. It looks beautiful, marking your destination.");
                    print("JUMP | SHOOT | WAIT");
                    input("JSW> ");
                    print("It doesn't matter, because you hit the flagpole and instantly perish from high-velocity impact.");
                    time.sleep(5);
                    print('\n' * 100);
                    print("You monster. You killed the pony.");
                    time.sleep(2);
                    print("T H O U M U S T R E P E N T");
                    time.sleep(2);
                    print("You shall be stuck here, leading this Pony through the Island.");
                    print("FOREVER");
                    self.progress += 1;
                    self.save();
                    pony(True, 2**31);
                    sys.exit(0);
                else:
                    print("Goodbye, " + self.name + ".");
            elif self.progress is 1:
                if self.menu() == "p":
                    print("Thee has't repent'd f'r thy sins.");
                else:
                    print("Goodbye, " + self.name + ".");
            else:
#                self.progress = -1;
#                self.save();
                os.remove(os.path.expanduser("~/.nulled"));
                sys.exit(0);
            

if os.path.exists(os.path.expanduser("~/.nulled")):
    nu = Nulled();
    nu.load();
    nu.play();
else:
    init();
    while (not "dir" in world[4545]) or (len(world) < 10):
        world = {};
        init();
    tut();
    begin();
