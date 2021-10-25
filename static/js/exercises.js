document.querySelector("form").addEventListener("submit", (e) => {
    e.preventDefault();
    const name = e.target.name.value.toLowerCase().replaceAll(/\s+/gim, "=");
    const number = e.target.number.value;

    if (!name) {
        alert("You must enter your name before starting the exercise !");
        return;
    }
    window.location.pathname = `/exercises/${number}/${name}`;
});

