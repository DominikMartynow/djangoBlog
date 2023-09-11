function popup_likes_list_wrapper_button_open() {
    const popup = document.querySelector('.post_likes_wrapper');
    popup.style.display = "block";
    
    console.log("Popup open")
}

function popup_likes_list_wrapper_button_close(){
    const popup = document.querySelector('.post_likes_wrapper');
    popup.style.display = "none";
}

function popup_users_data_edit_button_open() {
    const popup = document.querySelector('.usersDataEditWrapper');
    popup.style.display = "block";
    const popup2 = document.querySelector('.usersDataEditWrapperBg');
    popup2.style.display = "block";
    
    console.log("Popup open")
}

function popup_users_data_edit_button_close(){
    const popup = document.querySelector('.usersDataEditWrapper');
    popup.style.display = "none";
    const popup2 = document.querySelector('.usersDataEditWrapperBg');
    popup2.style.display = "none";
}