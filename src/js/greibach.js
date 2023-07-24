(function() {
    $(document).ready(function() {
      $('#greibach-form').submit(function(event) {
        event.preventDefault();
        var formData = $(this).serialize();
  
        $.ajax({
          url: '/greibach',
          type: 'POST',
          data: formData,
          success: function(response) {
            $('#wynikGreibach').text(response.wynikGreibach);
          }
        });
      });
    });
  })();
  