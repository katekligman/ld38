def default_collision_callback(sprite1, sprite2, map):
    if sprite1.map is None:
        map.add_sprite(sprite1)
    elif sprite2.map is None:
        map.add_sprite(sprite2)

def creature_hero_collision_callback(creature, hero, map):

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
    hero.x = to_portal.x + hero.width
    hero.y = to_portal.y

    new_map.add_sprite(hero)
    new_map.render()
