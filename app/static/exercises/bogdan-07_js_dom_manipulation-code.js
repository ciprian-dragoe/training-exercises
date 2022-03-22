const input = document.querySelector('input');
let result = document.querySelector('#code-result');

input.oninput = takeInput;

function takeInput(e) {
  if(e.target.value.length == 0) { 
  result.innerText = "Null is not a number";
  } else if(e.target.value % 2 == 0) {
    result.innerText = " # is Even";
  } else {
  result.innerText = "# is Odd";
  }
 }

