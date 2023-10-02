(function() {
  var formSubmitted = false; // dodaj zmienną, aby śledzić, czy formularz został już zatwierdzony

  $(document).ready(function() {
    $('#cyk-form').submit(function(event) {
      event.preventDefault();

      if (!formSubmitted) { 
        formSubmitted = true; 

        var formData = $(this).serialize();

        $.ajax({
          url: '/cyk',
          type: 'POST',
          data: formData,
          success: function(response) {
            $('#cyk-table').html(response);
          },
          error: function(xhr, status, error) {
            console.log("Wystąpił błąd: " + error); 
          },
          complete: function() {
            formSubmitted = false; 
          }
        });
      }
    });
  });
})();
(function() {
  var formSubmitted = false; 

  $(document).ready(function() {
    $('#cyk-form').submit(function(event) {
      event.preventDefault();

      if (!formSubmitted) {
        formSubmitted = true; 

        var formData = $(this).serialize();

        $.ajax({
          url: '/cyk',
          type: 'POST',
          data: formData,
          success: function(response) {
            $('#cyk-table').html(response);
          },
          error: function(xhr, status, error) {
            console.log("Wystąpił błąd: " + error); 
          },
          complete: function() {
            formSubmitted = false; 
          }
        });
      }
    });
  });
})();

const submitBtn = document.getElementById('submit-btn');

submitBtn.addEventListener('click', () => {
submitBtn.disabled = true; 
myFunction(); 
});

function myFunction() {

submitBtn.disabled = false; // włącz przycisk po zakończeniu funkcji
}
