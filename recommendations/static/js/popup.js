function showPopup(title, year, rating, imdbID, plot, director) {
    document.getElementById('popup-title').innerText = title;
    document.getElementById('popup-year').innerText = 'Year: ' + year;
    document.getElementById('popup-rating').innerText = 'IMDB Rating: ' + rating;
    document.getElementById('popup-plot').innerText = 'Plot: ' + plot;
    document.getElementById('popup-director').innerText = 'Director: ' + director;
    document.getElementById('popup-watch').href = 'https://www.imdb.com/title/' + imdbID;
    document.getElementById('movie-popup').style.display = 'block';
}

function hidePopup() {
    document.getElementById('movie-popup').style.display = 'none';
}
    
