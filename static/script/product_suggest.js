var titles = {}
var searchoption = null;
var doctype = $("#customsearch").data('doctype');

$("#customsearch").on('input', function(){
  autosuggest($(this).val());
 });
//requet GET à chaque nouvelle lettre tapées
function autosuggest(value){
  $.get("/suggest_product/suggest", {search: value},         function(data){
    console.log(data);
   showSuggestions(data);
  });
 }
//affiche les resultats renvoyés par ES
 function showSuggestions(data){
  var div = '';
  console.log(data.hits.hits);
  data.hits.hits.forEach(function(suggestion){
    div += ('<li class="suggestions">' + suggestion['_source']['title'] + '</li>');

  });
  $('.product-auto-suggest').html(div);
 }

//------------------------------------------------------------------------------------------

