function fill(value, alignment, len) {
    let rest = len - value.length;
    let spaces = '';
    while (rest-- > 0) {
        spaces += ' ';
    }
    if (alignment === 'right') {
        return spaces + value;
    } else {
        return value + spaces;
    }
}

function insert(line, position, alignment, len, value) {
    return line.substr(0, position) + fill(value, alignment, len) +
        line.substr(position + len);
}

inputchange = (nr, position, alignment, len, value) => {
    // console.log('changing nr:' + nr);
    let content = document.getElementById('content').value;
    let lines = content.split('\n');
    lines[nr - 1] = insert(lines[nr - 1], position, alignment, len, value);
    document.getElementById('content').innerHTML = lines.join('\n');
}

toggleTable = nr => {
    let table = document.getElementById('nr_' + nr)
    if (table.style.display === 'none') {
        table.style.display = 'block';
    } else {
        table.style.display = 'none';
    }
}

zoom = modus => {
    const text = document.getElementById('content');
    console.log(text);
    const textStyle = document.getElementById('content').style;
    console.log(textStyle.fontSize);
    const currentFontSize = parseInt(textStyle.fontSize);
    console.log(currentFontSize);
    let newFontSize;
    if (modus === 'in') {
        newFontSize = +currentFontSize + 1;
    }
    if (modus === 'out') {
        newFontSize = +currentFontSize - 1;
    }
    textStyle.fontSize = newFontSize.toString() + 'px';
    console.log(textStyle.fontSize);
}

notify_saved = () => {
    const filename = document.getElementById('filename').textContent;
    document.cookie =  'msg=saved: ' + filename;
}

onbodyload = () => {
    showMessage();
}