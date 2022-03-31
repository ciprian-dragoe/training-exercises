const sqlCodeInputElement = document.querySelector("[data-language=sql]")
const sqlCodeExecuteElement = document.querySelector("[data-execute-language=sql]")

sqlCodeExecuteElement.addEventListener("click", (event) => {
  const formattedSql = sqlFormatter.format(sqlCodeInputElement.value, {
    language: "postgresql",
    uppercase: true,
  });
  sqlCodeInputElement.value = formattedSql + "\n"
})
