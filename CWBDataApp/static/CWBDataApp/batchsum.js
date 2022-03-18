jQuery(document).ready(function($) {
        var $value = $('.weight'),
        $percent = $('#colourPercent'),
        $foampercent = $('#foamPercent'),
        $weight = $('#colourWeight'),
        $foamweight = $('#foamWeight'),
        $material1 = $('#material1');;
        var total = 0;

    //When weight changes sum up all weights
    $value.on('input', function(e) {
        total = 0 ;
        $value.each(function(index, elem) {
            if(!Number.isNaN(parseFloat(this.value, 10)))
                total = total + parseFloat(this.value, 10);
        });
        $('#weightSum').val(total);
    });

    //When a percent for colour is inputted, calculate the weight of colour needed
    $percent.on('input', function(e) {
        var percent = 0;
        if(!Number.isNaN(parseFloat(this.value, 10)))
            percent = $('#weightSum').val() * (parseFloat(this.value, 10) / 100);

        $weight.val(percent);
    });

    //When a percent for foam is inputted, calculate the weight of foam needed
    $foampercent.on('input', function(e) {
        var percent = 0;
        if(!Number.isNaN(parseFloat(this.value, 10)))
            percent = $('#weightSum').val() * (parseFloat(this.value, 10) / 100);

        $foamweight.val(percent);
    });

});
