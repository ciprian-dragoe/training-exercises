document.getElementById("special-input");
let input = document.getElementById("special-input");
input.addEventListener("blur", function(event){
let num = event.target.value;
if (num % 2 == 0) {
  console.log('even number');
}else{
  console.log('odd number');
}
  
});