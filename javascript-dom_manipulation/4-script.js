const getDiv = document.querySelector('#add_item');

getDiv.addEventListener('click', function () {
  const getUlClass = document.querySelector('.my_list');
  const createLi = document.createElement('li');
  createLi.appendChild(document.createTextNode('Item'));
  getUlClass.appendChild(createLi);
});
