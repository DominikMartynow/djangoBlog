function popup_wrapper_button_open() {
    const popup = document.querySelector('.post_likes_wrapper');
    popup.style.display = "block";
    
    console.log("Popup open")
}

function popup_wrapper_button_close(){
    const popup = document.querySelector('.post_likes_wrapper');
    popup.style.display = "none";
}