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

function getposition(nr, lines, position) {
    let p = 0;
    for (let i = 0; i < nr - 1; i++) {
        p += lines[i].length + 1;
    }
    return p + position;
}

inputchange = (nr, position, alignment, len, value) => {
    // console.log('changing nr:' + nr);
    let content = document.getElementById('content');
    let text = content.value;
    let lines = text.split('\n');
    let pos = getposition(nr, lines, position);
    let toInsert = fill(value, alignment, len);
    content.selectionStart = pos;
    content.selectionEnd = pos + len;
    lines[nr - 1] = insert(lines[nr - 1], position, alignment, len, value);
    content.innerHTML = lines.join('\n');
    content.focus();
    content.setSelectionRange(pos, pos + len);
}
