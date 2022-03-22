  console.log(input)
  input.addEventListener('blur', function(event) {
    let n = event.target.value;
    if(n%2==0) {
    console.log('The number in even.');
  } else {
    console.log('The number is odd.');
  }
  });
