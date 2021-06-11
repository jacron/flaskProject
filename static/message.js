const DELAY = 4000

function setMessage(s) {
    const topline = document.getElementById('topline');
    topline.style.display = 'block';
    const msg = document.getElementById('message');
    msg.textContent = s;
}

function clearMessage() {
    const topline = document.getElementById('topline');
    topline.style.display = 'none';
}

function getCookie(name) {
  const decodedCookie = decodeURIComponent(document.cookie);
    const entries = decodedCookie.split(';');
    for (let entry of entries){
        [name_, value] = entry.split('=');
        if (name === name_) {
            return value;
        }
    }
    return '';
}

showMessage = () => {
    const message = getCookie('msg');
    if (message.length > 0) {
        setMessage(message);
        setTimeout(() => {
            clearMessage();
        }, DELAY)
        document.cookie='msg=';
    } else {
        clearMessage();
    }

}

displayMessage = s => {
    setMessage(s);
    setTimeout(() => {
        clearMessage();
    }, DELAY)
}