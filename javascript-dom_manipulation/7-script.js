fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(data => {
    let movieDiv = document.getElementById('list_movies');
    data.results.forEach(film => {
      let listTitle = document.createElement('li');
      listTitle.innerText = film.title;
      movieDiv.appendChild(listTitle);
    });
  })
  .catch(error => console.log('Error:', error));
