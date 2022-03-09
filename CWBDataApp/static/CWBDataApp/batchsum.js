jQuery(document).ready(function($) {
        var $value = $('.weight'),
        $percent = $('#colourPercent'),
        $foampercent = $('#foamPercent'),
        $weight = $('#colourWeight'),
        $foamweight = $('#foamWeight');
        var total = 0;
    $value.on('input', function(e) {
        total = 0 ;
        $value.each(function(index, elem) {
            if(!Number.isNaN(parseFloat(this.value, 10)))
                total = total + parseFloat(this.value, 10);
        });
        $('#weightSum').val(total);
    });
    $percent.on('input', function(e) {
        var percent = 0;
        if(!Number.isNaN(parseFloat(this.value, 10)))
            percent = $('#weightSum').val() * parseFloat(this.value, 10);

        $weight.val(percent);
    });
    $foampercent.on('input', function(e) {
        var percent = 0;
        if(!Number.isNaN(parseFloat(this.value, 10)))
            percent = $('#weightSum').val() * parseFloat(this.value, 10);

        $foamweight.val(percent);
    });
});
