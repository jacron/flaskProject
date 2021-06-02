inputfocus = () => {
    // console.log('input focus')
}

function strip_query(s) {
    const parts = s.split('?')
    if (parts.length > 1) {
        return parts[0]
    } else {
        return s
    }
}

inputblur = (type, nr, name, value) => {
    console.log(type, nr, name, value) //"St" 6 "St/landing_date" "20"
    const href = strip_query(document.location.href)
    document.location.href = href + `?type=${type}&nr=${nr}&name=${name}&value=${value}`
}