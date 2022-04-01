import * as projects from "./data/projects.js";
import * as files from "./data/files.js";
import * as codeRunner from "./controllers/codeRunner/codeRunner.js";
import * as environmentInitializer from "./controllers/environmentInitializer/environmentInitializer.js";
import * as codeViewer from "./controllers/codeViewer.js";

async function main() {
    const projectId = window.location.href.split("/")[6]
    const userId = window.location.href.split("/")[4]
    const project = (await projects.get(userId, projectId)).project
    const fileEntryPoint = (await files.get(userId, projectId, project.entry_point_file_id)).file
    codeRunner.attachEventListener(project, fileEntryPoint)
    environmentInitializer.initialize(fileEntryPoint)
    codeViewer.loadFile(fileEntryPoint)
}

(async () => {
  await main();
})();
