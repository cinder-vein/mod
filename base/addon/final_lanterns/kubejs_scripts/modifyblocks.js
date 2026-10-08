ItemEvents.modification(event => {
    event.modify('kubejs:redlanternbattery', item => {
      item.craftingRemainder = Item.of('kubejs:redlanternbattery').item
    })
    event.modify('kubejs:orangelanternbattery', item => {
        item.craftingRemainder = Item.of('kubejs:orangelanternbattery').item
      })
      event.modify('kubejs:greenlanternbattery', item => {
        item.craftingRemainder = Item.of('kubejs:greenlanternbattery').item
      })
      event.modify('kubejs:bluelanternbattery', item => {
        item.craftingRemainder = Item.of('kubejs:bluelanternbattery').item
      })
      event.modify('kubejs:yellowlanternbattery', item => {
        item.craftingRemainder = Item.of('kubejs:yellowlanternbattery').item
      })
      event.modify('kubejs:pinklanternbattery', item => {
        item.craftingRemainder = Item.of('kubejs:pinklanternbattery').item
      })
      event.modify('kubejs:goldlanternbattery', item => {
        item.craftingRemainder = Item.of('kubejs:goldlanternbattery').item
      })
      event.modify('final_lanterns:indigostaff', item => {
        item.craftingRemainder = Item.of('final_lanterns:indigostaff').item
      })
            event.modify('final_lanterns:sworddjinn', item => {
        item.craftingRemainder = Item.of('final_lanterns:sworddjinn').item
      })
            event.modify('final_lanterns:pridebattery', item => {
        item.craftingRemainder = Item.of('final_lanterns:pridebattery').item
      })
            event.modify('kubejs:corruptedfatebattery', item => {
        item.craftingRemainder = Item.of('kubejs:corruptedfatebattery').item
      })
            event.modify('final_lanterns:yinyangsword', item => {
        item.craftingRemainder = Item.of('final_lanterns:yinyangsword').item
      })
            event.modify('final_lanterns:whitelanternring', item => {
        item.craftingRemainder = Item.of('final_lanterns:whitelanternring').item
      })
            event.modify('kubejs:graylanternbattery', item => {
        item.craftingRemainder = Item.of('kubejs:graylanternbattery').item
      })
  })