let box = document.getElementById('box');

box.addEventListener('mouseover', function MouseOver() {
  box.style.backgroundColor = 'red';
});
box.addEventListener('mouseout', function MouseOut() {
  box.style.backgroundColor = 'blue';
});
