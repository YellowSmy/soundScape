document.addEventListener('DOMContentLoaded', function () {
    //reply-btn
    const replyButtons = document.querySelectorAll('.reply-button');

    replyButtons.forEach(button => {
        button.addEventListener('click', function () {

            const parentId = this.getAttribute('parent-id');

            const formDiv = document.getElementById('reply-form-' + parentId);
            formDiv.style.display = formDiv.style.display === 'none' ? 'block' : 'none';
        });
    });

});

//toggle function
function toggle(id) {
    const contentDiv = document.getElementById(id);

    if (contentDiv.style.display == "none") {
        contentDiv.style.display = "block";
    } else {
        contentDiv.style.display = "none";
    }
}



