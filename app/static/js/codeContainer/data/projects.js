export async function get(userId, projectId) {
    const response = await fetch(`/api/users/${userId}/projects/${projectId}`)
    const data = await response.json()
    return data
}
