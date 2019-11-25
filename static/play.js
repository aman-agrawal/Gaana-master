function play(id )
{
	console.log(id);
	url = '/download_files/mp3/' + id ;  
	audio = document.getElementById("play") ; 
  audio.src = url;
  audio.controls = "controls";
  audio.load();
  audio.play();
  audio.addEventListener('ended',function(){      
  var song = document.getElementsByClassName('audio_button') ; 
  });	
}


var playlist_id ; 
var playlist_song;

function add_to_modal(id, songname)
{
	playlist_id = id ; 
	playlist_song = songname ; 
	$.ajax({url: "/playlist_names", success: function(result){
    console.log(result) ;
    document.getElementById('p_name_list').innerHTML = result;
    }});
}
 

function playlist()
{
	var id = playlist_id ; 
	var songname = playlist_song ;
	p_name = document.getElementById("new_playlist").value ; 
    if(p_name == "")
    {
    	var e = document.getElementById("playlist_select") ; 
    	p_name = e.options[e.selectedIndex].value;
    } 
    console.log(p_name) ; 

  var xhr = new XMLHttpRequest();
  xhr.open('GET', '/add_to_playlist/'+ id+'/' + songname + "/"  + p_name, true);
  xhr.onreadystatechange = function () {
  if(xhr.readyState === 4 && xhr.status === 200) {
    console.log(xhr.responseText);
    data  = JSON.parse(xhr.responseText) ; 
    if(data.msg == "success")
    { 
    	alert("successfull"); 	// show_template(id ,songname); 
    
    $.ajax({url: "/playlist_names1", success: function(result){
    console.log(result) ;
    document.getElementById('dynamic_playlist').innerHTML = result;
    }});


    }
    else alert("error : song already exists in your playlist")


  }
}
xhr.send() ;

}

