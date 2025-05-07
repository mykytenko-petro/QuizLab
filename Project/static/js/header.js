let header = document.querySelector("#header");

function setHeader() {
    const username = sessionStorage.getItem("username")

    console.log(username);

    if (username) {
        header.innerHTML = `
        <nav>
            <a href="/">Home</a>
            <a href="/logout">logout</a>
            <a href="/users/${username}">${username}</a>
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