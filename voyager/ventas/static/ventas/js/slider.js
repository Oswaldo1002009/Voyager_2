$(function() {
    $( "#slider-range" ).slider({
      range: true,
      min: 0,
      max: 20,
      values: [ 0, 20 ],
      slide: function( event, ui ) {
        $( "#duracion" ).val( ui.values[ 0 ] + " - " + ui.values[ 1 ] + " días" );
      }
    });
    $( "#duracion" ).val( $( "#slider-range" ).slider( "values", 0 ) +
      " - " + $( "#slider-range" ).slider( "values", 1 ) + " días" );
  } );