function display(){
    var extra = document.getElementById("extra");
    var button = document.getElementById("dislist");
    if(extra.style.display === "none"){extra.style.display = "block"; button.textContent = "Show Less"
    }else{
        extra.style.display = "none"
        button.textContent= "Display the reasons you should go hunting?"
    }
}
function change(){
    document.getElementById("mamo").style.display = "none"; document.getElementById("mal").style.display = "block"
}