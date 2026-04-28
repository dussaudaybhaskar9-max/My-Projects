document.getElementById("formContainer").addEventListener("submit",function data(e){
    e.preventDefault()
    let email=document.getElementById("email").value;
    let password=document.getElementById("password").value;

    let userDetails=JSON.parse(localStorage.getItem("userDetails"))
    if(email==userDetails.email && password==userDetails.password){
        window.location.href="../HOME/home.html"
    }
    else{
        alert("Invalid Credentials!!");
    }

})