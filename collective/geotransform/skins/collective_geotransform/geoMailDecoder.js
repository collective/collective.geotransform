$(document).ready( function() {
    // Decode the geomailaddress span to extract the mail
    $("span.geomailaddress").each(function(i){
        encodedMail = $(this).text();
        decodedMail = $.base64.decode(encodedMail);
        $(this).replaceWith(decodedMail);
    });
    // Decode the geomailto href attribute to extract the mail
    $("a[href^=geomailto]").each(function(i){
        $(this).attr('class', 'link-mailto');
        encodedMail = $(this).attr('href').replace("geomailto:","");
        decodedMail = $.base64.decode(encodedMail);
        $(this).attr('href', 'mailto:'+decodedMail);
    });
});
