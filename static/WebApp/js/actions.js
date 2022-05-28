$("#btn_home").click ((event)=>{
    window.location="/";
})
$("#btn_login").click ((event)=>{
    window.location='/login';
})
$("#btn_logout").click ((event)=>{
    window.location='/logout/';
})
$("#btn_register").click ((event)=>{
    window.location='/user_create';
})
$("#btn_indietro").click ((event)=>{
    history.go(-1);
})
$("#btn_playlist_home").click ((event)=>{
    window.location='/playlist/home/'
})
$("#btn_playlist_list").click ((event)=>{
    window.location='/playlist/list/'
})
$("#btn_playlist_create").click ((event)=>{
    window.location='/playlist/create/'
})
$("#btn_song_list").click ((event)=>{
    window.location='/playlist/song_list/'
})