document.querySelector("form").addEventListener("submit", (e) => {
    e.preventDefault();
    const name = e.target.name.value
        .toLowerCase()
        .normalize('NFKD')
        .replace(/[^\w]/g, '')
        .replaceAll(/\s+/gim, "=")
        .replaceAll(/-/g, "=");
    const number = e.target.number.value;

    if (!name) {
        alert("You must enter your name before starting the exercise !");
        return;
    }
    window.location.pathname = `/exercises/${number}/${name}`;
});

