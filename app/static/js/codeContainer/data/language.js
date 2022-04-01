export async function updateFileAndRunCode(languageType, code, userId, fileId) {
    const request = await fetch(`/api/language/${languageType}/update-file-and-run-code`, {
        method: "POST",
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ code, userId, fileId })
    })
    return await request.json()
}

export async function runCode(languageType, code) {
    const request = await fetch(`/api/language/${languageType}/run-code`, {
        method: "POST",
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ code })
    })
    return await request.json()
}
