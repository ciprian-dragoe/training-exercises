let box = document.querySelector('#box')

box.addEventListener('mouseover', function(event) {
        event.target.style.backgroundColor = "red";
    });
  
box.addEventListener('mouseout', function(event) {
    event.target.style.backgroundColor = "blue";
    });     