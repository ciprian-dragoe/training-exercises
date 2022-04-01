export async function get(userId, projectId, fileId) {
    const response = await fetch(`/api/users/${userId}/projects/${projectId}/files/${fileId}`)
    const data = await response.json()
    return data
}
