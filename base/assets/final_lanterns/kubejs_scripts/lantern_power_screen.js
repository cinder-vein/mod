let Minecraft = Java.loadClass('net.minecraft.client.Minecraft');
const RenderSystem = Java.loadClass('com.mojang.blaze3d.systems.RenderSystem');
//The render power screen event
PalladiumEvents.renderPowerScreen(e => {
    //Get Entity Client Sided
    let entity = Minecraft.getInstance().player
    if (!entity) return;
    let width = e.screen.width / 2
    let height = e.screen.height / 2
    //Checks to see if the tab is the requested power, or if you want to use it for a namespace, you can use: e.tab.toString().includes(`namespace:`)
    if (e.tab.toString().includes('final_lanterns:')) {
        let tab_name = e.tab.toString().replace('final_lanterns:', '')
        {
            let size = 257
            e.guiGraphics.blit(new ResourceLocation(`final_lanterns:textures/gui/ability_bars/${tab_name}_hud.png`),
                ((width) - 126), ((height) - 98), (0), (0), (size), (size), (size), (size));
        }
    }
});