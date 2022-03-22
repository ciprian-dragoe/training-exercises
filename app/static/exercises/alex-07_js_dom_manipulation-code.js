
let input = document.getElementById('special-input');
input.addEventListener('change', function(event){
  let n = event.target.value;
  if(n%2==0) {
    console.log('the Number Is Even ');
    } else {
    console.log('the  Number Is Odd') ;
    }
    
  });