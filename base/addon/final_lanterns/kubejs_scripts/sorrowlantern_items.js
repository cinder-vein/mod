// Listen to item registry event
StartupEvents.registry('item', e => {


    e.create('greatsword_sorrow', 'sword')
    .tier('diamond')
    .attackDamageBaseline(2.0)
    .displayName('Sorrow Great Sword')
    .parentModel('kubejs:item/sorrow/greatsword')
    .texture('kubejs:item/sorrow/greatsword')

    e.create('scythe_sorrow', 'sword')
    .tier('diamond')
    .attackDamageBaseline(2.0)
    .displayName('Sorrow Scythe')
    .parentModel('kubejs:item/sorrow/scythe')
    .texture('kubejs:item/sorrow/scythe')

    e.create('bostaff_sorrow', 'sword')
    .tier('diamond')
    .attackDamageBaseline(2.0)
    .displayName('Sorrow Bostaff')
    .parentModel('kubejs:item/sorrow/spear')
    .texture('kubejs:item/sorrow/spear')
    
    e.create('axe_sorrow', 'axe')
    .tier('diamond')
    .attackDamageBaseline(2.0)
    .displayName('Sorrow Axe')
    .texture('kubejs:item/sorrow/axe')

    e.create('pickaxe_sorrow', 'pickaxe')
    .tier('diamond')
    .attackDamageBaseline(2.0)
    .displayName('Sorrow Pickaxe')
    .texture('kubejs:item/sorrow/pickaxe')

    e.create('shovel_sorrow', 'shovel')
    .tier('diamond')
    .attackDamageBaseline(1.0)
    .displayName('Sorrow Shovel')
    .texture('kubejs:item/sorrow/shovel')
  })