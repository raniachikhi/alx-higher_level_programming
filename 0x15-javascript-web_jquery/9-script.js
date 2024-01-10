$(document).ready(function () {
  const salutUri = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  const $helloElement = $('DIV#hello');

  function getSalut () {
    return $.get({
      url: salutUri,
      dataType: 'json'
    });
  }

  getSalut().then((res) => {
    $helloElement.text(res.hello);
  });
});
