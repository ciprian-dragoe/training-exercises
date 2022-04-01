export function show(errorMessage) {
    document.getElementById("code-result").innerHTML = `
        <div class="error">
            ${errorMessage}
        </div>
    `
}
