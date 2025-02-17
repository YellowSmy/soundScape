document.addEventListener("DOMContentLoaded", function () {
    const modalLinks = document.querySelectorAll(".modal-input");
    const modals = document.querySelectorAll(".modal-container");

    // 모달 열기 이벤트
    modalLinks.forEach(link => {
        link.addEventListener("click", function (event) {
            event.preventDefault(); // 페이지 이동 방지
            const modalId = this.getAttribute("data-modal");
            document.getElementById(modalId).style.display = "block";
        });
    });

    // 모달 닫기 이벤트
    modals.forEach(modal => {
        modal.addEventListener("click", function () {
            this.style.display = "none";
        });

        // 닫기 버튼 클릭 시 닫기
        modal.querySelector(".close-btn").addEventListener("click", function (event) {
            event.stopPropagation();
            modal.style.display = "none";
        });
    });
});