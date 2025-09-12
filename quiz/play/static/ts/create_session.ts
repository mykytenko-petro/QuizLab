import { ajaxGetRequest } from "@ajaxUtils";
import { redirectInApp, getSlug } from "@utils";
import { ICreateSession } from "./types";


function createQuizSession() {
    ajaxGetRequest(
        "/quiz/api/create_single_play_session?quiz_id=" + getSlug(),
        (data : ICreateSession) => {
            redirectInApp("/quiz/play/" + data.session_id)
        }
    )
}

const playButton = document.querySelector(".play") as HTMLButtonElement
playButton.onclick = () => {createQuizSession()}