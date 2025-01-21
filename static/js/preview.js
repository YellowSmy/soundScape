window.onload = () => {
    document.getElementById('id_profile_img').addEventListener("change", 
        (event) => {
            const file = event.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = (e) => { document.getElementById('preview').src = e.target.result; }
                reader.readAsDataURL(file);
            }
        });
    }
