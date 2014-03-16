var $window   = $(window),
    $document = $(document),
    $html     = $(document.documentElement),
    $body     = $(document.body),
    $surface  = $body,
    $content  = $('.content', $surface);
    $navOffSet= 50;
 

// Smooth scrolling for same page anchors
    // =================
    $document.on('click', 'a[href^=#]:not([href=#])', function(e) {
      e.preventDefault();
 
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
      if (target.length) {
        $surface.animate({
          scrollTop: target.offset().top - $navOffSet
        }, 500);
        location.hash = this.hash;
        return false;
      }
    });
 
    // Fix oveflow-scrolling on iOS7
    // =================
    $surface.on('touchstart', function(e) {});