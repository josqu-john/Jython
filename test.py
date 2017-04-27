import sys
sys.path.append('lib')

import game_info
import difficulty_sys
import config
import world_sys
import world

world_sys.create_world(1, config.world_name, config.world_length_x, config.world_length_y, config.average_fertility, config.randomnes)

world.idc[1].new_char(1, 'Leonidas', 'male', 38)
world.idc[1].new_char(2, 'Atehna', 'male', 18)
world.idc[1].new_char(3, 'Alexandar', 'male', 23)

world.idc[1].create_faction(1, 'Sparta', 1)
world.idc[1].create_faction(2, 'Athen', 2)
world.idc[1].create_faction(3, 'Mazedonien', 3)

world.idc[1].factions[1].create_city_on_faction(1, 'Bonn', 1, 1, True)
world.idc[1].factions[2].create_city_on_faction(1, 'New-Books', 2, 2, True)
world.idc[1].factions[3].create_city_on_faction(1, 'Colone', 2, 3, True)
#print world.idc[1].factions[1].citys[1].pop
world.idc[1].world_calc_next_round(3)
