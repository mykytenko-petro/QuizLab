let header = document.querySelector("#header");

function delCookies() {
    sessionStorage.clear()
}

function setHeader() {
    const username = sessionStorage.getItem("username")

    console.log(username);

    if (username) {
        header.innerHTML = `
        <nav>
            <a href="/">Home</a>
            <a href="/logout" onclick="delCookies()">logout</a>
            <a href="/profile">${username}</a>
        </nav>
        `;
    } else {
        header.innerHTML = `
        <nav>
            <a href="/">Home</a>
            <a href="/registration">registration</a>
            <a href="/login">login</a>


        </nav>
        `;
    };
};

setHeader();
