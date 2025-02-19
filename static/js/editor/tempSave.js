document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("temp-save-list-btn").addEventListener("click", () => {
        fetch('/temp', {
            method: 'GET'
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Server Error');
            }
            return response.json();
    })
        .then(data => {
            const tempListDiv = document.getElementById("temp-save-list");
            if (data.html) {
                tempListDiv.innerHTML = data.html
            }
        })
        .catch(error => {
            console.error(error);
        });
    });
});

