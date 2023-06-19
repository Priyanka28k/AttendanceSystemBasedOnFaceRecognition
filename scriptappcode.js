document.addEventListener('DOMContentLoaded', function() {
    fetch('/data')
        .then(response => response.json())
        .then(data => {
            // Process the data and update the webpage
            console.log(data);
        })
        .catch(error => console.log(error));
});
