import sqlite3

def db_connect(dbname='rpg_db.sqlite3'):
    return sqlite3.connect(dbname)

def execute_query(cursor,query):
    cursor.execute(query)
    return cursor.fetchall()

# Part 1 
# Get total Character Count
GET_CHARACTER_COUNT = 'SELECT COUNT(*) FROM charactercreator_character;'

# GET TOTAL CLERIC
GET_TOTAL_C_CLERIC = 'SELECT COUNT(*) FROM charactercreator_cleric'

# GET TOTAL FIGHTER
GET_TOTAL_C_FIGHTER = 'SELECT COUNT(*) FROM charactercreator_fighter'

#GET TOTAL MAGE
GET_TOTAL_C_MAGE = 'SELECT COUNT(*) FROM charactercreator_mage'

# GET TOTAL NECROMANCER
GET_C_NECROMANCER = 'SELECT COUNT(*) FROM charactercreator_necromancer'

#GET TOTAL THIEF
GET_C_THIEF = 'SELECT COUNT(*) FROM charactercreator_thief'

# Get Total Items
GET_TOTAL_ITEMS = 'SELECT COUNT(*) FROM armory_item;'

# Get total weapons
GET_TOTAL_WEAPON = 'SELECT COUNT(*) FROM armory_weapon'

#Get how many items each character 

GET_ITEM_PER_CHARACTER = 'SELECT character_id, character_name,\
                          COUNT(DISTINCT item_id) FROM \
                          (SELECT cc.character_id, cc.name \
                           AS character_name, ai.item_id, ai.name AS item_name \
                           FROM charactercreator_character AS \
                            cc, armory_item AS ai, charactercreator_character_inventory \
                           AS cci WHERE cc.character_id = cci.character_id \
                           AND ai.item_id = cci.item_id) \
                           GROUP BY 1 ORDER BY 2 DESC LIMIT 20;'

#avg items per character
GET_AVG_ITEM_PER_CHARA = 'SELECT AVG(num_item) FROM (SELECT character_id, character_name,\
                          COUNT(DISTINCT item_id) AS num_item FROM \
                          (SELECT cc.character_id, cc.name \
                           AS character_name, ai.item_id, ai.name AS item_name \
                           FROM charactercreator_character \
                           AS cc, armory_item AS ai, charactercreator_character_inventory \
                           AS cci WHERE cc.character_id = cci.character_id \
                           AND ai.item_id = cci.item_id) GROUP BY 1);'

#avg number of weapons
GET_AVG_WEAPON = 'SELECT AVG(num_of_weapon) \
                  FROM (SELECT character_id, character_name, COUNT(DISTINCT item_ptr_id) \
                  AS num_of_weapon FROM \
                (SELECT cc.character_id, cc.name AS character_name, aw.item_ptr_id \
                 FROM charactercreator_character AS cc, armory_weapon \
                 AS aw, charactercreator_character_inventory AS cci \
                 WHERE cc.character_id = cci.character_id AND aw.item_ptr_id = cci.item_id) GROUP BY 1)'

#GET WEAPON PER CHARACTER
GET_WEAPON_PER_CHARACTER = 'SELECT character_id, character_name, \
                            COUNT(DISTINCT item_ptr_id) FROM \
                            (SELECT cc.character_id, cc.name \
                             AS character_name, aw.item_ptr_id \
                             FROM charactercreator_character \
                             AS cc, armory_weapon \
                             AS aw, charactercreator_character_inventory \
                             AS cci WHERE cc.character_id = cci.character_id \
                            AND aw.item_ptr_id = cci.item_id) \
                            GROUP BY 1 ORDER BY 2 DESC LIMIT 20;'

# Get non weapons
GET_NON_WEAPON = 'SELECT COUNT(*) FROM armory_item \
                  WHERE armory_item.item_id NOT IN \
                  (SELECT armory_weapon.item_ptr_id \
                  FROM armory_weapon)'
if __name__ == '__main__':
    conn = db_connect()
    curs = conn.cursor()
    num_of_characters = execute_query(curs,GET_CHARACTER_COUNT)
    print(f"Part 1: \n")
    print(f"Total Number of Characters: {num_of_characters[0][0]}")

    #SPECIFIC CHARACTERS PRINT CODE
    num_of_cleric = execute_query(curs,GET_TOTAL_C_CLERIC)
    num_of_fighter = execute_query(curs,GET_TOTAL_C_FIGHTER)
    numf_of_mage = execute_query(curs,GET_TOTAL_C_MAGE)
    num_of_necromancer = execute_query(curs,GET_C_NECROMANCER)
    num_of_thief = execute_query(curs,GET_C_THIEF)
    print("\nSpecific Subclass amount:\n")
    print(f"Number of Cleric: {num_of_cleric[0][0]}")
    print(f'Number of Fighters: {num_of_fighter[0][0]}')
    print(f"Number of Mage: {numf_of_mage[0][0]}")
    print(f'Number of NecroMancer: {num_of_necromancer[0][0]}')
    print(f'Number of thiefs {num_of_thief[0][0]}\n')
    print(f'ITEMS:\n')

    num_of_items = execute_query(curs,GET_TOTAL_ITEMS)
    print(f'Total Number of items: {num_of_items[0][0]}')
    total_weapons = execute_query(curs,GET_TOTAL_WEAPON)
    print(f'Total items that are weapon: {total_weapons[0][0]}')
    total_non_weapon = execute_query(curs,GET_NON_WEAPON)
    print(f'Total items that are NOT weapon: {total_non_weapon[0][0]}')
    print(f'\nItems per character (First 20)\n')

    item_per_char = execute_query(curs,GET_ITEM_PER_CHARACTER)
    for i, item in enumerate(item_per_char):
        print(f'{item_per_char[i][1]}: {item_per_char[i][2]}')
    weapon_per_char = execute_query(curs,GET_WEAPON_PER_CHARACTER)
    print("\nWeapons Per Character(First 20): \n")
    for i, weapon in enumerate(weapon_per_char):
        print(f'{weapon_per_char[i][1]}: {weapon_per_char[i][2]}')
    avg_weapon = execute_query(curs,GET_AVG_WEAPON)
    print(f'\nAverage Weapon: {avg_weapon[0][0]}')
    avg_item = execute_query(curs,GET_AVG_ITEM_PER_CHARA)
    print(f'Average Item: {avg_item[0][0]}\n')