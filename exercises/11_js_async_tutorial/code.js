async function getInformationFromInternet() {
  console.log(getElapsedTime(), "[getInformationFromInternet] Before fetch")
  let response = await fetch("https://api.coindesk.com/v1/bpi/currentprice.json")
  console.log(getElapsedTime(), "[getInformationFromInternet] After fetch")
  globalVariableWithBitcoinPrice = await response.json()
  console.log(getElapsedTime(), "[getInformationFromInternet] After json")
  console.log(getElapsedTime(), "[getInformationFromInternet] Value of data = ", globalVariableWithBitcoinPrice.bpi.USD.rate)
}

let globalVariableWithBitcoinPrice = null
console.log(getElapsedTime(), "[main] Starting to execute getInformationFromInternetWithoutAsync()")
getInformationFromInternet()
console.log(getElapsedTime(), "[main] Finished executing getInformationFromInternetWithoutAsync()")
console.log(getElapsedTime(), "[main] Value of globalVariableWithBitcoinPrice = ", globalVariableWithBitcoinPrice)
