$(function() {
  var has_answered = function() {
    if (!$('input:checked').length) {
      alert('Please provide an answer!');
      return false;
    }
    return true;
  }

  $('#submit').on('click', function(ev) {
    ev.preventDefault();
    if (has_answered()) {
      var answer = $('input:checked').val() === 'right' ? 1 : 0;
      $.ajax({
        url: '/_answer_linda',
        type: 'POST',
        data: {'answer': answer}
      }).done(function() {
        $('.content').replaceWith('<h2>Thanks! Your code is <b>7E93<b></h2>');
      });
    }
  });
});
