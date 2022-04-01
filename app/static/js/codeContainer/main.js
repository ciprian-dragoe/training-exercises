import * as projects from "./data/projects";
import * as files from "./data/files";
import * as codeRunner from "./controllers/codeRunner/codeRunner";
import * as environmentInitializer from "./controllers/environmentInitializer/environmentInitializer";

function main() {
    const projectId = window.location.href.split("/")[6]
    const userId = window.location.href.split("/")[4]
    const project = projects.get(userId, projectId)
    const fileEntryPoint = files.get(userId, projectId, project.entry_point_file_id)
    codeRunner.attachEventListener(project, fileEntryPoint)
    environmentInitializer.initialize(file)
}

main()
