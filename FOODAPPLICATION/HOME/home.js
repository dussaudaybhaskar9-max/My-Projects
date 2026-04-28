let items=[]
let itemsContainer = document.getElementById("itemsContainer");

function fetchRecipes() {
    fetch("https://dummyjson.com/recipes").then((res)=>{
        return res.json();
    }).then((val)=>{
        items = val.recipes.map((item) => {
            return {
                ...item,
                price: Math.floor(Math.random() * 500) + 100
            };
        });
        // console.log(val.recipes);
        // items=val.recipes;
        localStorage.setItem("allitems",JSON.stringify(items));  
        displayItems(items);     
    })
}
fetchRecipes()

function displayItems(items){
    // console.log(items);
    let output = "";
    items.map((v)=>{
        output +=`
        <main>
            <div id="items_image">
            <img src="${v.image}"/>
            </div>
            <div id="content">
                <h3>${v.name}</h3>
                 <p>CookTimeMinutes : ${v.cookTimeMinutes}</p>
            <div id="ratingbox">
               <p>Rating : ${v.rating}</p>
               <p>Price : ₹${v.price}</p>
            </div>
            <div id="detailbox">
              <p>Servings : ${v.servings}</p>
              <button onclick="viewDetails(${v.id})">Details</button>
            </div>
            </div>
        </main> 
        `
        console.log(items);
    });
    itemsContainer.innerHTML = output;
}
document.getElementById("searchitem").addEventListener("input", (e) => {
    let searchTerm = e.target.value.toLowerCase();
    let filteredItems = items.filter((v) => {
        return (
            v.name.toLowerCase().includes(searchTerm) || v.cuisine.toLowerCase().includes(searchTerm)
        );
    });
    displayItems(filteredItems);
});
function viewDetails(itemId) {
    console.log(itemId);
    localStorage.setItem("itemId", itemId);
    window.location.href = "../Details/details.html"
}