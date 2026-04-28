document.addEventListener("DOMContentLoaded", () => {
    displayCart()
})
function displayCart() {
    let itemContent = document.getElementById("itemContent");
    let totalPrice = document.getElementById("totalPrice")
    let cartitem = JSON.parse(localStorage.getItem("cartitem")) || [];

    itemContent.innerHTML = "";
    let totalBill = 0;
    if (cartitem.length == 0) {
        itemContent.innerHTML = `<p>Your cart is Empty.Start Shoping....,</p>`
        totalBill.innerHTML = "";
    }
    else {
        cartitem.map((item, i) => {
            totalBill +=(item.price)
            let newItem = document.createElement("div");
            newItem.setAttribute("class", "item_info");
            newItem.innerHTML = `
            <main>
                 <div id="cart_item_img">
                     <img src="${item.image}" alt="">
                 </div>
                 <div id="content_matter">
                     <h1>Name : ${item.name}</h1>
                     <p>Cuisine : ${item.cuisine}</p>
                     <p>PrepTimeMinutes : ${item.prepTimeMinutes}</p>
                     <p>Servings : ${item.servings}</p>
                     <p>Rating : ${item.rating}</p>
                     <p>Price &#8377; ${item.price}</p>
                 </div>
                 <div id="btn_div">
                    <button onclick="removeFromCart(${i})">Remove</button>
                    <button onclick="backToHome()">Back to Home</button>
                </div>
             </main>
            `

            itemContent.append(newItem)
        });
        totalPrice.innerHTML = `<h1>Your totalPrice is : &#8377; ${totalBill}</h1>`

    }
}
function removeFromCart(index){
    // console.log(index);
    let cartitem=JSON.parse(localStorage.getItem("cartitem"))
    cartitem.splice(index,1)
    localStorage.setItem("cartitem",JSON.stringify(cartitem))
    displayCart()   
}
function backToHome(){
    window.location.href="../HOME/home.html"
}


