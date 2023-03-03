(function() {
    $(document).ready(function() {
      $('#greibach-form').submit(function(event) {
        event.preventDefault();
        var formData = $(this).serialize();
  
        $.ajax({
          url: '/greibach-convert',
          type: 'POST',
          data: formData,
          success: function(response) {
            $('#wynik').text(response.wynik);
          }
        });
      });
    });
  })();
  