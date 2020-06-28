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
  dt.boss_drop_zenny(50) # Second Nu fight
  dt.split("Nu", 305)

  # Pre-Manor
  dt.buy_weapon(BRONZE_SWORD, 240)
  dt.buy(40) # Wooden Rod
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
  dt.buy_skill_ink()
  dt.split("Pre-Manor", 397)

  # After Manor
  dt.level_up(TEEPO)
  dt.level_up(RYU)
  dt.boss_drop_zenny(10) # Pooch
  dt.level_up(TEEPO)
  dt.level_up(RYU)
  dt.pick_up_zenny(120)
  dt.boss_drop_zenny(8)  # Torast
  dt.level_up(TEEPO)
  dt.level_up(RYU)
  dt.pick_up_zenny(40)
  dt.boss_drop_zenny(20) # Kassen
  dt.boss_drop_zenny(4)  # Galtel
  dt.boss_drop_zenny(24) # Doksen
  dt.pick_up_zenny(600)
  dt.level_up(TEEPO)
  dt.level_up(RYU)
  dt.pick_up_weapon(BROAD_SWORD)
  dt.level_up(REI)
  dt.level_up(TEEPO)
  dt.level_up(RYU)
  dt.boss_drop_zenny(200) # Amalgam
  dt.split("After Manor", 1674)

  # Wake Up In A Cell
  dt.pick_up_zenny(200)
  dt.lose_character(REI)
  dt.lose_character(TEEPO)
  dt.level_up(RYU)
  dt.split("Wake up in a cell", 2068)

  # Across Mr. Boumore
  dt.pick_up_skill_ink()
  dt.gain_character(NINA)
  dt.level_up(RYU)
  dt.level_up(RYU)
  dt.buy_weapon(MACE, 280)
  dt.buy_weapon(MAGICIAN_ROD, 546)
  dt.buy_weapon(RIPPERS, 420)
  dt.pick_up_zenny(80)
  dt.level_up(NINA)
  dt.pick_up_zenny(400)
  dt.pick_up_weapon(BENT_SWORD)
  dt.split("Across Mr. Boumore", 1632)

  # Tower
  dt.buy(2 * 20) # Toad and Old Popper from Merchant outside
  dt.level_up(NINA)
  dt.level_up(NINA)
  dt.gain_character(MOMO)
  dt.pick_up_skill_ink()
  dt.pick_up_weapon(ICE_CHRYSM)
  dt.pick_up_weapon(FIRE_CHRYSM)
  dt.pick_up_zenny(800)
  dt.level_up(RYU)
  dt.pick_up_zenny(40)
  dt.split("Tower", 2841)

  # Clean The Dump
  dt.pick_up_weapon(SCRAMASAX)
  dt.pick_up_zenny(80)
  dt.buy(30) # Inn at Plant
  dt.pick_up_zenny(1200)
  dt.level_up(MOMO)
  dt.level_up(RYU)
  dt.boss_drop_zenny(300)
  dt.use_skill_ink()
  dt.gain_character(PECO)
  dt.split("Clean The Dump", 4832)

  # Champion
  dt.pick_up_zenny(40)
  dt.level_up(RYU, levels=5)
  dt.buy(100) # Inn in arena
  dt.level_up(RYU)
  dt.boss_drop_zenny(340)
  dt.boss_drop_zenny(350)
  dt.gain_character(GARR)
  dt.level_up(MOMO)
  dt.boss_drop_zenny(500)
  dt.level_up(MOMO)
  dt.pick_up_zenny(400)
  dt.pick_up_zenny(200)
  dt.split("Champion", 6562)

  # Fix the Lighthouse
  dt.buy(50) # Float
  dt.use_skill_ink()
  dt.pick_up_skill_ink()
  dt.boss_drop_zenny(1000) # Gazer
  dt.boss_drop_zenny(200) # Dolphin
  dt.level_up(NINA, levels=8)
  dt.use_skill_ink()
  dt.split("Fix the Lighthouse", 9495)

  # Through the Volcano
  dt.level_up(RYU)
  dt.level_up(MOMO)
  dt.level_up(RYU)
  dt.boss_drop_zenny(1000)
  dt.split("Through the Volcano", 12205)

  # The Grind
  dt.buy(12000) # Barbarossa
  dt.use_skill_ink()
  dt.buy(2 * 50 + 10 * 10) # 2 Vitamins and 10 Healing Herbs
  dt.level_up(PECO, levels=7)
  dt.level_up(PECO) # change master to Meryleep
  dt.level_up(PECO, levels=2)
  dt.level_up(PECO)
  dt.level_up(PECO)
  dt.level_up(PECO)
  dt.level_up(PECO)
  dt.level_up(PECO)
  dt.level_up(PECO) # go back to Meryleep
  dt.use_skill_ink()
  dt.level_up(RYU)
  dt.level_up(RYU)
  dt.split("The Grind", 6402)

  # Childhood Ends
  dt.level_up(RYU)
  dt.pick_up_skill_ink()
  dt.split("Childhood Ends", 7538)

  # Out of Mine
  dt.lose_character(NINA)
  dt.lose_character(MOMO)
  dt.lose_character(PECO)
  dt.level_up(GARR)
  dt.boss_drop_zenny(300)
  dt.level_up(GARR)
  dt.pick_up_zenny(3000)
  dt.split("Out of Mine", 12384)

  # Revenge
  dt.buy(4 * 4000) # Manly clothes
  dt.level_up(RYU)
  dt.level_up(GARR)
  dt.pick_up_zenny(800)
  dt.level_up(RYU)
  dt.gain_character(NINA)
  dt.boss_drop_zenny(1500)
  dt.gain_character(REI)
  dt.level_up(REI, levels=12)
  dt.pick_up_zenny(80)
  dt.split("Revenge", 13479)

  # After Plant
  dt.gain_character(MOMO)
  dt.gain_character(PECO)
  dt.buy(10000) # Emitai
  dt.level_up(MOMO)
  dt.level_up(GARR)
  dt.buy(30) # Rest at Plant
  dt.pick_up_skill_ink()
  dt.level_up(MOMO)
  dt.level_up(GARR)
  dt.boss_drop_zenny(300)
  dt.level_up(MOMO)
  dt.level_up(RYU)
  dt.level_up(GARR)
  dt.level_up(MOMO)
  dt.boss_drop_zenny(300)
  dt.pick_up_zenny(400)
  dt.split("After Plant", 10304)

  # Free Deis
  dt.use_skill_ink()
  dt.boss_drop_zenny(500)
  dt.use_skill_ink() # give Steal back to Momo to get Beef Jerky from Cerberus, fml
  dt.split("Free Deis", 12777)

  # Minigame Hell
  dt.level_up(NINA)
  dt.level_up(GARR)
  dt.boss_drop_zenny(200)
  dt.level_up(RYU)
  dt.split("Minigame Hell", 13442)

  # Across the Sea
  dt.pick_up_skill_ink()
  dt.level_up(NINA)
  dt.pick_up_zenny(2400)
  dt.level_up(MOMO)
  dt.level_up(NINA, levels=2)
  dt.level_up(GARR, levels=2)
  dt.boss_drop_zenny(1000)
  dt.split("Across the Sea", 19817)

  # Fixed the Antenna
  dt.buy(10 * 10 + 16 * 4) # 10 Vitamins, 16 Healing Herbs
  dt.buy(8000) # AP Shells
  dt.level_up(RYU)
  dt.level_up(REI)
  dt.level_up(MOMO)
  dt.buy(100) # Inn
  dt.use_skill_ink()
  dt.pick_up_zenny(4000)
  dt.pick_up_skill_ink()
  dt.level_up(RYU)
  dt.split("Fixed the Antenna", 21584)

  # Elder
  dt.pick_up_skill_ink()
  dt.use_skill_ink()
  dt.level_up(MOMO, levels=14)
  dt.split("Elder", 21584)

  # After Factory
  dt.buy_skill_ink(amt=2)
  dt.pick_up_skill_ink()
  dt.level_up(NINA)
  dt.level_up(NINA)
  dt.split("After Factory", 28234)

  # Desert
  dt.level_up(RYU)
  dt.level_up(NINA)
  dt.level_up(PECO)
  dt.level_up(PECO)
  dt.use_skill_ink()
  dt.level_up(PECO)
  dt.level_up(MOMO)
  dt.level_up(PECO)
  dt.level_up(PECO)
  dt.level_up(PECO)
  dt.level_up(PECO)
  dt.level_up(PECO)
  dt.level_up(PECO)
  dt.use_skill_ink()
  dt.level_up(REI)
  dt.level_up(REI)
  dt.level_up(REI)
  dt.level_up(RYU)
  dt.level_up(REI)
  dt.level_up(REI)
  dt.level_up(REI)
  dt.level_up(REI)
  dt.boss_drop_zenny(1000)
  dt.pick_up_zenny(800)
  dt.use_skill_ink()
  dt.split("Desert", 54124)

  # After Lab
  dt.buy(24000) # 10 soul gems
  dt.buy(17600) # 2 Protectors
  dt.buy(5760)  # Sun Mask
  dt.sell(70186 - 6766) # Sell all unneeded weapons and armor
  dt.buy(17600) # Force Armor
  dt.buy(12800) # Atomic Bomb
  dt.buy(900)   # 6 Ammonia
  dt.buy(3680)  # 92 Vitamins
  dt.pick_up_zenny(800)
  dt.level_up(REI)
  dt.pick_up_zenny(400)
  dt.level_up(RYU)
  dt.level_up(MOMO)
  dt.level_up(REI)
  dt.level_up(REI)
  dt.level_up(REI)
  dt.level_up(RYU)
  dt.boss_drop_zenny(2000)
  dt.split("After Lab", 48056)

  # Dragon Lord
  dt.level_up(REI)
  dt.level_up(MOMO)
  dt.level_up(RYU)
  dt.level_up(RYU)
  dt.level_up(REI, levels=2)
  dt.level_up(MOMO)
  dt.level_up(RYU, levels=2)
  dt.boss_drop_zenny(3000)
  dt.split("Dragon Lord", 62305)

  # Myria
  dt.level_up(REI)
  dt.split("Myria", 68574)

  # Kerserkr & Archmage
  dt.buy(30000) # 10 Soul gems
  dt.level_up(REI)
  dt.level_up(MOMO)
  dt.level_up(RYU)
  dt.level_up(REI)
  dt.level_up(MOMO)
  dt.level_up(RYU)
  dt.split("Berserkr & Archmage", 43574)
### END OF USER COMMANDS ###
