

function cargarDatos(){
  var myjson;
$.getJSON("http://localhost:8000/maininfo/", function(json){
    myjson = json;
    $("#infoname").text(json[0].name);
    $("#birthday").text(json[0].birthday);
    $("#adress").text(json[0].adress);
    $("#phonenum").text(json[0].phonenum);
}),

$.getJSON("http://localhost:8000/experienceinfo/", function(json){
  comments = json;
    var table ="<h3><br><center><table class ='info-box'>" +
             "<tr>" +
             "<th class='tg-yw4l'>Company</th>" +
             "<th class='tg-yw4l'>Position</th>" +
             "<th class='tg-yw4l'>Dates</th>" +
             "<th class='tg-yw4l'>Description</th>" +
             "</tr>";
             //$("#comments").append(tableHeader);

             //Append the rows of the response
             comments.forEach(function(comment){
               table = table + "<tr>" +
               "<td>"+ comment.company +"</td>" +
               "<td>"+ comment.position +"</td>" +
               "<td>"+ comment.dates +"</td>" +
               "<td>"+ comment.description +"</td>" +
               "</tr>";
             })

             table = table + "</table></center></h3>";

             $("#experienceinfo").append(table);
}),


$.getJSON("http://localhost:8000/skillsinfo/", function(json){
  comments = json;
    var table ="<h3><br><center><table class ='info-box'>" +
             "<tr>" +
             "<th class='tg-yw4l'>Tech </th>" +
             "<th class='tg-yw4l'>Experience Time</th>" +
             "</tr>";
             //$("#comments").append(tableHeader);

             //Append the rows of the response
             comments.forEach(function(comment){
               table = table + "<tr>" +
               "<td>"+ comment.technology +"</td>" +
               "<td>"+ comment.timeskill +"</td>" +
               "</tr>";
             })

             table = table + "</table></center></h3>";

             $("#skillsinfo").append(table);
}),


$.getJSON("http://localhost:8000/proyectsinfo/", function(json){
  comments = json;
    var table ="<h3><br><center><table class ='info-box'>" +
             "<tr>" +
             "<th class='tg-yw4l'>Name</th>" +
             "<th class='tg-yw4l'>Position</th>" +
             "<th class='tg-yw4l'>Description</th>" +
             "<th class='tg-yw4l'>Technologies involved</th>" +  
             "</tr>";
             //$("#comments").append(tableHeader);

             //Append the rows of the response
             comments.forEach(function(comment){
               table = table + "<tr>" +
               "<td>"+ comment.proyectname +"</td>" +
               "<td>"+ comment.positionproy +"</td>" +
               "<td>"+ comment.descriptionproy +"</td>" +
               "<td>"+ comment.techinvolved +"</td>" +
               "</tr>";
             })

             table = table + "</table></center></h3>";

             $("#proyectsinfo").append(table);
}),

$.getJSON("http://localhost:8000/comments/", function(json){
  comments = json;
             //$("#comments").append(tableHeader);
  var table;
             //Append the rows of the response
             comments.forEach(function(comment){
              table = table +
              "<div>" + "<h3> Id: "+ comment.id +"</h3>"+
               "<div>" + "<h3> Name: "+ comment.commentname +"</h3>"+
               "<h3> Comment: " + comment.comment + "</h3>"+
                  "<button type='delete' onclick='deleteData("+ comment.id+ ")'>Delete</button></div>";                  ;
             })


             $("#comments").append(table);
});


 
}

function getFormData(){ 
var commentname=document.getElementById('commentname').value;
var comment=document.getElementById('comment').value;

$.ajax({
                 type:"POST",
                 url:"http://localhost:8000/comments/",
                 data: {
                        'commentname': commentname,
                        'comment': comment // from form
                        },
                 success: function(){
                     location.reload();
                 }
/* some other fields */
/* now call ur function by passing the above values */
});

}


function deleteData(commentid){ 
$.ajax({
                 type:"delete",
                 url:"http://localhost:8000/comments/" + commentid+ "/" ,
                 success: function(){
                     window.location.replace("landingdel.html");
                 }
/* some other fields */
/* now call ur function by passing the above values */

});
}
function getCommentId(commentid){ 
var cmid = commentid;
cmid = JSON.stringify(cmid);
cmid = btoa(cmid);
localStorage.setItem('_commentid', cmid);
window.location.replace("/home/canto/Documents/efficenty/updatecomment.html");


}

function loadData(commentname,comment) {
   var commentid = localStorage.getItem('_commentid');
   if (!commentid) return false;
   localStorage.removeItem('_commentid');
   //decodes a string data encoded using base-64
   commentid = atob(commentid);
   //parses to Object the JSON string
   commentid = JSON.parse(commentid);
   //do what you need with the Object



   $.ajax({
                 type:"PUT",
                 url:"http://localhost:8000/comments/" + commentid +"/",
                 data: {
                        'commentname': commentname,
                        'comment': comment, // from form
                        },
                  dataType: "json",
                 success: (result) => {
                console.log("success")
            },
/* some other fields */
/* now call ur function by passing the above values */
});

}


