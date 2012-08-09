// app.js
// Copyright 2012 Stripe Consulting
// Author: Damian Mullins
// Updated: 31/07/2012

jQuery(document).ready(function ($) {

  var keyword = $("input[name=url]").val();
  
  if(!keyword){
    $("input[name^='title']").keyup(function(){
       var text = $(this).val();
           text = text.toLowerCase();
           text = text.replace(/[^a-zA-Z0-9]+/g,'-');
       $("input[name=url]").val(text);       
     });
  }
	
	$('.delete').click(function() {
		return confirm('Last chance! Are you sure you would like to delete this post?');
	})
});