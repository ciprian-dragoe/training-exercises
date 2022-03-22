let input = document.getElementsByTagName('input')[0];

input.addEventListener('blur', function (event) {
  let n = event.target.value;
  if(n%2 == 0) {
    console.log("Even.");
  } else {
    console.log("Odd");
  }
});