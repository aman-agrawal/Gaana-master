function changeView(view)
{
allid = ['genre', 'artist', 'trending', 'radio', 'song_list'] ; 
for(var i = 0 ; i < allid.length ;i++)
{
	document.getElementById(allid[i]).style.display = 'None' ;
}

document.getElementById(view).style.display = "initial" ;
window.scrollTo(0,0);

}

function songsView(cat, name , id)
{
if(cat == "genre")
{
	console.log('hey') ;
    $.ajax({url: "/genre/"+id, success: function(result){
        console.log(result) ;
        embed_view(result);
    }});
}
else if(cat == "artist")
{
    $.ajax({url: "/artist/" + id, success: function(result){
    		console.log(result) ;
    		embed_view(result) ;
    }});
}
else
{


}

}




function embed_view(result)
{

allid = ['genre', 'artist', 'trending', 'radio','song_list'] ; 
for(var i = 0 ; i < allid.length ;i++)
{
	document.getElementById(allid[i]).style.display = 'None' ;
}
document.getElementById('song_list').style.display = "initial" ;
document.getElementById('song_list').innerHTML = result;

window.scrollTo(0,0);
 
}


function playlist_view(name)
{
     $.ajax({url: "/fetch_playlist/" +name , success: function(result){
            console.log(result) ;
            embed_view(result) ;
    }});   
}


function viewTrending()
{
     $.ajax({url: "/trending_songs" , success: function(result){
            console.log(result) ;
            embed_view(result) ;
    }}); 

}

function devotional_view()
{
         $.ajax({url: "/devotional_songs" , success: function(result){
            console.log(result) ;
            embed_view(result) ;
    }}); 
}

function hiphop_view()
{
         $.ajax({url: "/hiphop_songs" , success: function(result){
            console.log(result) ;
            embed_view(result) ;
    }}); 
}