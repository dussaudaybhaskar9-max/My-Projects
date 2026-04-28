document.getElementById("formContainer").addEventListener("submit",function data(e){
    e.preventDefault()
    let name=document.getElementById("name").value
    let email=document.getElementById("email").value
    let password=document.getElementById("password").value
    let mobile=document.getElementById("mobile").value
    // console.log(name,email,password,mobile);
    

    let userDetails={
        name:name,
        email:email,
        password:password,
        mobile:mobile,
    }
    localStorage.setItem("userDetails",JSON.stringify(userDetails))
    window.location.href="./login.html"

})