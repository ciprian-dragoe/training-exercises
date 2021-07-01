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

async function executeQuery() {
    const response = await fetch("/sql/execute", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ query: textArea.value})
    })
    const data = await response.json()
    console.log(data)
}

document.getElementById("run-query-button").addEventListener("click", executeQuery)