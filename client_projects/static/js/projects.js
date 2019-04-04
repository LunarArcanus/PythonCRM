"use strict";

// Operations pertaining to data modification

var saveButtons;
var deleteButtons;
var addButton = document.getElementsByClassName("add-button")[0];
var table = document.querySelector("table > tbody");

// Add an event for each save button to update the database record
function addSaveEvents() {
  var projectObject;
  var data;
  var button;
  var xhttp;
  saveButtons = document.getElementsByClassName("save-button");

  for (var i = 0; i < saveButtons.length; i++) {
      button = saveButtons[i];
      button.removeEventListener("click", addSaveEvents);

      button.addEventListener("click", function(event) {
          projectObject = {
              id: button.getAttribute("data-record-id"),
              projectName: button.parentElement.parentElement.children[0].children[0].value,
              projectStatus: button.parentElement.parentElement.children[2].children[0].value,
              projectClientRef: button.parentElement.parentElement.children[1].children[0].value,
          };
          data = JSON.stringify(projectObject);
          console.log(`Updating project with id ${projectObject.id}`);

          xhttp = new XMLHttpRequest();
          xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
              console.log(JSON.parse(xhttp.responseText).result);
              window.location.reload();
            }
          };
          xhttp.open("POST", "/project/update/", true);
          xhttp.setRequestHeader("Content-Type", "application/json");
          xhttp.setRequestHeader("X-CSRFToken", csrfToken);
          xhttp.send(data);
      });
  }
}

// Add an event for each delete button to delete the database record
function addDeleteEvents() {
  var projectObject;
  var data;
  var button;
  var xhttp;
  deleteButtons = document.getElementsByClassName("delete-button");
  for (var i = 0; i < deleteButtons.length; i++) {
    button = deleteButtons[i];
    button.removeEventListener("click", addDeleteEvents);

    button.addEventListener("click", function(event) {
        projectObject = {
            id: button.getAttribute("data-record-id"),
        };
        data = JSON.stringify(projectObject);
        button.parentElement.parentElement.remove();
        console.log(`Deleting project with id ${projectObject.id}`);

        xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
          if (this.readyState == 4 && this.status == 200) {
            console.log(JSON.parse(xhttp.responseText).result);
            window.location.reload();
          }
        };
        xhttp.open("POST", "/project/delete/", true);
        xhttp.setRequestHeader("Content-Type", "application/json");
        xhttp.setRequestHeader("X-CSRFToken", csrfToken);
        xhttp.send(data);
    });
  }
}

// Add an event for the add button to create a new database record
addButton.addEventListener("click", function(event) {
  var xhttp = new XMLHttpRequest();
  var id;
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      id = JSON.parse(xhttp.response).id;
      console.log(`Adding project with id ${id}`);
      window.location.reload();
    }
  };
  xhttp.open("POST", "/project/create/", true);
  xhttp.setRequestHeader("X-CSRFToken", csrfToken);
  xhttp.send();
});

addSaveEvents();
addDeleteEvents();