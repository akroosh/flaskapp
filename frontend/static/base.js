window.onload = function(){
  fetch('http://localhost:5000/movies/pagin?limit=2&offset=0')
    .then((response)=>{
      return response.json();
    })
    .then((data)=>{
      for(let i = 1; i<=data.page_count; i++){
          const pageItem = document.createElement("li"); 
          pageItem.innerText = i;
          pageContainer.appendChild(pageItem)}
      getMovies(data.movies)
    })
}

function getMovies(movies){
  const moviesCont = document.querySelector(".movies")
  moviesCont.innerHTML = ''
  movies.forEach(item => {
    moviesCont.insertAdjacentHTML("beforeend",
    `<div class="movie__content">
    <div class="containerr">
        <div class="filmplace">
            <div class="imgss">
                <p><img class="film-img" src="" alt="">
                <div class="film__title">${item.title}</div>
            </div>
            <div class="genre"><span>
                {%for genre in movie.genres%}
                
                    <a href="genre/{{genre.slug}}">{{genre.title}}</a>,
                    
                    {%endfor%}</span>
            </div>
            <div class="film__text">
            <span>${item.description}</span>
            </div>
            
            <div>Year: <span>${item.year}</span></div>
            <div>Country: <span>${item.country}</span></div>

            <a href="{{movie.slug}}" class="button-container">Watch it now</a>
            <div class="m-api">
            <a href="{{movie.slug}}/edit" class="m-edit">edit</a>
            <a href="{{movie.slug}}/delete"class="m-delete" onclick="Delete(this)">delete</a>
            <a href="{{movie.slug}}/upload"class="m-upload">upload</a>

        </div>
    </div>
</div>`)
  })
}

const pageContainer = document.querySelector('.pagesWrapper')
pageContainer.addEventListener('click', (e)=>{
  let activePage
  if(+e.target.innerHTML > 1){
    activePage = +e.target.innerHTML
  }
  else{
    activePage = +e.target.innerHTML - 1
  }
  fetch(`http://localhost:5000/movies/pagin?limit=2&offset=${activePage}`)
  .then((response)=>{
    return response.json();
  })
  .then((data)=>{
    getMovies(data.movies)
  })
})

  