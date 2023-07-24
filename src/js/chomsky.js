(function() {
    $(document).ready(function() {
      $('#chomsky-form').submit(function(event) {
        event.preventDefault();
        var formData = $(this).serialize();
  
        $.ajax({
          url: '/chomsky',
          type: 'POST',
          data: formData,
          success: function(response) {
            $('#wynikChomsky').text(response.wynikChomsky);
          }
        });
      });
    });
  })();
  