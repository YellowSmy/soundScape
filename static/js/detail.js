document.addEventListener('DOMContentLoaded', function () {
    // reply-btn
    const replyButtons = document.querySelectorAll('.reply-button');

    replyButtons.forEach(button => {
        button.innerHTML = "답글"; 

        button.addEventListener('click', function () {
            const parentId = this.getAttribute('parent-id');
            const formDiv = document.getElementById('reply-form-' + parentId);

            // 답글 폼 보이기/숨기기
            if (formDiv.style.display === 'none' || formDiv.style.display === '') {
                formDiv.style.display = 'flex';
                this.innerHTML = "닫기"; 
            } else {
                formDiv.style.display = 'none';
                this.innerHTML = "답글";
            }
        });
    });
});



