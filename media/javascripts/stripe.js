// stripe.bp.js
// Copyright 2012 Stripe Consulting
// Author: Damian Mullins
// Updated: 31/07/2012

// Self-Executing Anonymous Function (Public & Private)
(function (stripe, $, undefined) {

  /*--------------------------------------------------------------------------------
    Contents                                                                       
  ----------------------------------------------------------------------------------
  
    Private Properties
    
    Public Properties
    
    Public Methods
      init -
    
    Private Methods
      SlideshowInit - 
      Sanitize - Check if a string is equal to 'undefined'
      StringUtils - 
      ArrayUtils - Extend the Array Object
                                                                                   
  --------------------------------------------------------------------------------*/
  

  /* -----------------------------------------
    Private Properties
  ----------------------------------------- */
  //var isHot = true;



  /* -----------------------------------------
    Public Properties
  ----------------------------------------- */
  //stripe.ingredient = "Bacon Strips";
  
  
  
  /* -----------------------------------------
    Public Methods
  ----------------------------------------- */
   
  stripe.init = function() {
  
    StringUtils();
    ArrayUtils();
    
    
    // Slideshow
    if ($('.slideshow').length > 0) {
      SlideshowInit();
    }
    
    
    // Highlight code blocks
    $('pre code').each(function(i, e) {
      hljs.highlightBlock(e);
    });
    
    
    // Image galleries
    if ($('figure a').length > 0) {
      $(".fancybox").fancybox({
        prevEffect: 'none',
        nextEffect: 'none',
      });
    }
    
    
    // Add a class of firefox to the html element if the current browser is firefox
    if ($.browser.mozilla) {
      $('html').addClass('mozilla');
    }
    
  };
  
  
  
  /* -----------------------------------------
    Private Methods
  ----------------------------------------- */
  
  // Un-finished
  function SlideshowInit () {
  
    $('.slideshow').click(function() {
      var slideList = '';
      
      // Toggle sections
      $('.content .slide-hide').toggle();
      // Toggle all sections except the first
      $('.content .slide:not(:first)').toggle();
      
      // Build and add the content menu if it doesn't exist
      if ($('.slide-content').length == 0) {
        // Loop each section
        $('.content .slide').each(function() {
          slideList += '<li><a href="#{0}">{1}</a></li>'.format($(this).attr('id'), $(this).find('h3:first').text());  
        });
        
        // Wrap the list items with an ul
        slideList = '<ul class="slide-content">{0}</ul>'.format(slideList);
        
        $('.navigation ul').after(slideList);
        
        
        // Bind slide content link click events
        $('.slide-content a').click(function() {
          // Toggle all sections except the first
          $('.content .slide:visible').hide();
          $($(this).attr('href')).show();
          
          return false;
        });
      }
      
    });
  
  }
  
  
  // Check if a string is equal to 'undefined', if so return '0', else the string.
  // string s - String to be checked 
  function Sanitize (string, replacement) {

    return s === undefined ? replacement || '' : string;

  }
  
  
  // Extend the String Object
  function StringUtils () {
  
    String.prototype.format = function() {
      var args = arguments;
      return this.replace(/{(\d+)}/g, function(match, number) { 
        return typeof args[number] != 'undefined'
          ? args[number]
          : match
        ;
      });
    };
  
  }
  
  
  // Extend the Array Object
  function ArrayUtils () {

    // indexOf for IE8 and below
    if (!Array.prototype.indexOf) {
        Array.prototype.indexOf = function (what, i) {
            i = i || 0;
            var l = this.length;
            while (i < l) {
                if (this[i] === what) return i;
                ++i;
            }
            return -1;
        };
    }

    // Remove an item from an Array by its value
    Array.prototype.remove = function () {
        var what, a = arguments, l = a.length, ax;
        while (l && this.length) {
            what = a[--l];
            while ((ax = this.indexOf(what)) != -1) {
                this.splice(ax, 1);
            }
        }
        return this;
    };


    // Get all unique values from an Array
    Array.prototype.getUnique = function () {
        var u = {}, a = [];
        for (var i = 0, l = this.length; i < l; ++i) {
            if (this[i] in u)
                continue;
            a.push(this[i]);
            u[this[i]] = 1;
        }
        return a;
    };

  }
            
            
}( window.stripe = window.stripe || {}, jQuery ));