PalladiumEvents.registerAnimations((event) => {
    event.register('final_lanterns/lanternsoath', 10, (builder) => {
        const bluecharge_ring_anim = animationUtil.getAnimationTimerAbilityValue(builder.getPlayer(), 'final_lanterns:bluelanternsoath', 'charge_ring_anim', builder.getPartialTicks());
        const redcharge_ring_anim = animationUtil.getAnimationTimerAbilityValue(builder.getPlayer(), 'final_lanterns:redlanternsoath', 'charge_ring_anim', builder.getPartialTicks());
        const roaranim = animationUtil.getAnimationTimerAbilityValue(builder.getPlayer(), 'final_lanterns:redlantern', 'roar_anim', builder.getPartialTicks());
        const roaranim1 = animationUtil.getAnimationTimerAbilityValue(builder.getPlayer(), 'final_lanterns:whitelantern', 'roar_anim1', builder.getPartialTicks());
        const corruptcharge_ring_anim = animationUtil.getAnimationTimerAbilityValue(builder.getPlayer(), 'final_lanterns:corruptedfateoath', 'charge_ring_anim', builder.getPartialTicks());
        const orangecharge_ring_anim = animationUtil.getAnimationTimerAbilityValue(builder.getPlayer(), 'final_lanterns:orangelanternsoath', 'charge_ring_anim', builder.getPartialTicks());
        const greencharge_ring_anim = animationUtil.getAnimationTimerAbilityValue(builder.getPlayer(), 'final_lanterns:greenlanternsoath', 'charge_ring_anim', builder.getPartialTicks());
        const yellowcharge_ring_anim = animationUtil.getAnimationTimerAbilityValue(builder.getPlayer(), 'final_lanterns:yellowlanternsoath', 'charge_ring_anim', builder.getPartialTicks());
        const pinkcharge_ring_anim = animationUtil.getAnimationTimerAbilityValue(builder.getPlayer(), 'final_lanterns:pinklanternsoath', 'charge_ring_anim', builder.getPartialTicks());
        const goldcharge_ring_anim = animationUtil.getAnimationTimerAbilityValue(builder.getPlayer(), 'final_lanterns:goldlanternsoath', 'charge_ring_anim', builder.getPartialTicks());
        const graycharge_ring_anim = animationUtil.getAnimationTimerAbilityValue(builder.getPlayer(), 'final_lanterns:sorrowlanternsoath', 'charge_ring_anim', builder.getPartialTicks());
        const pridecharge_ring_anim = animationUtil.getAnimationTimerAbilityValue(builder.getPlayer(), 'final_lanterns:pridelanternsoath', 'charge_ring_anim', builder.getPartialTicks());
        const whitecharge_ring_anim = animationUtil.getAnimationTimerAbilityValue(builder.getPlayer(), 'final_lanterns:whitelanternsoath', 'charge_ring_anim', builder.getPartialTicks());
        const starheartcharge_ring_anim = animationUtil.getAnimationTimerAbilityValue(builder.getPlayer(), 'final_lanterns:starheartsoath', 'charge_ring_anim', builder.getPartialTicks());
        const driving = animationUtil.getAnimationTimerAbilityValue(builder.getPlayer(), 'final_lanterns:greenlantern', 'driving', builder.getPartialTicks());
        const drivin = animationUtil.getAnimationTimerAbilityValue(builder.getPlayer(), 'final_lanterns:starheart', 'drivin', builder.getPartialTicks());
        const resurection = animationUtil.getAnimationTimerAbilityValue(builder.getPlayer(), 'final_lanterns:parallax', 'animation', builder.getPartialTicks());
        if (bluecharge_ring_anim > 0.0) {
            builder.get('left_arm').setXRotDegrees(-83.8407).animate('InOutCubic', bluecharge_ring_anim);
            builder.get('left_arm').setYRotDegrees(60.6524).animate('InOutCubic', bluecharge_ring_anim);
            builder.get('left_arm').setZRotDegrees(-61.6781).animate('InOutCubic', bluecharge_ring_anim);
            builder.get('right_arm').setXRotDegrees(-105.2126).animate('InOutCubic', bluecharge_ring_anim);
            builder.get('right_arm').setYRotDegrees(-57.557).animate('InOutCubic', bluecharge_ring_anim);
            builder.get('right_arm').setZRotDegrees(69.6731).animate('InOutCubic', bluecharge_ring_anim);

            builder.get('right_arm').setY(2).animate('InOutCubic', bluecharge_ring_anim);
            builder.get('left_arm').setY(5).animate('InOutCubic', bluecharge_ring_anim);
            builder.get('left_arm').setZ(-3.5).animate('InOutCubic', bluecharge_ring_anim);

            builder.get('head').setXRotDegrees(7.5).animate('InOutCubic', bluecharge_ring_anim);
        };
        if (roaranim > 0.0) {
            builder.get('left_arm').setXRotDegrees(90).animate('easeInOutQuint', roaranim);
            builder.get('left_arm').setYRotDegrees(0).animate('easeInOutQuint', roaranim);
            builder.get('left_arm').setZRotDegrees(50).animate('easeInOutQuint', roaranim);
            builder.get('right_arm').setXRotDegrees(80).animate('easeInOutQuint', roaranim);
            builder.get('right_arm').setYRotDegrees(0).animate('easeInOutQuint', roaranim);
            builder.get('right_arm').setZRotDegrees(-20).animate('easeInOutQuint', roaranim);
            builder.get('head').setXRotDegrees(-40).animate('easeInOutQuint', roaranim);
            builder.get('body').setXRotDegrees(-20).animate('easeInOutQuint', roaranim);
            builder.get('left_leg').setXRotDegrees(20).animate('easeInOutQuint', roaranim);
            builder.get('right_leg').setXRotDegrees(-40).animate('easeInOutQuint', roaranim);
        };
        if (roaranim1 > 0.0) {
            builder.get('left_arm').setXRotDegrees(90).animate('easeInOutQuint', roaranim1);
            builder.get('left_arm').setYRotDegrees(0).animate('easeInOutQuint', roaranim1);
            builder.get('left_arm').setZRotDegrees(50).animate('easeInOutQuint', roaranim1);
            builder.get('right_arm').setXRotDegrees(80).animate('easeInOutQuint', roaranim1);
            builder.get('right_arm').setYRotDegrees(0).animate('easeInOutQuint', roaranim1);
            builder.get('right_arm').setZRotDegrees(-20).animate('easeInOutQuint', roaranim1);
            builder.get('head').setXRotDegrees(-40).animate('easeInOutQuint', roaranim1);
            builder.get('body').setXRotDegrees(-20).animate('easeInOutQuint', roaranim1);
            builder.get('left_leg').setXRotDegrees(20).animate('easeInOutQuint', roaranim1);
            builder.get('right_leg').setXRotDegrees(-40).animate('easeInOutQuint', roaranim1);
        };
        if (corruptcharge_ring_anim > 0.0) {
            builder.get('left_arm').setXRotDegrees(-83.8407).animate('InOutCubic', corruptcharge_ring_anim);
            builder.get('left_arm').setYRotDegrees(60.6524).animate('InOutCubic', corruptcharge_ring_anim);
            builder.get('left_arm').setZRotDegrees(-61.6781).animate('InOutCubic', corruptcharge_ring_anim);
            builder.get('right_arm').setXRotDegrees(-105.2126).animate('InOutCubic', corruptcharge_ring_anim);
            builder.get('right_arm').setYRotDegrees(-57.557).animate('InOutCubic', corruptcharge_ring_anim);
            builder.get('right_arm').setZRotDegrees(69.6731).animate('InOutCubic', corruptcharge_ring_anim);

            builder.get('right_arm').setY(2).animate('InOutCubic', corruptcharge_ring_anim);
            builder.get('left_arm').setY(5).animate('InOutCubic', corruptcharge_ring_anim);
            builder.get('left_arm').setZ(-3.5).animate('InOutCubic', corruptcharge_ring_anim);

            builder.get('head').setXRotDegrees(7.5).animate('InOutCubic', corruptcharge_ring_anim);
        };
        if (pridecharge_ring_anim > 0.0) {
            builder.get('left_arm').setXRotDegrees(-83.8407).animate('InOutCubic', pridecharge_ring_anim);
            builder.get('left_arm').setYRotDegrees(60.6524).animate('InOutCubic', pridecharge_ring_anim);
            builder.get('left_arm').setZRotDegrees(-61.6781).animate('InOutCubic', pridecharge_ring_anim);
            builder.get('right_arm').setXRotDegrees(-105.2126).animate('InOutCubic', pridecharge_ring_anim);
            builder.get('right_arm').setYRotDegrees(-57.557).animate('InOutCubic', pridecharge_ring_anim);
            builder.get('right_arm').setZRotDegrees(69.6731).animate('InOutCubic', pridecharge_ring_anim);

            builder.get('right_arm').setY(2).animate('InOutCubic', pridecharge_ring_anim);
            builder.get('left_arm').setY(5).animate('InOutCubic', pridecharge_ring_anim);
            builder.get('left_arm').setZ(-3.5).animate('InOutCubic', pridecharge_ring_anim);

            builder.get('head').setXRotDegrees(7.5).animate('InOutCubic', pridecharge_ring_anim);
        };
        if (starheartcharge_ring_anim > 0.0) {
            builder.get('left_arm').setXRotDegrees(-83.8407).animate('InOutCubic', starheartcharge_ring_anim);
            builder.get('left_arm').setYRotDegrees(60.6524).animate('InOutCubic', starheartcharge_ring_anim);
            builder.get('left_arm').setZRotDegrees(-61.6781).animate('InOutCubic', starheartcharge_ring_anim);
            builder.get('right_arm').setXRotDegrees(-105.2126).animate('InOutCubic', starheartcharge_ring_anim);
            builder.get('right_arm').setYRotDegrees(-57.557).animate('InOutCubic', starheartcharge_ring_anim);
            builder.get('right_arm').setZRotDegrees(69.6731).animate('InOutCubic', starheartcharge_ring_anim);

            builder.get('right_arm').setY(2).animate('InOutCubic', starheartcharge_ring_anim);
            builder.get('left_arm').setY(5).animate('InOutCubic', starheartcharge_ring_anim);
            builder.get('left_arm').setZ(-3.5).animate('InOutCubic', starheartcharge_ring_anim);

            builder.get('head').setXRotDegrees(7.5).animate('InOutCubic', starheartcharge_ring_anim);
        };
        if (whitecharge_ring_anim > 0.0) {
            builder.get('left_arm').setXRotDegrees(-83.8407).animate('InOutCubic', whitecharge_ring_anim);
            builder.get('left_arm').setYRotDegrees(60.6524).animate('InOutCubic', whitecharge_ring_anim);
            builder.get('left_arm').setZRotDegrees(-61.6781).animate('InOutCubic', whitecharge_ring_anim);
            builder.get('right_arm').setXRotDegrees(-105.2126).animate('InOutCubic', whitecharge_ring_anim);
            builder.get('right_arm').setYRotDegrees(-57.557).animate('InOutCubic', whitecharge_ring_anim);
            builder.get('right_arm').setZRotDegrees(69.6731).animate('InOutCubic', whitecharge_ring_anim);

            builder.get('right_arm').setY(2).animate('InOutCubic', whitecharge_ring_anim);
            builder.get('left_arm').setY(5).animate('InOutCubic', whitecharge_ring_anim);
            builder.get('left_arm').setZ(-3.5).animate('InOutCubic', whitecharge_ring_anim);

            builder.get('head').setXRotDegrees(7.5).animate('InOutCubic', whitecharge_ring_anim);
        };
        if (redcharge_ring_anim > 0.0) {
            builder.get('left_arm').setXRotDegrees(-83.8407).animate('InOutCubic', redcharge_ring_anim);
            builder.get('left_arm').setYRotDegrees(60.6524).animate('InOutCubic', redcharge_ring_anim);
            builder.get('left_arm').setZRotDegrees(-61.6781).animate('InOutCubic', redcharge_ring_anim);
            builder.get('right_arm').setXRotDegrees(-105.2126).animate('InOutCubic', redcharge_ring_anim);
            builder.get('right_arm').setYRotDegrees(-57.557).animate('InOutCubic', redcharge_ring_anim);
            builder.get('right_arm').setZRotDegrees(69.6731).animate('InOutCubic', redcharge_ring_anim);

            builder.get('right_arm').setY(2).animate('InOutCubic', redcharge_ring_anim);
            builder.get('left_arm').setY(5).animate('InOutCubic', redcharge_ring_anim);
            builder.get('left_arm').setZ(-3.5).animate('InOutCubic', redcharge_ring_anim);

            builder.get('head').setXRotDegrees(7.5).animate('InOutCubic', redcharge_ring_anim);
        };
        if (orangecharge_ring_anim > 0.0) {
            builder.get('left_arm').setXRotDegrees(-83.8407).animate('InOutCubic', orangecharge_ring_anim);
            builder.get('left_arm').setYRotDegrees(60.6524).animate('InOutCubic', orangecharge_ring_anim);
            builder.get('left_arm').setZRotDegrees(-61.6781).animate('InOutCubic', orangecharge_ring_anim);
            builder.get('right_arm').setXRotDegrees(-105.2126).animate('InOutCubic', orangecharge_ring_anim);
            builder.get('right_arm').setYRotDegrees(-57.557).animate('InOutCubic', orangecharge_ring_anim);
            builder.get('right_arm').setZRotDegrees(69.6731).animate('InOutCubic', orangecharge_ring_anim);

            builder.get('right_arm').setY(2).animate('InOutCubic', orangecharge_ring_anim);
            builder.get('left_arm').setY(5).animate('InOutCubic', orangecharge_ring_anim);
            builder.get('left_arm').setZ(-3.5).animate('InOutCubic', orangecharge_ring_anim);

            builder.get('head').setXRotDegrees(7.5).animate('InOutCubic', orangecharge_ring_anim);
        };
        if (greencharge_ring_anim > 0.0) {
            builder.get('left_arm').setXRotDegrees(-83.8407).animate('InOutCubic', greencharge_ring_anim);
            builder.get('left_arm').setYRotDegrees(60.6524).animate('InOutCubic', greencharge_ring_anim);
            builder.get('left_arm').setZRotDegrees(-61.6781).animate('InOutCubic', greencharge_ring_anim);
            builder.get('right_arm').setXRotDegrees(-105.2126).animate('InOutCubic', greencharge_ring_anim);
            builder.get('right_arm').setYRotDegrees(-57.557).animate('InOutCubic', greencharge_ring_anim);
            builder.get('right_arm').setZRotDegrees(69.6731).animate('InOutCubic', greencharge_ring_anim);

            builder.get('right_arm').setY(2).animate('InOutCubic', greencharge_ring_anim);
            builder.get('left_arm').setY(5).animate('InOutCubic', greencharge_ring_anim);
            builder.get('left_arm').setZ(-3.5).animate('InOutCubic', greencharge_ring_anim);

            builder.get('head').setXRotDegrees(7.5).animate('InOutCubic', greencharge_ring_anim);
        };
        if (yellowcharge_ring_anim > 0.0) {
            builder.get('left_arm').setXRotDegrees(-83.8407).animate('InOutCubic', yellowcharge_ring_anim);
            builder.get('left_arm').setYRotDegrees(60.6524).animate('InOutCubic', yellowcharge_ring_anim);
            builder.get('left_arm').setZRotDegrees(-61.6781).animate('InOutCubic', yellowcharge_ring_anim);
            builder.get('right_arm').setXRotDegrees(-105.2126).animate('InOutCubic', yellowcharge_ring_anim);
            builder.get('right_arm').setYRotDegrees(-57.557).animate('InOutCubic', yellowcharge_ring_anim);
            builder.get('right_arm').setZRotDegrees(69.6731).animate('InOutCubic', yellowcharge_ring_anim);

            builder.get('right_arm').setY(2).animate('InOutCubic', yellowcharge_ring_anim);
            builder.get('left_arm').setY(5).animate('InOutCubic', yellowcharge_ring_anim);
            builder.get('left_arm').setZ(-3.5).animate('InOutCubic', yellowcharge_ring_anim);

            builder.get('head').setXRotDegrees(7.5).animate('InOutCubic', yellowcharge_ring_anim);
        };
            if (pinkcharge_ring_anim > 0.0) {
            builder.get('left_arm').setXRotDegrees(-83.8407).animate('InOutCubic', pinkcharge_ring_anim);
            builder.get('left_arm').setYRotDegrees(60.6524).animate('InOutCubic', pinkcharge_ring_anim);
            builder.get('left_arm').setZRotDegrees(-61.6781).animate('InOutCubic', pinkcharge_ring_anim);
            builder.get('right_arm').setXRotDegrees(-105.2126).animate('InOutCubic', pinkcharge_ring_anim);
            builder.get('right_arm').setYRotDegrees(-57.557).animate('InOutCubic', pinkcharge_ring_anim);
            builder.get('right_arm').setZRotDegrees(69.6731).animate('InOutCubic', pinkcharge_ring_anim);

            builder.get('right_arm').setY(2).animate('InOutCubic', pinkcharge_ring_anim);
            builder.get('left_arm').setY(5).animate('InOutCubic', pinkcharge_ring_anim);
            builder.get('left_arm').setZ(-3.5).animate('InOutCubic', pinkcharge_ring_anim);

            builder.get('head').setXRotDegrees(7.5).animate('InOutCubic', pinkcharge_ring_anim);
        };
        if (goldcharge_ring_anim > 0.0) {
            builder.get('left_arm').setXRotDegrees(-83.8407).animate('InOutCubic', goldcharge_ring_anim);
            builder.get('left_arm').setYRotDegrees(60.6524).animate('InOutCubic', goldcharge_ring_anim);
            builder.get('left_arm').setZRotDegrees(-61.6781).animate('InOutCubic', goldcharge_ring_anim);
            builder.get('right_arm').setXRotDegrees(-105.2126).animate('InOutCubic', goldcharge_ring_anim);
            builder.get('right_arm').setYRotDegrees(-57.557).animate('InOutCubic', goldcharge_ring_anim);
            builder.get('right_arm').setZRotDegrees(69.6731).animate('InOutCubic', goldcharge_ring_anim);

            builder.get('right_arm').setY(2).animate('InOutCubic', goldcharge_ring_anim);
            builder.get('left_arm').setY(5).animate('InOutCubic', goldcharge_ring_anim);
            builder.get('left_arm').setZ(-3.5).animate('InOutCubic', goldcharge_ring_anim);

            builder.get('head').setXRotDegrees(7.5).animate('InOutCubic', goldcharge_ring_anim);
        };
        if (graycharge_ring_anim > 0.0) {
            builder.get('left_arm').setXRotDegrees(-83.8407).animate('InOutCubic', graycharge_ring_anim);
            builder.get('left_arm').setYRotDegrees(60.6524).animate('InOutCubic', graycharge_ring_anim);
            builder.get('left_arm').setZRotDegrees(-61.6781).animate('InOutCubic', graycharge_ring_anim);
            builder.get('right_arm').setXRotDegrees(-105.2126).animate('InOutCubic', graycharge_ring_anim);
            builder.get('right_arm').setYRotDegrees(-57.557).animate('InOutCubic', graycharge_ring_anim);
            builder.get('right_arm').setZRotDegrees(69.6731).animate('InOutCubic', graycharge_ring_anim);

            builder.get('right_arm').setY(2).animate('InOutCubic', graycharge_ring_anim);
            builder.get('left_arm').setY(5).animate('InOutCubic', graycharge_ring_anim);
            builder.get('left_arm').setZ(-3.5).animate('InOutCubic', graycharge_ring_anim);

            builder.get('head').setXRotDegrees(7.5).animate('InOutCubic', graycharge_ring_anim);
        };
        if (driving == 1.0) {
            if (builder.isFirstPerson()) {
            } else {
                builder.get('left_arm').setXRotDegrees(-83.47).animate('InOutCubic', driving);
                builder.get('left_arm').setYRotDegrees(8.36).animate('InOutCubic', driving);
                builder.get('left_arm').setZRotDegrees(-6.53).animate('InOutCubic', driving);
    
                builder.get('right_arm').setXRotDegrees(10.33).animate('InOutCubic', driving);
                builder.get('right_arm').setYRotDegrees(24.9).animate('InOutCubic', driving);
                builder.get('right_arm').setZRotDegrees(86.99).animate('InOutCubic', driving);
    
                builder.get('left_leg').setXRotDegrees(-80.42).animate('InOutCubic', driving);
                builder.get('left_leg').setYRotDegrees(-5.78).animate('InOutCubic', driving);
                builder.get('left_leg').setZRotDegrees(4.08).animate('InOutCubic', driving);
    
                builder.get('right_leg').setXRotDegrees(-80.42).animate('InOutCubic', driving);
                builder.get('right_leg').setYRotDegrees(5.78).animate('InOutCubic', driving);
                builder.get('right_leg').setZRotDegrees(-4.08).animate('InOutCubic', driving);
    
                builder.get('body').setXRotDegrees(0.001).animate('InOutCubic', driving);
                builder.get('body').setYRotDegrees(0.001).animate('InOutCubic', driving);
                builder.get('body').setZRotDegrees(0.001).animate('InOutCubic', driving);
    
                builder.get('head').setXRotDegrees(1).animate('InOutCubic', driving);
            }
        };
        if (drivin == 1.0) {
            if (builder.isFirstPerson()) {
            } else {
                builder.get('left_arm').setXRotDegrees(-83.47).animate('InOutCubic', drivin);
                builder.get('left_arm').setYRotDegrees(8.36).animate('InOutCubic', drivin);
                builder.get('left_arm').setZRotDegrees(-6.53).animate('InOutCubic', drivin);
    
                builder.get('right_arm').setXRotDegrees(10.33).animate('InOutCubic', drivin);
                builder.get('right_arm').setYRotDegrees(24.9).animate('InOutCubic', drivin);
                builder.get('right_arm').setZRotDegrees(86.99).animate('InOutCubic', drivin);
    
                builder.get('left_leg').setXRotDegrees(-80.42).animate('InOutCubic', drivin);
                builder.get('left_leg').setYRotDegrees(-5.78).animate('InOutCubic', drivin);
                builder.get('left_leg').setZRotDegrees(4.08).animate('InOutCubic', drivin);
    
                builder.get('right_leg').setXRotDegrees(-80.42).animate('InOutCubic', drivin);
                builder.get('right_leg').setYRotDegrees(5.78).animate('InOutCubic', drivin);
                builder.get('right_leg').setZRotDegrees(-4.08).animate('InOutCubic', drivin);
    
                builder.get('body').setXRotDegrees(0.001).animate('InOutCubic', drivin);
                builder.get('body').setYRotDegrees(0.001).animate('InOutCubic', drivin);
                builder.get('body').setZRotDegrees(0.001).animate('InOutCubic', drivin);
    
                builder.get('head').setXRotDegrees(1).animate('InOutCubic', drivin);
            }
        };
        if (resurection == 1.0) {
                builder.get('left_arm').setXRotDegrees(20.18).animate('InOutCubic', resurection);
                builder.get('left_arm').setYRotDegrees(-10).animate('InOutCubic', resurection);
                builder.get('left_arm').setZRotDegrees(-13.4).animate('InOutCubic', resurection);
    
                builder.get('right_arm').setXRotDegrees(12.7).animate('InOutCubic', resurection);
                builder.get('right_arm').setYRotDegrees(9.8).animate('InOutCubic', resurection);
                builder.get('right_arm').setZRotDegrees(14.7).animate('InOutCubic', resurection);
    
                builder.get('right_leg').setXRotDegrees(8).animate('InOutCubic', resurection);
                builder.get('right_leg').setYRotDegrees(4.3).animate('InOutCubic', resurection);
                builder.get('right_leg').setZRotDegrees(5.6).animate('InOutCubic', resurection);
    
                builder.get('left_leg').setXRotDegrees(7.5).animate('InOutCubic', resurection);
                builder.get('left_leg').setYRotDegrees(-5).animate('InOutCubic', resurection);
                builder.get('left_leg').setZRotDegrees(-5.7).animate('InOutCubic', resurection);
    
                builder.get('head').setXRotDegrees(-20).animate('InOutCubic', resurection);
        };
    });
});
PalladiumEvents.registerAnimations((event) => {
    event.register('final_lanterns/ring_conjure_green', 10, (builder) => {
        const progress = animationUtil.getAnimationTimerAbilityValue(builder.getPlayer(), 'final_lanterns:greenlantern', 'ring_conjure_anim', builder.getPartialTicks());
        if (builder.isFirstPerson()) {
            builder.get('right_arm').setXRotDegrees(-30).setZRotDegrees(-50).animate('InOutCubic', progress);
        } else {
            builder.get('right_arm').setXRotDegrees(-50).setZRotDegrees(-40).animate('InOutCubic', progress);
        }
        if (builder.isFirstPerson()) {
            builder.get('left_arm').setXRotDegrees(-30).setZRotDegrees(50).animate('InOutCubic', progress);
        } else {
            builder.get('left_arm').setXRotDegrees(-50).setZRotDegrees(40).animate('InOutCubic', progress);
        }
    });
});
PalladiumEvents.registerAnimations((event) => {
    event.register('final_lanterns/ring_conjure_star', 10, (builder) => {
        const progress = animationUtil.getAnimationTimerAbilityValue(builder.getPlayer(), 'final_lanterns:starheart', 'ring_conjure_anim', builder.getPartialTicks());
        if (builder.isFirstPerson()) {
            builder.get('right_arm').setXRotDegrees(-30).setZRotDegrees(-50).animate('InOutCubic', progress);
        } else {
            builder.get('right_arm').setXRotDegrees(-50).setZRotDegrees(-40).animate('InOutCubic', progress);
        }
        if (builder.isFirstPerson()) {
            builder.get('left_arm').setXRotDegrees(-30).setZRotDegrees(50).animate('InOutCubic', progress);
        } else {
            builder.get('left_arm').setXRotDegrees(-50).setZRotDegrees(40).animate('InOutCubic', progress);
        }
    });
});
PalladiumEvents.registerAnimations((event) => {
    event.register('final_lanterns/ring_conjure_blue', 10, (builder) => {
        const progress = animationUtil.getAnimationTimerAbilityValue(builder.getPlayer(), 'final_lanterns:bluelantern', 'ring_conjure_anim', builder.getPartialTicks());
        if (builder.isFirstPerson()) {
            builder.get('right_arm').setXRotDegrees(-30).setZRotDegrees(-50).animate('InOutCubic', progress);
        } else {
            builder.get('right_arm').setXRotDegrees(-50).setZRotDegrees(-40).animate('InOutCubic', progress);
        }
        if (builder.isFirstPerson()) {
            builder.get('left_arm').setXRotDegrees(-30).setZRotDegrees(50).animate('InOutCubic', progress);
        } else {
            builder.get('left_arm').setXRotDegrees(-50).setZRotDegrees(40).animate('InOutCubic', progress);
        }
    });
});
PalladiumEvents.registerAnimations((event) => {
    event.register('final_lanterns/ring_conjure_pink', 10, (builder) => {
        const progress = animationUtil.getAnimationTimerAbilityValue(builder.getPlayer(), 'final_lanterns:pinklantern', 'ring_conjure_anim', builder.getPartialTicks());
        if (builder.isFirstPerson()) {
            builder.get('right_arm').setXRotDegrees(-30).setZRotDegrees(-50).animate('InOutCubic', progress);
        } else {
            builder.get('right_arm').setXRotDegrees(-50).setZRotDegrees(-40).animate('InOutCubic', progress);
        }
        if (builder.isFirstPerson()) {
            builder.get('left_arm').setXRotDegrees(-30).setZRotDegrees(50).animate('InOutCubic', progress);
        } else {
            builder.get('left_arm').setXRotDegrees(-50).setZRotDegrees(40).animate('InOutCubic', progress);
        }
    });
});
PalladiumEvents.registerAnimations((event) => {
    event.register('final_lanterns/ring_conjure_yellow', 10, (builder) => {
        const progress = animationUtil.getAnimationTimerAbilityValue(builder.getPlayer(), 'final_lanterns:yellowlantern', 'ring_conjure_anim', builder.getPartialTicks());
        if (builder.isFirstPerson()) {
            builder.get('right_arm').setXRotDegrees(-30).setZRotDegrees(-50).animate('InOutCubic', progress);
        } else {
            builder.get('right_arm').setXRotDegrees(-50).setZRotDegrees(-40).animate('InOutCubic', progress);
        }
        if (builder.isFirstPerson()) {
            builder.get('left_arm').setXRotDegrees(-30).setZRotDegrees(50).animate('InOutCubic', progress);
        } else {
            builder.get('left_arm').setXRotDegrees(-50).setZRotDegrees(40).animate('InOutCubic', progress);
        }
    });
});
PalladiumEvents.registerAnimations((event) => {
    event.register('final_lanterns/ring_conjure_indigo', 10, (builder) => {
        const progress = animationUtil.getAnimationTimerAbilityValue(builder.getPlayer(), 'final_lanterns:indigolantern', 'ring_conjure_anim', builder.getPartialTicks());
        if (builder.isFirstPerson()) {
            builder.get('right_arm').setXRotDegrees(-30).setZRotDegrees(-50).animate('InOutCubic', progress);
        } else {
            builder.get('right_arm').setXRotDegrees(-50).setZRotDegrees(-40).animate('InOutCubic', progress);
        }
        if (builder.isFirstPerson()) {
            builder.get('left_arm').setXRotDegrees(-30).setZRotDegrees(50).animate('InOutCubic', progress);
        } else {
            builder.get('left_arm').setXRotDegrees(-50).setZRotDegrees(40).animate('InOutCubic', progress);
        }
    });
});
PalladiumEvents.registerAnimations((event) => {
    event.register('final_lanterns/ring_conjure_white', 10, (builder) => {
        const progress = animationUtil.getAnimationTimerAbilityValue(builder.getPlayer(), 'final_lanterns:whitelantern', 'ring_conjure_anim', builder.getPartialTicks());
        if (builder.isFirstPerson()) {
            builder.get('right_arm').setXRotDegrees(-30).setZRotDegrees(-50).animate('InOutCubic', progress);
        } else {
            builder.get('right_arm').setXRotDegrees(-50).setZRotDegrees(-40).animate('InOutCubic', progress);
        }
        if (builder.isFirstPerson()) {
            builder.get('left_arm').setXRotDegrees(-30).setZRotDegrees(50).animate('InOutCubic', progress);
        } else {
            builder.get('left_arm').setXRotDegrees(-50).setZRotDegrees(40).animate('InOutCubic', progress);
        }
    });
});
PalladiumEvents.registerAnimations((event) => {
    event.register('final_lanterns/ring_conjure_black', 10, (builder) => {
        const progress = animationUtil.getAnimationTimerAbilityValue(builder.getPlayer(), 'final_lanterns:blacklantern', 'ring_conjure_anim', builder.getPartialTicks());
        if (builder.isFirstPerson()) {
            builder.get('right_arm').setXRotDegrees(-30).setZRotDegrees(-50).animate('InOutCubic', progress);
        } else {
            builder.get('right_arm').setXRotDegrees(-50).setZRotDegrees(-40).animate('InOutCubic', progress);
        }
        if (builder.isFirstPerson()) {
            builder.get('left_arm').setXRotDegrees(-30).setZRotDegrees(50).animate('InOutCubic', progress);
        } else {
            builder.get('left_arm').setXRotDegrees(-50).setZRotDegrees(40).animate('InOutCubic', progress);
        }
    });
});
