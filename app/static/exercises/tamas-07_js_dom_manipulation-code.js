const result = document.getElementById("code-result");
let input = document.getElementById("special-input");
input.addEventListener('blur', function (event) {
   n = event.target.value;
   if (n % 2 == 0) {
    result.innerHTML="The number is even.";
}else {
    result.innerHTML="The number is odd.";
}
});
   
  