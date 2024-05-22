const getDiv = document.querySelector('#toggle_header');

getDiv.addEventListener('click', function () {
  const headCol = document.querySelector('.green, .red');
  headCol.classList.toggle('red');
  headCol.classList.toggle('green');
});
