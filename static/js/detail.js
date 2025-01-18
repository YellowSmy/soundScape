document.addEventListener('DOMContentLoaded', function () {
    const replyButtons = document.querySelectorAll('.reply-button');

    replyButtons.forEach(button => {
        button.addEventListener('click', function () {

            const parentId = this.getAttribute('parent-id');

            const formDiv = document.getElementById('reply-form-' + parentId);
            formDiv.style.display = formDiv.style.display === 'none' ? 'block' : 'none';
        });
    });

});


