"use strict";

// Home page buttons

var loginButton = document.getElementById("login-button");
var registerButton = document.getElementById("register-button");
var clientsButton = document.getElementById("clients-button");
var projectsButton = document.getElementById("projects-button");
var logOutButton = document.getElementById("logout-button");

loginButton.addEventListener("click", function() {
    window.location.href = "/accounts/login/";
});

registerButton.addEventListener("click", function() {
    window.location.href = "/accounts/register/";
});

clientsButton.addEventListener("click", function() {
    window.location.href = "/clients/";
});

projectsButton.addEventListener("click", function() {
    window.location.href = "/projects/";
});

logOutButton.addEventListener("click", function() {
    window.location.href = "/accounts/logout/";
});