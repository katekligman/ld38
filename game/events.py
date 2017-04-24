def default_collision_callback(sprite1, sprite2, map):
    if sprite1.map is None:
        map.add_sprite(sprite1)
    elif sprite2.map is None:
        map.add_sprite(sprite2)

def creature_hero_collision_callback(creature, hero, map):

    raise Exception("hero collided")

def hero_portal_collision_callback(hero, portal, map):

    to_portal = portal.to_portal
    new_map = to_portal.map

    # Change x and y coordinates
    hero.x = to_portal.x + hero.width
    hero.y = to_portal.y

    new_map.add_sprite(hero)
    new_map.render()
