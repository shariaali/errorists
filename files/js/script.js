var socket = io();

var logged_in = false;

var projects;
function project_form(){
    var team_name = document.getElementById("name").value;
    var project_name = document.getElementById("project-name").value;
    var project_image = document.getElementById("project-image").files[0];
    var project_skills = document.getElementById('project-skills').value;
    var project_desc = document.getElementById('project-message').value;
    
    var fileReader = new FileReader();
    fileReader.readAsArrayBuffer(project_image);
    fileReader.onload = () => {
        img = fileReader.result;
        var data = {"name":project_name,"image":img, "description":project_desc, "skills":project_skills, "collaborators":[]};
        console.log("Sending data");
        socket.emit('create_project', data);
        console.log("Data sent!");
        console.log(data);
        }
    
}

socket.on('create_project', function(state){
    alert("Data has been succesfully added!");
});

function get_projects(){
    socket.emit('load_projects');
}

socket.on('load_projects', function(data){

});

socket.on('logged_in', function(state){
    logged_in = true;
});

function signupClick(){
    username = document.getElementById("signame").value;
    password = document.getElementById("signpw").value;
    socket.emit('signup', {"username":username, "password":password});
    console.log({"username":username, "password":password});
}

function loginClick(){
    username = document.getElementById("loginame").value;
    password = document.getElementById("loginpw").value;
    socket.emit('login', {"username":username, "password":password});
}

function openForm(evt, tabName){
    //swaps between two tab-contents
    var login = document.getElementById("login_form")
    var signup = document.getElementById("signup_form")
    if (tabName =="SignUp"){
        console.log("Clicked Signup");
        login.style.display= "none";
        signup.style.display= "block";
    }
    else if (tabName =="Login"){
        console.log("Clicked Login");
        login.style.display= "block";
        signup.style.display= "none";
    }
}