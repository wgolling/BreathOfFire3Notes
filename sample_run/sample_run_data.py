# Import constants from datatracker module.
from datatracker import *

def track_data(dt):
  # Segement 0: Awakening
  dt.split("Awakening", 0)


  ### START OF USER COMMANDS ###

  # Second Awakening
  dt.pick_up_weapon(MELTED_BLADE) # From Mogu's body
  dt.gain_character(REI)
  dt.gain_character(TEEPO)
  dt.split("Second Awakening", 0)

  # Nu
  dt.pick_up_skill_ink() 
  dt.pick_up_zenny(40)
  dt.pick_up_weapon(BENT_SWORD)
  dt.pick_up_zenny(200)
  dt.pick_up_weapon(BALLOCK_KNIFE)
  dt.level_up(REI)
  dt.level_up(TEEPO, levels=2)
  dt.boss_drop_zenny(50) # Second Nu fight
  dt.split("Nu", 305)

  # Pre-Manor
  dt.buy_weapon(BRONZE_SWORD, 240)
  dt.buy(40) # Wooden Rod
  dt.buy(3 * 10)  # Herbs
  dt.pick_up_weapon(POINTED_STICK)
  dt.level_up(RYU)
  dt.level_up(TEEPO)
  dt.pick_up_weapon(POINTED_STICK)
  dt.level_up(RYU)
  dt.pick_up_zenny(80)
  dt.pick_up_zenny(120)
  dt.pick_up_weapon(SILVER_KNIFE)
  dt.buy_skill_ink()
  dt.split("Pre-Manor", 238)

  # The McNeil Incident
  dt.boss_drop_zenny(10) # Pooch
  dt.level_up(TEEPO)     # Rocky
  dt.level_up(RYU)       # Rocky
  dt.level_up(REI)       # Rocky  
  dt.level_up(RYU)
  dt.pick_up_zenny(120)
  dt.level_up(TEEPO)
  dt.boss_drop_zenny(8)  # Torast
  dt.level_up(RYU)
  dt.pick_up_zenny(40)
  dt.level_up(TEEPO)
  dt.boss_drop_zenny(20) # Kassen
  dt.level_up(RYU)       # Galtel
  dt.boss_drop_zenny(4)  # Galtel
  dt.pick_up_zenny(600)
  dt.boss_drop_zenny(24) # Doksen
  dt.level_up(TEEPO)
  dt.pick_up_weapon(BROAD_SWORD)
  dt.level_up(RYU)
  dt.level_up(RYU)        # Amalgam
  dt.boss_drop_zenny(200) # Amalgam
  dt.split("The McNeil Incident", 1697)

  # Mt. Mynerg
  dt.lose_character(REI)
  dt.lose_character(TEEPO)
  dt.pick_up_zenny(200)
  dt.level_up(RYU)
  dt.split("Mt. Mynerg", 2013)

  # Wyndia
  dt.pick_up_skill_ink()
  dt.gain_character(NINA)
  dt.level_up(RYU)
  dt.split("Wyndia", 2233)

  # Escape
  dt.buy_weapon(MACE, 280)
  dt.buy_weapon(MAGICIAN_ROD, 546)
  dt.buy_weapon(RIPPERS, 420)
  dt.pick_up_zenny(80)
  dt.buy(100) # Rest at Inn in Genmel, next time don't do this
  dt.level_up(NINA)
  dt.pick_up_zenny(400)
  dt.level_up(NINA)
  dt.pick_up_weapon(BENT_SWORD)
  dt.level_up(NINA)
  dt.split("Escape", 1632)

  # Tower
  dt.buy(2 * 20) # Toad and Old Popper from Merchant outside
  dt.gain_character(MOMO)
  dt.pick_up_skill_ink()
  dt.pick_up_weapon(ICE_CHRYSM)
  dt.pick_up_weapon(FIRE_CHRYSM)
  dt.level_up(RYU)
  dt.pick_up_zenny(800)
  dt.pick_up_zenny(40)
  dt.split("Tower", 2841)

  # Coffee Break
  dt.pick_up_weapon(SCRAMASAX)
  dt.pick_up_zenny(80)
  dt.buy(30) # Inn at Plant
  dt.pick_up_zenny(1200)
  dt.level_up(MOMO)
  dt.boss_drop_zenny(300) # Mutant
  dt.gain_character(PECO) # Mutant
  dt.level_up(RYU)       
  dt.level_up(MOMO)
  dt.use_skill_ink()
  dt.split("Coffee Break", 4617)

  # Champion
  dt.pick_up_zenny(40)
  dt.level_up(RYU, levels=5)  # Dodai
  dt.buy(100) # Inn in arena
  dt.boss_drop_zenny(340) # Emitai
  dt.level_up(RYU)        # Thugs
  dt.boss_drop_zenny(350) # Thugs
  dt.gain_character(GARR)
  dt.boss_drop_zenny(500) # Stallion
  dt.pick_up_zenny(400)
  dt.split("Champion", 6147)

  # Fix the Lighthouse
  dt.buy(50) # Float
  dt.use_skill_ink()
  dt.level_up(MOMO)
  dt.level_up(NINA)
  dt.level_up(NINA)
  dt.pick_up_skill_ink()
  dt.level_up(NINA, levels=5) # Gazer
  dt.boss_drop_zenny(1000)    # Gazer
  dt.level_up(NINA)       # Dolphin
  dt.boss_drop_zenny(200) # Dolphin
  dt.use_skill_ink()
  dt.split("Fix the Lighthouse", 9181)

  # Mt. Zublo
  dt.level_up(MOMO)
  dt.pick_up_zenny(800)
  dt.level_up(RYU)
  dt.level_up(RYU)
  dt.level_up(RYU)          # Gisshan
  dt.boss_drop_zenny(1000)  # Gisshan
  dt.split("Mt. Zublo", 13343)

  # The Grind
  dt.buy(12000) # Barbarossa
  dt.use_skill_ink()
  dt.buy(10 * 50 + 20 * 10 + 3 * 200) # 10 Vitamins, 10 Healing Herbs, 3 Ammonia
  dt.level_up(PECO, levels=8)
  dt.level_up(PECO)
  dt.level_up(PECO)
  dt.level_up(PECO)
  dt.level_up(PECO)
  dt.level_up(PECO)
  dt.level_up(PECO)
  dt.level_up(PECO)
  dt.level_up(PECO) # go back to Meryleep
  dt.use_skill_ink()
  dt.level_up(RYU)
  dt.split("The Grind", 4523)

  # Angel Tower
  dt.pick_up_skill_ink()
  dt.level_up(RYU)
  dt.split("Angel Tower", 6624)

  # Third Awakening
  dt.lose_character(NINA)
  dt.lose_character(MOMO)
  dt.lose_character(PECO)
  dt.level_up(GARR)
  dt.boss_drop_zenny(300) # Dragon Zombie
  dt.level_up(GARR)
  dt.pick_up_zenny(3000)
  dt.split("Third Awakening", 11978)

  # Revenge
  dt.buy(4 * 4000) # Manly clothes
  dt.level_up(GARR)
  dt.level_up(RYU)
  dt.pick_up_zenny(800)
  dt.gain_character(NINA)
  dt.boss_drop_zenny(1500) # Mikba
  dt.gain_character(REI)
  dt.level_up(REI, levels=13)
  dt.pick_up_zenny(80)
  dt.split("Revenge", 12773)

  # Plant
  dt.level_up(RYU)
  dt.gain_character(MOMO)
  dt.gain_character(PECO)
  dt.buy(10000) # Emitai
  dt.level_up(MOMO)
  dt.pick_up_skill_ink()
  dt.level_up(MOMO)
  dt.level_up(GARR)
  dt.boss_drop_zenny(300) # Huge Slug
  dt.level_up(MOMO)
  dt.level_up(RYU)        # Shroom
  dt.level_up(GARR)       # Shroom
  dt.boss_drop_zenny(300) # Shroom
  dt.pick_up_zenny(400)
  dt.level_up(MOMO)
  dt.split("Plant", 9795)

  # Free Deis
  dt.level_up(GARR)
  dt.level_up(MOMO)
  dt.boss_drop_zenny(500) #Gaist
  dt.split("Free Deis", 14450)

  # Minigame Hell
  dt.level_up(NINA)       # Angler
  dt.boss_drop_zenny(200) # Angler
  dt.level_up(GARR)
  dt.level_up(RYU)
  dt.split("Minigame Hell", 15015)

  # The Black Ship
  dt.pick_up_skill_ink()
  dt.pick_up_skill_ink()
  dt.pick_up_zenny(2400)
  dt.level_up(NINA)
  dt.level_up(NINA, levels=2) # Ammonites
  dt.level_up(GARR)           # Ammonites
  dt.boss_drop_zenny(1000)    # Ammonites
  dt.split("The Black Ship", 21718)

  # Back Across The Ocean
  dt.buy(10 * 10 + 16 * 4) # 10 Vitamins, 16 Healing Herbs
  dt.buy(8000) # AP Shells
  dt.level_up(RYU)
  dt.level_up(GARR)
  dt.level_up(REI)
  dt.level_up(MOMO)
  dt.pick_up_zenny(4000)
  dt.pick_up_skill_ink()
  dt.level_up(RYU)
  dt.split("Back Across The Ocean", 24870)

  # Elder
  dt.pick_up_skill_ink()
  dt.use_skill_ink()
  dt.level_up(MOMO, levels=12)
  dt.split("Elder", 24870)

  # Factory
  dt.pick_up_skill_ink()
  dt.level_up(NINA)
  dt.split("Factory", 29420)

  # Desert
  dt.level_up(RYU)
  dt.level_up(NINA)
  dt.level_up(NINA)
  dt.level_up(PECO)
  dt.level_up(MOMO)
  dt.level_up(PECO)
  dt.level_up(PECO)
  dt.level_up(RYU)
  dt.level_up(PECO)
  dt.level_up(MOMO)
  dt.level_up(MOMO)
  dt.use_skill_ink()
  dt.level_up(PECO)
  dt.level_up(PECO)
  dt.level_up(PECO)
  dt.level_up(PECO)
  dt.level_up(PECO)         # Manmo
  dt.boss_drop_zenny(1000)  # Manmo
  dt.pick_up_zenny(800)
  dt.use_skill_ink()
  dt.split("Desert", 53540)

  # Enter Myria Station
  dt.buy(17600) # 2 Protectors
  dt.buy(5760)  # Sun Mask
  dt.buy(17600) # Force Armor
  dt.buy(12800) # Atomic Bomb
  dt.buy(5000)   # a bunch of ammonias and votamins
  dt.sell(14267) # Sell unneeded weapons and armor
  dt.level_up(REI)
  dt.level_up(REI)
  dt.level_up(REI)
  dt.pick_up_zenny(800)
  dt.pick_up_zenny(400)
  dt.split("Enter Myria Station", 12807)

  # Lab
  dt.buy(9 * 2400) # 9 Soul Gems
  dt.sell(9600) # unused weapons an armour
  dt.pick_up_zenny(10000)
  dt.level_up(REI)
  dt.level_up(REI)
  dt.level_up(REI)
  dt.level_up(REI)
  dt.level_up(RYU)
  dt.level_up(MOMO)
  dt.level_up(REI)          # Chimera
  dt.boss_drop_zenny(2000)  # Chimera
  dt.level_up(REI)
  dt.split("Lab", 18354) # Split is when I re-enter main area

  # Eden
  dt.level_up(RYU)
  dt.level_up(REI)
  dt.level_up(RYU)
  dt.level_up(REI, levels=2)  # Dragon Lord
  dt.level_up(MOMO, levels=2) # Dragon Lord
  dt.level_up(RYU, levels=2)  # Dragon Lord
  dt.boss_drop_zenny(12000)   # Dragon Lord
  dt.level_up(REI)
  dt.split("Eden", 32979) # Split when I re-enter the main area

  # Myria
  dt.split("Myria", 39261)

  # Berserkr & Archmage
  dt.level_up(REI)  # Berserker
  dt.level_up(MOMO) # Berserker
  dt.level_up(RYU)  # Berserker
  dt.level_up(REI)
  dt.level_up(REI)  # Archemage
  dt.level_up(MOMO) # Archemage
  dt.level_up(RYU)  # Archemage
  dt.split("Berserkr & Archmage", 44261)

### END OF USER COMMANDS ###
