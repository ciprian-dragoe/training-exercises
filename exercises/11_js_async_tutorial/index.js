let start = new Date();

function getElapsedTime() {
    let difference = new Date() - start;
    let remainder = Math.floor(difference / 10);
    let amount = 1;
    while (remainder > 0) {
        remainder = Math.floor(remainder / 10);
        amount++;
    }
    let result = difference.toString();
    for (let i = amount; i < 8; i++) {
        result = " " + result;
    }
    return result + "ms -";
}

function runJs (code, result) {
    eval(code)
}
