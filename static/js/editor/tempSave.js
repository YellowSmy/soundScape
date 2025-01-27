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

                //close
                const closeBtn = document.getElementById("close-btn")
                const showBtn =  document.getElementById("temp-save-list-btn")


                closeBtn.addEventListener("click", () => {
                    tempListDiv.style.display = "none";
                    showBtn.style.display = "block"; 
                });

                showBtn.style.display = "none";
                tempListDiv.style.display = "block"; 
            }
        })
        .catch(error => {
            console.error(error);
        });
    });
});

