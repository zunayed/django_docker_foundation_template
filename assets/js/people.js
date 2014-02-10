/*global $:false */

//hoverinfo
$('.people').hover(function(){

  var fname = $(this).attr('fname');
  var lname = $(this).attr('lname');
  var role = $(this).attr('role');

  $('#info').html('<h2><b>People / ' + fname + ' ' + lname + ' - ' + role + '</b></h2>');
});

//search box
$('#search').on('keyup', function(){

  var val = $.trim($(this).val()).toLowerCase();

  $('.people').hide().filter(function () {
    var text = $(this).attr('fname').toLowerCase() + $(this).attr('lname').toLowerCase();
    return text.indexOf(val) != -1 ;
  }).show();
});

