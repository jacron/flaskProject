function getxy(pos) {
    let content = document.getElementById('content').value;
    let lines = content.split('\n');
    let p = 0;
    let caretlinenr = 0;
    let lineposstart = 0;
    for (let i = 0; i < lines.length; i++) {
        p += lines[i].length + 1;
        if (p > pos) {
            caretlinenr = i;
            break;
        }
        lineposstart = p;
    }
    let x, y;
    if (caretlinenr > 0) {
        y = caretlinenr;
        x = pos - lineposstart;
    } else {
        y = 0;
        x = pos;
    }
    return `${y+1}:${x+1}`;
}

function showPosition() {
    const pos = document.getElementById('position');
    const content = document.getElementById('content');
    content.onkeyup = () => {
        pos.textContent = getxy(content.selectionStart);
    }
    content.onclick = () => {
        pos.textContent = getxy(content.selectionStart);
    }
    // setInterval(() => {
    //     pos.textContent = content.selectionStart;
    // }, 100)
}

