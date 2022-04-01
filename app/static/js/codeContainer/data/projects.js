export async function get(userId, projectId) {
    const response = fetch(`/api/user/${userId}/projects/${projectId}`)
    const data = response.json()
    return data.project
}
