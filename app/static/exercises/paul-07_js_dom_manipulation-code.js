let input = document.getElementById("special-input")
console.log(input)
input.addEventListener('blur', function(event) {
  let n=event.target.value
  if(n%2==0) {
     console.log('even number');
     } else {
     console.log('odd number');
       }
       });