define([
  'jquery',
  'jquery_base64',
], function($, base64) {
  'use strict';

    $(document).ready( function() {
        // Decode the geomailaddress span to extract the mail
        $("span.geomailaddress").each(function(i){
            var encodedMail = $(this).text();
            var decodedMail = $.base64.decode(encodedMail);
            $(this).replaceWith(decodedMail);
        });
        // Decode the geomailto href attribute to extract the mail
        $("a[href^=geomailto]").each(function(i){
            $(this).attr('class', 'link-mailto');
            var encodedMail = $(this).attr('href').replace("geomailto:","");
            var decodedMail = $.base64.decode(encodedMail);
            $(this).attr('href', 'mailto:'+decodedMail);
        });
    });

});

