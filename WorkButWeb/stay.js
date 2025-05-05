function change(){
    const show = document.getElementById("show");
    const btn = document.getElementById("btn");

    if (show.style.display === 'none') {
        show.style.display = 'block';
        btn.textContent = "Display Less";
    } else {
        show.style.display = 'none';
        btn.textContent = "Get in contact with travel agency?";
    }
}


function flip(){
    const im1 = document.getElementById("pstr");
    const im2 = document.getElementById("bridge");

    im1.style.display = 'none';
    im2.style.display = 'block';
}
function flipagain(){
    const im1 = document.getElementById("pstr");
    const im2 = document.getElementById("bridge");

    im2.style.display = 'none';
    im1.style.display = 'block';
}