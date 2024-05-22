const getDiv = document.querySelector('#update_header');

getDiv.addEventListener('click', function () {
  const getHeader = document.querySelector('header');
  getHeader.innerText = 'New Header!!!';
});
