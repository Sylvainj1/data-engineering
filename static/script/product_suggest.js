var titles = {}
var searchoption = null;
var doctype = $("#customsearch").data('doctype');
//Typing into the input box will generate autosuggestions
$("#customsearch").on('input', function(){
  autosuggest($(this).val());
 });
//Sends a GET request to grab suggested job titles based through ElasticSearch
function autosuggest(value){
  $.get("/suggest_product/suggest", {search: value},         function(data){
    console.log(data);
   showSuggestions(data);
  });
 }
//Creates the Suggestion dropdown
 function showSuggestions(data){
  var div = '';
  console.log(data.hits.hits);
  data.hits.hits.forEach(function(suggestion){
    div += ('<li class="suggestions">' + suggestion['_source']['title'] + '</li>');

  });
  $('.product-auto-suggest').html(div);
 }