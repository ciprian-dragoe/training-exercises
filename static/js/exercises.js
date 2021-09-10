document.querySelector("form").addEventListener("submit", (e) => {
    e.preventDefault();
    const name = e.target.name.value.toLowerCase().replace(/\s+/gim, "-");
    const number = e.target.number.value;

    if (!name) {
        alert("Name must not be empty!");
        return;
    }

    window.location.href = `http://127.0.0.1:5000/exercises/${number}/${name}`;
});
