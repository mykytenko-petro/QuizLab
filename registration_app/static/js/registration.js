const hiddenInput = document.querySelector("#user_session");

getSession = () => {
    hiddenInput.value = sessionStorage.getItem("user_session");
};

getSession();