export function getSlug() {
    return window.location.href.split("/").pop()
}

export function redirectInApp(url) {
    window.location.replace(`${url}`)
}