async function startFetch() {
  console.log(getElapsedTime(), "[startFetch] Before fetch")
  let url = "https://api.coindesk.com/v1/bpi/currentprice.json"
  let response = await fetch(url)
  console.log(getElapsedTime(), "[startFetch] After fetch")
  globalVariable = await response.json()
  console.log(getElapsedTime(), "[startFetch] After json")
  console.log(getElapsedTime(), "[startFetch] Value of data = ", globalVariable)
}

let globalVariable = null
console.log(getElapsedTime(), "[main] Starting to execute startFetch()")
startFetch()
console.log(getElapsedTime(), "[main] Finished executing startFetch()")
console.log(getElapsedTime(), "[main] Value of globalVariable = ", globalVariable)
