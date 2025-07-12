export function getSlug() {
    return window.location.href.split("/").pop()
}