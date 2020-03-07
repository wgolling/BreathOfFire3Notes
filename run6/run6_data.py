from datatracker import *

def track_data(dt):
  # Segement 0: Awakening
  dt.split("Awakening")


  ### START OF USER COMMANDS ###

  dt.pick_up_weapon(MELTED_BLADE)
  dt.gain_character(REI)
  dt.gain_character(TEEPO)
  dt.split("Second Awakening")

  dt.pick_up_skill_ink()
  dt.pick_up_zenny(40)
  dt.pick_up_weapon(BENT_SWORD)
  dt.pick_up_zenny(200)
  dt.pick_up_weapon(BALLOCK_KNIFE)
  dt.level_up(REI)
  dt.boss_drop_zenny(50)
  dt.set_current_zenny(305)
  dt.split("Nu")

  dt.buy_weapon(BRONZE_SWORD, 240)
  dt.buy(40) # Wodden Rod
  dt.buy(2 * 10)  # Herbs
  dt.level_up(TEEPO)
  dt.level_up(RYU)
  dt.pick_up_weapon(POINTED_STICK)
  dt.pick_up_weapon(POINTED_STICK)
  dt.level_up(REI)
  dt.level_up(TEEPO)
  dt.level_up(RYU)
  dt.pick_up_zenny(80)
  dt.pick_up_zenny(120)
  dt.pick_up_weapon(SILVER_KNIFE)
  dt.pick_up_skill_ink()
  dt.set_current_zenny(397)
  dt.split("Pre-Manor")

  dt.level_up(TEEPO)
  dt.level_up(RYU)
  dt.boss_drop_zenny(10) # Pooch
  dt.level_up(TEEPO)
  dt.level_up(RYU)
  dt.pick_up_zenny(120)
  dt.boss_drop_zenny(8) # Torast
  dt.level_up(TEEPO)
  dt.level_up(RYU)
  dt.pick_up_zenny(40)
  dt.boss_drop_zenny(20) # Kassen
  dt.boss_drop_zenny(4) # Galtel
  dt.boss_drop_zenny(24) # Doksen
  dt.pick_up_zenny(600)
  dt.level_up(TEEPO)
  dt.level_up(RYU)
  dt.pick_up_weapon(BROAD_SWORD)
  dt.level_up(REI)
  dt.level_up(TEEPO)
  dt.level_up(RYU)
  dt.level_up(TEEPO)
  dt.level_up(RYU)
  dt.boss_drop_zenny(200) # Amalgam
  dt.lose_character(REI)
  dt.lose_character(TEEPO)
  dt.set_current_zenny(1674)
  dt.split("After Manor")

  dt.pick_up_zenny(200)
  dt.level_up(RYU)
  dt.set_current_zenny(2068)
  dt.split("Wake up in a cell")

  dt.gain_character(NINA)
  dt.split("buh")
  ### END OF USER COMMANDS ###
