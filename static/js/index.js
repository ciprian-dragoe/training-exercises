document.getElementsByTagName("button")[0].addEventListener("click", () => {
  const name = document.getElementsByName("name")[0].value
  const exerciseNumber = document.getElementsByName("exercise-number")[0].value
  const maxNumberExercise = parseInt(document.querySelector("[max]").max)
  if (!name) {
    alert("Name must not be empty!")
    return
  }
  
  if (!parseInt(exerciseNumber) || parseInt(exerciseNumber) < 1 || parseInt(exerciseNumber) > maxNumberExercise) {
    alert("Number is out of range!")
    return
  }

  window.location.href = `http://127.0.0.1:5000/exercises/${exerciseNumber}/${name}`
})