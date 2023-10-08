var socket = io();


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