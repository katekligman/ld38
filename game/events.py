def hero_map_change_teleportation_callback(hero, portal):
    hero.free_creatures()
    hero.teleportation_handler.trigger("win_check", hero, portal)

def win_check_teleportation_callback(hero, portal):
    level = hero.level
    win_check = True
    for m in level.maps:
        for s in m.sprites.values():
            if hasattr(s, "home_map") and s.home_map.name != m.name:
                win_check = False
    level.is_won = win_check

def default_collision_callback(sprite1, sprite2, map):
    if sprite1.map is None:
        map.add_sprite(sprite1)
    elif sprite2.map is None:
        map.add_sprite(sprite2)

def creature_hero_collision_callback(creature, hero, map):

    # don't remove creatures that are in their home map
    if creature.map.name == creature.home_map.name:
        if hero.map is None:
            map.add_sprite(hero)
        return

    # Only one sprite is removed from map
    # If it's the hero, then we also have to remove creature
    # from map
    if hero.map is None:
        map.add_sprite(hero)
        map.pop_sprite(creature.name)

    map.undraw(creature)
    hero.grab(creature)

def hero_portal_collision_callback(hero, portal, map):

    to_portal = portal.to_portal
    new_map = to_portal.map

    # Change x and y coordinates
    hero.x = to_portal.x + to_portal.width
    hero.y = to_portal.y

    new_map.add_sprite(hero)
    new_map.render()
    hero.teleportation_handler.trigger("hero_map_change", hero, portal)
