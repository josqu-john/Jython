import random
import maps
import config
import world

def create_world(idc, name, max_x, max_y, average_fertility, randomnes):
    'World-idc, World-name, max_x, max_y, average_fertility, randomnes'
    world.idc[idc] = World(world.idc, idc, name, max_x, max_y, average_fertility, randomnes)

class World(object):
    def __init__(self, dicto, idc, name, max_x, max_y, average_fertility, randomnes):
        self.IDC = idc
        self.world_round = 0
        self.factions = {}
        self.factions_list = {}
        self.amount_factions = 0
        self.DICTO = dicto
        self.WORLD_NAME = name
        self.MAX_X = max_x
        self.MAX_Y = max_y
        self.CELLS = {}
        self.AMOUNT_CELLS = 0
        self.FINISH_CELL_CREATION = False
        self.chars = {}

        self.AVERAGE_FERTILITY = average_fertility
        self.RANDOMNES = randomnes

        self.world_gen()
    def new_char(self, idc, name, sex, age):
        'char-idc, char-name, sex, age'
        self.chars[idc] = Char(idc, self.IDC, name, sex, age)

    def world_calc_next_round(self, amount):
        'amount round'
        a = 0
        while a != amount:
            a += 1
            self.world_round += 1
            print ""
            print 'Beginn Calc world Round: %d in %d' %(self.world_round, self.IDC)
            print "---------------"
            self.world_all_factions_next_round()
            print "---------------"
            print 'End succesfull Calc Round: %d' %(self.world_round)
            print ""
    def world_gen(self): #Cell creation Process
        wanted_cells = self.MAX_X * self.MAX_Y
        cell_pos_x = 0
        cell_pos_y = 1
        print "============================================="
        print "Cell Creation is starting in world: %d!" % (self.IDC)
        while not self.FINISH_CELL_CREATION:
            if cell_pos_x == self.MAX_X:
                cell_pos_y += 1
                cell_pos_x = 0
            cell_pos_x += 1
            cell_fertility = self.AVERAGE_FERTILITY * 3
            cell_name = '%d/%d' % (cell_pos_x, cell_pos_y)
            self.CELLS[cell_name] = Cell(self.IDC, cell_pos_x, cell_pos_y, cell_fertility)
            self.AMOUNT_CELLS += 1
            print "Succesfull created a Cell. Finish: %d from %d" % (self.AMOUNT_CELLS, wanted_cells)
            if self.AMOUNT_CELLS == wanted_cells:
                self.FINISH_CELL_CREATION = True
                print "Cell Creation is Finish"
                print "============================================="
                print ' '
                print ' '



    def create_faction(self, faction_idc, f_name, leader):
        'faction_idc, f_name, leader-idc'
        print ""
        print "Start Creating faction: %s" % (f_name)
        world_IDC = self.IDC
        self.factions_list[self.amount_factions + 1] = faction_idc
        self.factions[faction_idc] = Faction(world_IDC, faction_idc, f_name, leader)
        self.amount_factions += 1
        print "Ending succesfull Creating faction: %s" % (f_name)
        print ""

    def world_all_factions_next_round(self):#DONT WORK
        b = 0
        while b != self.amount_factions:
            print ""
            b += 1
            self.factions[b].faction_next_round()
            print ""




    #Getter & Setter:
        #Getter:
    def get_world_round(self):
        return self.world_round
    def get_factions(self):
        return self.factions
    def get_amount_factions(self):
        return self.amount_factions
    def get_factions_list(self):
        return self.factions_list
    def get_dicto(self):
        return self.dicto
    def get_WORLD_NAME(self):
        return self.WORLD_NAME
    def get_MAX_X(self):
        return self.MAX_X
    def get_MAX_Y(self):
        return self.MAX_Y
    def get_CELLS(self):
        return self.CELLS
    def get_AMOUNT_CELLS(self):
        return self.AMOUNT_CELLS
    def get_FINIISH_CELL_CREATION(self):
        return self.FINISH_CELL_CREATION
    def get_AVERAGE_FERTILITY(self):
        return self.AVERAGE_FERTILITY
    def get_RANDOMNES(self):
        return self.RANDOMNES
    def set_world_round(self, var):
        self.world_round = var
    def set_factions_list(self, var):
        self.factions_list = var
    def set_factions(self, var):
        self.factions = var
    def set_amount_factions(self, var):
        self.amount_factions = var

    def control_faction(self, which):
        x = self.factions[which]
        return x


class Cell(object):
    def __init__(self, world, pos_x, pos_y, fertility):
        self.WORLD = world
        self.POS_X = pos_x
        self.POS_Y = pos_y
        self.owner = {'faction': 'NOBODY', 'city': 'NOBODY'}
        self.status = 'Empty'
        self.fertility = fertility
        #print self.fertility
    def cell_to_city(self, owner):
        self.owner = owner
        self.status = 'city'
        #maps.dicto['Erde'].factions['Sparta'].citys
        #city = maps.dicto['Erde'].factions['Sparta'].citys['Bonn'] #Dont work!
    #Gesseting:
    def get_world(self):
        return self.WORLD
    def get_pos_x(self):
        return self.POS_X
    def get_pos_y(self):
        return self.POS_Y
    def get_owner(self):
        return self.owner
    def get_fertility(self):
        return self.fertility
    def get_owner(self):
        return self.owner
    def get_status(self):
        return self.status

        #Setter:
    def set_owner(self, var):
        self.owner = var
    def set_fertility(self, var):
        if var != int:
            print "ERROR VAR IS NO INT"
        else:
            self.fertility = var
        self.fertility = var
    def set_owner(self, var):
        self.owner = var
    def set_status(self, var):
        self.status = var

class Faction(object):
    def __init__(self, world_idc, idc, name, leader):
        self.WORLD_IDC = world_idc
        self.IDC = idc
        self.WORLD = world
        self.faction_name = name
        self.leader = leader
        self.city_list = {}
        self.amount_citys = 0
        self.citys = dict()
        self.leader = world.idc[self.WORLD_IDC].chars[leader]

        self.faction_pop = self.get_factions_citys_pop()
        self.faction_wealth = 0

    def create_city_on_faction(self, idc, name, pos_x, pos_y, is_capital):
        'city-idc, city-name, city-pos_x, city-pos_y, is_capital)'
        self.citys[idc] = City(idc, self.IDC, self.WORLD, self.faction_name, name, pos_x, pos_y, is_capital)
        self.city_list[self.amount_citys + 1] = idc
        self.amount_citys += 1

    def faction_next_round(self):

        print "Begin Next Round in faction: %s" % (self.faction_name)
        self.faction_citys_next_round()
        self.faction_wealth = self.faction_wealth + self.get_factions_city_tax()
        self.faction_pop = self.get_factions_citys_pop()
        print 'FACTION STATS:'
        print "Pop: %d" % (self.faction_pop)
        print "Wealth: %d:" % (self.faction_wealth)
        print "Ending succesfull Next Round in faction: %s" % (self.faction_name)


    def faction_citys_next_round(self):
        i = 0
        while i != self.amount_citys:
            i+=1
            self.control_city(i).city_next_round()

    #Gesseting
    def get_factions_citys_pop(self):
        i = 0
        factions_pop = 0
        while i != self.amount_citys:
            i+=1
            factions_pop = factions_pop + self.control_city(i).get_pop()
        return factions_pop

    def get_factions_city_tax(self):
        i = 0
        factions_tax = 0.0
        while i != self.amount_citys:
                i+=1
                factions_tax = factions_tax + self.control_city(i).get_taxes()
        return factions_tax

    def get_WORLD(self):
        return self.WORLD
    def get_faction_name(self):
        return self.faction_name
    def get_leader(self):
        return self.leader
    def get_city_list(self):
        return self.city_list
    def get_amount_citys(self):
        return self.amount_citys
    def get_citys_dic(self):
        return self.citys

    def set_faction_name(self, var):
        self.faction_name = var
    def set_leader(self, var):
        self.leader = var
    def set_city_list(self, var):
        self.city_list = var
    def set_amount_citys(self, var):
        self.amount_citys = var

    def control_city(self, idc):
        x = self.citys[idc]
        return x
class City(object):
    def __init__(self, idc, nation, world, faction, name, pos_x, pos_y, is_capital):
        self.IDC = idc
        self.NATION = nation
        self.WORLD =  world
        self.city_name = name
        self.city_faction = faction
        self.POS_X = pos_x
        self.POS_Y = pos_y
        self.CELL_NAME = None
        self.CELL = None
        self.assigne_cell() # Assigne cell and create cell_name
        self.is_capital = is_capital
        self.pop = config.city_starting_pop
        self.taxes = self.pop / 4
        self.fertility = self.CELL.get_fertility()
        self.grow_rate = self.fertility + self.pop / config.city_grow_div
        self.wealth = 0
    def assigne_cell(self): #Assigne the City a Cell:
        if self.POS_X > world.idc[self.IDC].MAX_X:
            print "ERROR! city %s Cell is over Worlds MAX_X" % (self.city_name)
            exit()
        elif self.POS_Y > world.idc[self.IDC].MAX_Y:
            print "ERROR! city %s Cell is over Worlds MAX_Y" % (self.city_name)
            exit()
        else:
            self.CELL_NAME = '%d/%d' % (self.POS_X, self.POS_Y)
            self.CELL = world.idc[self.IDC].CELLS[self.CELL_NAME]
        if self.CELL.status == 'city':
            print "ERROR! city %s Cell: %s is already used!" % (self.city_name, self.cell_name)
            exit()
        else:
            self.CELL.cell_to_city({'faction': self.city_faction, 'city': self.city_name})
        print 'Succecfull creating & Assigne a City(%s) a Cell(%s)' % (self.city_name, self.CELL_NAME)

    def grow(self):
        self.pop = self.pop + self.grow_rate / config.city_grow_div
    def city_next_round(self):
        self.grow()
        self.wealth += self.taxes / 5
        print "Succesfull next_round City: %s" % (self.city_name)

    #Gesseting:
    def get_taxes(self):
        return self.taxes
    def get_wealth(self):
        return self.wealth
    def get_WORLD(self):
        return self.WORLD
    def get_city_name(self):
        return self.city_name
    def get_city_faction(self):
        return self.city_faction
    def get_POS_X(self):
        return self.POS_X
    def get_POS_Y(self):
        return self.POS_Y
    def get_CELL_NAME(self):
        return self.CELL_NAME
    def get_CELL(self):
        return self.CELL
    def get_is_capital(self):
        return self.is_capital
    def get_pop(self):
        return self.pop
    def get_fertility(self):
        return self.fertility
    def get_grow_rate(self):
        return self.grow_rate
    def set_city_name(self, var):
        self.city_name = var
    def set_is_capital(self, var):
        self.is_capital = var
    def set_pop(self, var):
        self.pop = var
    def set_fertility(self, var):
        self.fertility = var
    def set_grow_rate(self, var):
        self.grow_rate = var
    def set_taxes(self, var):
        self.taxes = var
    def set_wealth(self, var):
        self.wealth = var

'''
class Leader(object):
    def __init__(self, idc_char, world, faction):
        self.WORLD = world
        self.FACTION = faction
        self.idc_char = idc_char
        self.char =  world[self.WORLD].chars[self.idc_char]
        self.name = self.char
        self.sex = self.char
        self.age = self.char
        self.life = self.char

    def give_WORLD(self):
        return self.WORLD
    def give_FACTION(self):
        return self.FACTION
    def give_idc_char(self):
        return self.idc_char
    def give_name(self):
        return self.name
    def give_sex(self):
        return self.sex
    def give_age(self):
        return self.age
    def give_life(self):
        return self.life
'''
class Char(object):
    def __init__(self, idc, world, name, sex, age):
        self.IDC = idc
        self.name = name
        self.WORLD = world
        self.sex = sex
        self.age = age
        self.life = True

    def go_older(self, amount):
        self.age += amount
    def make_leader(self, leader_of):
        self.is_leader = True
        self.leader_of = leader_of
    def die(self):
        self.life = False

    def get_IDC(self):
        return self.IDC
    def get_WORLD(self):
        return self.World
    def get_name(self):
        return self.name
    def get_sex(self):
        return self.sex
    def get_age(self):
        return self.age
    def get_life(self):
        return self.life
    def get_is_leader(self):
        return self.is_leader
    def get_leader_of(self):
        return self.leader_of

    def set_name(self, var):
        self.name = var
    def set_sex(self, var):
        self.sex = var
    def set_age(self, var):
        self.age = var
    def set_life(self, var):
        self.life = var
    def set_is_leader(self, var):
        self.is_leader = var
    def set_leader_of(self, var):
        self.leader_of = var
