StartupEvents.registry('palladium:condition_serializer', (event) => {
    event.create('finallanterns:get_y')
        .addProperty('min', 'float', 60, 'minimum y level')
        .addProperty('max', 'float', 100, 'maximum y level')
        .test((entity, props) => {
            let min = props.get('min');
            let max = props.get('max');
            let y_level = entity.y;
            if (y_level >= min && y_level <= max) {
                return true;
            } else {
                return false;
            }
        })
});