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
