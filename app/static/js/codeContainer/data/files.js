export async function get(userId, projectId, fileId) {
    const response = fetch(`/api/user/${userId}/projects/${projectId}/files/${fileId}`)
    const data = response.json()
    return data.files
}
