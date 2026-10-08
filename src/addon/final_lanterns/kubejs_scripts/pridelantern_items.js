// Listen to item registry event
StartupEvents.registry('item', e => {

    e.create('greatsword_igris', 'sword')
    .tier('diamond')
    .attackDamageBaseline(2.0)
    .displayName('Pride Greatsword')
    .parentModel('kubejs:item/pride/bat')
    .texture('kubejs:item/pride/bat')

    e.create('dagger_pride', 'sword')
    .tier('diamond')
    .attackDamageBaseline(2.0)
    .displayName('Pride Dagger')
    .texture('kubejs:item/pride/dagger')

    e.create('hammer_pride', 'sword')
    .tier('diamond')
    .attackDamageBaseline(2.0)
    .displayName('Pride Hammer')
    .parentModel('kubejs:item/pride/hammer')
    .texture('kubejs:item/pride/hammer')

    e.create('scythe_pride', 'sword')
    .tier('diamond')
    .attackDamageBaseline(2.0)
    .displayName('Pride Scythe')
    .parentModel('kubejs:item/pride/scythe')
    .texture('kubejs:item/pride/scythe')
    
    e.create('axe_pride', 'axe')
    .tier('diamond')
    .attackDamageBaseline(2.0)
    .displayName('Pride Axe')
    .texture('kubejs:item/pride/axe')

    e.create('pickaxe_pride', 'pickaxe')
    .tier('diamond')
    .attackDamageBaseline(2.0)
    .displayName('Pride Pickaxe')
    .texture('kubejs:item/pride/pickaxe')

    e.create('shovel_pride', 'shovel')
    .tier('diamond')
    .attackDamageBaseline(1.0)
    .displayName('Pride Shovel')
    .texture('kubejs:item/pride/shovel')
  })