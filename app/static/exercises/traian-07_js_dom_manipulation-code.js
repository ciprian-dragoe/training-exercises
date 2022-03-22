let input = document.getElementById('special-input')
 
input.addEventListener('blur', function(event) {
  let n = event.target.value
  if(n%2==0) {
    console.log('the number is even');
    } else {
      console.log('the number is odd');
      }
  });    
    


