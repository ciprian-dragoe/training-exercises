console.log(11)
let timerID
const textArea = document.getElementById("sql")

textArea.addEventListener("input", (e) => {
    timerID && clearTimeout(timerID)

    timerID = setTimeout(() => {
        const formattedSql = sqlFormatter.format(textArea.value, {
            language: "postgresql",
            uppercase: true,
          });
        textArea.value = formattedSql
    }, 1500)
})

document.getElementById("run-query-button").addEventListener("click", () => {
    console.log(textArea.value)
})