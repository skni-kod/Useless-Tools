(function() {
  $(document).ready(function() {
    $('#password-form').submit(function(event) {
      event.preventDefault();
      var formData = $(this).serialize();

      $.ajax({
        url: '/generate-password',
        type: 'POST',
        data: formData,
        success: function(response) {
          $('#password').text(response.password);
        }
      });
    });
  });
})();
