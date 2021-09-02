document.querySelector("form").addEventListener("submit", (e) => {
    e.preventDefault();
    const name = e.target.name.value;
    const number = parseInt(e.target.number.value, 10);
    const maxNumberExercise = parseInt(document.querySelector("[max]").max, 10);

    if (!name) {
        alert("Name must not be empty!");
        return;
    }

    if (
        !parseInt(number) ||
        parseInt(number) < 1 ||
        parseInt(number) > maxNumberExercise
    ) {
        alert("Number is out of range!");
        return;
    }

    window.location.href = `http://127.0.0.1:5000/exercises/${number}/${name}`;
});
