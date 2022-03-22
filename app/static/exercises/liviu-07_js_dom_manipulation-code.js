let input = document.getElementsByTagName('input')[0];
console.log('input');
input.addEventListener('blur',function(event){
  let n = event.target.value;
  if(n%2 == 0){
  console.log('Number is even');}
  else {
  console.log('Number is odd');}
});