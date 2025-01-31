// Toast UI Editor
document.addEventListener('DOMContentLoaded', () => {
    const textarea = document.querySelector('#toast-editor');
    if (!textarea) {
        console.error("Error: #toast-editor not found");
        return;
    }

    if (textarea.value == "None") {
        initalText = ""
    } else {
        initalText = textarea.value
    }

    const editor = new toastui.Editor({
        el: document.querySelector('#editor'),
        height: '400px',
        initialEditType: 'wysiwyg',
        previewStyle: 'vertical',
        initialValue: initalText,
    });

    document.querySelector('#content-form').addEventListener('submit', () => {
        textarea.value = editor.getMarkdown();
    });
});


//Theme Settings
function changeTheme(theme) {
    fetch(`/change-theme/?theme=${theme}`)
    .then(response => response.json())
    .then(data => {
        const link = document.getElementById("stylesheet-theme");
        link.setAttribute('href', data.css_path)
        alert(`${theme}으로 전환`);
    })
    .catch(error => {
        console.error(error);
    });

    //set theme in form value
    document.getElementById("id_theme").value = theme;
}

