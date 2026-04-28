document.addEventListener("DOMContentLoaded",() =>{
    let itemsDetails=document.getElementById("itemsDetails");
    let allitems=JSON.parse(localStorage.getItem("allitems"));
    let itemId=localStorage.getItem("itemId");

    if(allitems && itemId){
        let selectedItem = allitems.find((u) => {
            return u.id == itemId;
       })
        console.log(selectedItem);
        if(selectedItem){
            itemsDetails.innerHTML = `
            <main>
               <div id="head_btn_con">
                   <h2>${selectedItem.name}</h2>
                   <div>
                     <button id="addToCart">Add To Cart</button>
                     <button onclick="homepage()">Back to Home</button>
                   </div>
               </div>
               <div id="itemImage">
                   <img src="${selectedItem.image}" alt="">
               </div>
               <div id="itemdetails">
                   <p><strong> Cuisine :</strong> ${selectedItem.cuisine}</p>
                   <p><strong> CaloriesPerServing :</strong> ${selectedItem.caloriesPerServing}</p>
                   <p><strong> CookTimeMinutes :</strong> ${selectedItem.cookTimeMinutes}</p>
                   <p><strong> Servings :</strong> ${selectedItem.servings}</p>
                   <p><strong> Ingredients :</strong> ${selectedItem.ingredients}</p>
                   <p><strong> Rating :</strong> ${selectedItem.rating}</p>
                   <p><strong> Price &#8377;</strong> ${selectedItem.price}</p>
               </div>
            </main>
            `;
            document.getElementById("addToCart").addEventListener("click",()=>{
                cartItem(selectedItem)
            });
        }else{
            itemsDetails.innerHTML="Item is not avaliable"
        }
    }
    else{
        itemsDetails.innerHTML = "NO Item Found.."
    }   
});
function homepage(){
    window.location.href="../HOME/home.html"
}
function cartItem(item){
    // console.log(item);
    let cartitem=JSON.parse(localStorage.getItem("cartitem")) || [];
    cartitem.push(item);
    localStorage.setItem("cartitem",JSON.stringify(cartitem));
    alert("Food Added Successfully..") 
}