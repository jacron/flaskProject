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

save = () => {
    const form = document.getElementById('saveForm');
    const url = '/exchange';
    const data = {
        content: form.content.value,
        filename: form.filename.value
    }
    // console.log(data.content);
    postAjax(url, data, result => {
        displayMessage(result);
    });
}