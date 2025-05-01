function change(){
    if(document.getElementById("btn").style.display != 'block'){
        document.getElementById("show").style.display = 'block'; document.getElementById("btn").textContent = "Display less"
    }else{
        document.getElementById("show").style.display = 'none'
    }
}