toggleTable = nr => {
    let table = document.getElementById('nr_' + nr)
    if (table.style.display === 'none') {
        table.style.display = 'block';
    } else {
        table.style.display = 'none';
    }
}

notify_saved = () => {
    const filename = document.getElementById('filename').textContent;
    document.cookie =  'msg=saved: ' + filename;
}

onbodyload = () => {
    showMessage();
    showPosition();
}