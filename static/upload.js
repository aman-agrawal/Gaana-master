

function upload_song()
{
var form = document.getElementById('the-form');
  // form.onsubmit = function(e){
  //e.preventDefault();

  var formData = new FormData(form);

  var fileInput = document.getElementById('the-file');
  var file = fileInput.files[0];

  var imgInput = document.getElementById('the-img');
  var image = imgInput.files[0];

  formData.append('img', image);
  formData.append('file' , file);

  // console.log(formData) ;  
  if(!formData.get('cat') || !formData.get('art') || !formData.get('name') || !file || !image)
  {
    $("#upload_status").html("<b>!..Fill all fields..!</b>");
    return ;
  }
   name = formData.get('name') ; 
   formData.set('name' ,name.replace(/</g, "&lt;").replace(/>/g, "&gt;")) ;
  $("#upload_status").html("<b>!..uploading!</b>");

  var xhr = new XMLHttpRequest();
  // Add any event handlers here...
  xhr.open('POST', '/upload', true);

  xhr.onreadystatechange = function () {
   if(xhr.readyState === 4 && xhr.status === 200) {
    var data = JSON.parse(xhr.responseText) ;
    console.log(data) ;
    $("#upload_status").html("");
    if(data.status == -1) 
    {
      alert("<>error : song already exists") ;
    }
    else if(data.status >= 0)
    {
      alert("song " + data.s_name+" successfully uploaded "); 
      $("#close_button").trigger();
    }
  }
}

  xhr.send(data);
  return false; // To avoid actual submission of the form

// }

}




// $("#the-form").submit(function(e) {
//     e.preventDefault();    
//     var formData = new FormData(this);

//   var fileInput = document.getElementById('the-file');
//   var file = fileInput.files[0];

//   var imgInput = document.getElementById('the-img');
//   var image = imgInput.files[0];

//   formData.append('img', image);
//   formData.append('file' , file);


//     $.ajax({
//         url: '/upload',
//         type: 'POST',
//         data: formData,
//         success: function (data) {
//             alert(data)
//         },
//         cache: false,
//         contentType: false,
//         processData: false
//     });
//     // return false;
// });


