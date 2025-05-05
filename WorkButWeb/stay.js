function change(){
    const show = document.getElementById("show");
    const btn = document.getElementById("btn");

    if (show.style.display === 'none') {
        show.style.display = 'block';
        btn.textContent = "Display Less";
    } else {
        show.style.display = 'none';
        btn.textContent = "Display Reasons?";
    }
}